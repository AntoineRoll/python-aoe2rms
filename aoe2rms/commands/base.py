import pydantic as pdt
from typing import Iterable

from aoe2rms.constants import Constant
from aoe2rms.generations.base import BaseGenerationModel


class CommandModel(pdt.BaseModel):
    _command_name: str
    _command_parameters: Iterable[str] = tuple()
    _generation_section_commands: list | None = None
    comment: str = ""

    def compile(self):
        result = ""

        if self.comment:
            result += f"/* {self.comment}  */\n"
        result += f"{self._command_name} "

        # Parameters passed right after command name
        for cmd_param in self._command_parameters:
            result += f"{self.__dict__.get(cmd_param)} "

        result += "{\n"

        for attr, val in self.__dict__.items():
            if val is not None and attr not in self._command_parameters:
                if isinstance(val, tuple):
                    # Handle tuples like land_position, circle_radius, and replace_terrain
                    result += f"\t{attr} {' '.join(map(str, val))}\n"
                elif isinstance(val, bool) and val:
                    result += f"\t{attr}\n"
                else:
                    result += f"\t{attr} {val}\n"

        result += "}\n\n"
        return result

    def model_post_init(self, context):
        section_commands = BaseGenerationModel.get_current_commands()

        # Explicit section definition
        if section_commands is not None:
            section_commands.append(self)

        section_constants = BaseGenerationModel.get_current_constants()
        # Appending constants for top of section declaration
        for attr, val in self.__dict__.items():
            if isinstance(val, Constant):
                section_constants.append(val)

        return super().model_post_init(context)
