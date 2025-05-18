import logging
from pydantic import BaseModel, Field
from typing import Any

from aoe2rms.constants import Constant


class BaseGenerationModel(BaseModel):
    _header: str
    constants: list[Constant] = Field(default_factory=list)
    commands: list[BaseModel] = Field(default_factory=list)
    map: Any | None = None

    def compile(self):
        result = f"{self._header}\n\n"
        logging.debug("%s - Header scripted.", self.__class__.__name__)

        for constant in self.constants:
            result += constant.declare()
        if self.constants:
            logging.debug("%s - Constants scripted.", self.__class__.__name__)

        for attr, val in self.__dict__.items():
            if attr not in ("commands", "constants", "map") and val is not None:
                result += f"{attr} {val}\n"
                logging.debug(
                    "%s - %s - Attributes scripted.", self.__class__.__name__, attr
                )

        result += "\n"
        for command in self.commands:
            result += command.compile()
            logging.debug(
                "%s - %s - Commands scripted.",
                self.__class__.__name__,
                command.__class__.__name__,
            )

        return result

    @classmethod
    def get_current_commands(self):
        if hasattr(self, "commands"):
            return self.commands

    @classmethod
    def get_current_constants(self):
        if hasattr(self, "constants"):
            return self.constants

    def __enter__(self) -> BaseModel:
        BaseGenerationModel.commands = self.commands
        BaseGenerationModel.constants = self.constants
        return self

    def assign_to_map(self) -> None:
        raise NotImplementedError

    def __exit__(self, *args) -> None:
        if self.map:
            self.assign_to_map()
        return None
