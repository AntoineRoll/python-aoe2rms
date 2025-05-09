from aoe2rms.constants import Constant
from aoe2rms import Script
from pydantic import BaseModel

class Variable(Script):
    name: str
    
    def compile(self, prefix = ""):
        result = f"{prefix}#define {self.name}\n"
        return result

class ConditionalConstant(BaseModel):
    
    first_condition: str
    first_output: Constant | list[Constant]
    
    additional_conditions: list[tuple[str, Constant | list[Constant]]] | None = None
    
    else_output: Constant | list[Constant] | None = None
    
    def model_post_init(self, context):
        if isinstance(self.first_output, Constant):
            self.first_output = [self.first_output]
            
        if self.else_output is not None and isinstance(self.else_output, Constant):
            self.else_output = [self.else_output]
            
        if self.additional_conditions is None:
            self.additional_conditions = []
            
        for i, (_, output) in enumerate(self.additional_conditions):
            if isinstance(output, Constant):
                self.additional_conditions[i] = (_, [output])
        return super().model_post_init(context)
    
    def compile(self):
        
        result = ""
        
        # First if command
        result += f"if {self.first_condition}\n"
    
        for constant in self.first_output:
            result += f"\t{constant.declare()}"
            
        # Optional elseif commands
        for (condition, constants) in self.additional_conditions:
            result += f"elseif {condition}\n"
        
            for constant in constants:
                result += f"\t{constant.declare()}"
                
        # Optional else command
        if self.else_output:
            result += "else\n"
            for constant in self.else_output:
                result += f"\t{constant.declare()}"
            
        result += "endif\n"
        
        return result