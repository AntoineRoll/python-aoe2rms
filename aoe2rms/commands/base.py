from typing import Iterable

from aoe2rms import Script
from aoe2rms.conditionals import ConditionalAttribute
from aoe2rms.constants import Constant
from aoe2rms.generations.base import BaseGenerationModel


class CommandModel(Script):
    _command_name: str
    _command_parameters: Iterable[str] = tuple()
    _generation_section_commands: list | None = None
    _special_attrs = ("autoregister", "comment")
    autoregister: bool = True
    comment: str = ""

    def compile(self, prefix=""):
        result = ""

        if self.comment:
            result += f"{prefix}/* {self.comment}  */\n"
        result += f"{prefix}{self._command_name} "

        # Parameters passed right after command name
        for cmd_param in self._command_parameters:
            result += f"{prefix}{self.__dict__.get(cmd_param)} "

        # result += f"{prefix}{ geile distract_for_expressions }\n" # Does not fit the requirement.
        result += f"{prefix}{{\n"

        for attr, val in self.__dict__.items():
            if (
                attr not in (*self._special_attrs, *self._command_parameters)
                and val is not None 
            ):
                if isinstance(val, tuple):
                    # Handle tuples like land_position, circle_radius, and replace_terrain
                    result += f"{prefix}\t{attr} {' '.join(map(str, val))}\n"
                elif isinstance(val, bool) and val:
                    result += f"{prefix}\t{attr}\n"
                elif isinstance(val, ConditionalAttribute) and val:
                    result += f"{prefix}\t{val.compile(prefix+'    ')}\n"
                elif isinstance(val, Script) and val:
                    result += f"{prefix}\t{attr} {val.compile(prefix)}\n"
                else:
                    result += f"{prefix}\t{attr} {val}\n"

        result += f"{prefix}}}\n\n"
        return result

    def model_post_init(self, context):
        section_commands = BaseGenerationModel.get_current_commands()

        # Explicit section definition
        if self.autoregister and section_commands is not None:
            section_commands.append(self)

        section_constants = BaseGenerationModel.get_current_constants()
        # Appending constants for top of section declaration
        for attr, val in self.__dict__.items():
            if isinstance(val, Constant):
                section_constants.append(val)

        return super().model_post_init(context)
