from pydantic import BaseModel, Field

from aoe2rms.constants import Constant


class BaseGenerationModel(BaseModel):
    _header: str
    constants: list[Constant] = Field(default_factory=list)
    commands: list[BaseModel] = Field(default_factory=list)


    def compile(self):
        result = f"{self._header}\n\n"

        for constant in self.constants:
            result += constant.declare()

        for attr, val in self.__dict__.items():
            if attr not in ("commands", "constants") and val is not None:
                result += f"{attr} {val}\n"

        result += "\n"
        for command in self.commands:
            result += command.compile()

        return result
    
    @classmethod
    def get_current_commands(self):
        return self.commands
    
    @classmethod
    def get_current_constants(self):
        return self.constants

    def __enter__(self) -> BaseModel:
        BaseGenerationModel.commands = self.commands
        BaseGenerationModel.constants = self.constants
        return self

    def __exit__(self, *args) -> None:
        return None