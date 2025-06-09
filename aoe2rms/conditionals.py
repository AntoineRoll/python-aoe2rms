from aoe2rms.constants import Constant
from aoe2rms import Script

class Attribute(Script):
    name: str
    value: str | int
    
    def compile(self, prefix = ""):
        return f"{prefix}{self.name} {self.value}\n"

class Variable(Script):
    name: str

    def compile(self, prefix=""):
        result = f"{prefix}#define {self.name}\n"
        return result

class ConditionalScript(Script):
    
    cases: list[tuple[str, Script | str]]
    else_case: Script | str | None = None
    
    def compile(self, prefix=""):
        result = ""
        is_first = True
        for condition, script in self.cases:
            if is_first:
                result += f"{prefix}if {condition}"
            else:
                result += f"{prefix}elseif {condition}"
            
            if isinstance(script, Script):
                result += "\n" + script.compile(prefix + "\t")
            else:
                result += f" {prefix}\t{script}\n"
            
            is_first = False
            
        if self.else_case is not None:
            result += f"{prefix}else\n"
            if isinstance(self.else_case, Script):
                result += self.else_case.compile(prefix + "\t")
            else:
                result += f"{prefix}\t{self.else_case}\n"
        result += f"{prefix}endif\n"
        return result

class ConditionalAttribute(ConditionalScript):
    cases: list[tuple[str, Attribute]]
    else_case: Attribute | None = None

class ConditionalConstant(Script):
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
        for condition, constants in self.additional_conditions:
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
