import logging
import os
from pydantic import BaseModel, Field
from typing import Optional, List, Union

from aoe2rms.generations.base import BaseGenerationModel
from aoe2rms.generations.land import LandGeneration
from aoe2rms.generations.elevation import ElevationGeneration
from aoe2rms.generations.cliff import CliffGeneration
from aoe2rms.generations.terrain import TerrainGeneration
from aoe2rms.generations.connection import ConnectionGeneration
from aoe2rms.generations.objects import ObjectsGeneration


class PlayerSetup(BaseGenerationModel):
    """Model for PLAYER_SETUP section in RMS scripts."""

    _header: str = "<PLAYER_SETUP>"

    # Placement options - mutually exclusive
    random_placement: bool = True
    grouped_by_team: bool = False
    direct_placement: bool = False

    # Nomad options
    nomad_resources: bool = False
    force_nomad_treaty: bool = False

    # Version options
    behavior_version: Optional[int] = None
    override_map_size: Optional[int] = None

    # Gaia and AI options
    set_gaia_civilization: Optional[int] = None
    ai_info_map_type: Optional[List[Union[str, int]]] = None

    # Effect modifications
    effect_amount: Optional[List[str]] = None
    effect_percent: Optional[List[str]] = None

    # Special states
    guard_state: Optional[List[Union[str, int]]] = None
    terrain_state: Optional[List[int]] = None
    weather_type: Optional[List[int]] = None

    def compile(self):
        """Custom compilation for player setup section"""
        result = f"{self._header}\n\n"

        # Handle placement options
        if self.random_placement:
            result += "random_placement\n"
        elif self.grouped_by_team:
            result += "grouped_by_team\n"
        elif self.direct_placement:
            result += "direct_placement\n"

        # Handle nomad options
        if self.nomad_resources:
            result += "nomad_resources\n"
        if self.force_nomad_treaty:
            result += "force_nomad_treaty\n"

        # Handle other options
        if self.behavior_version is not None:
            result += f"behavior_version {self.behavior_version}\n"
        if self.override_map_size is not None:
            result += f"override_map_size {self.override_map_size}\n"
        if self.set_gaia_civilization is not None:
            result += f"set_gaia_civilization {self.set_gaia_civilization}\n"

        # Handle more complex options
        if self.ai_info_map_type:
            result += f"ai_info_map_type {' '.join(map(str, self.ai_info_map_type))}\n"

        if self.effect_amount:
            for effect in self.effect_amount:
                result += f"effect_amount {effect}\n"

        if self.effect_percent:
            for effect in self.effect_percent:
                result += f"effect_percent {effect}\n"

        if self.guard_state:
            result += f"guard_state {' '.join(map(str, self.guard_state))}\n"

        if self.terrain_state:
            result += f"terrain_state {' '.join(map(str, self.terrain_state))}\n"

        if self.weather_type:
            result += f"weather_type {' '.join(map(str, self.weather_type))}\n"

        result += "\n"
        return result


class Map(BaseModel):
    """Main class for generating complete RMS scripts."""

    # Map metadata
    name: str
    description: Optional[str] = None
    author: Optional[str] = None

    # RMS Sections in the order they are processed
    player_setup: PlayerSetup = Field(default_factory=PlayerSetup)
    land_generation: LandGeneration = Field(default_factory=LandGeneration)
    elevation_generation: Optional[ElevationGeneration] = None
    cliff_generation: Optional[CliffGeneration] = None
    terrain_generation: Optional[TerrainGeneration] = None
    connection_generation: Optional[ConnectionGeneration] = None
    objects_generation: Optional[ObjectsGeneration] = None

    # Global script elements
    global_comments: List[str] = Field(default_factory=list)
    global_definitions: List[str] = Field(default_factory=list)
    random_scripts: List[str] = Field(default_factory=list)
    conditional_scripts: List[str] = Field(default_factory=list)

    def compile(self) -> str:
        """Generate the complete RMS script."""
        script = f"/* {self.name} */\n"

        if self.author:
            script += f"/* Author: {self.author} */\n"
        if self.description:
            script += f"/* {self.description} */\n"

        script += "\n"
        logging.debug("%s - Header comments scripted.", self.__class__.__name__)

        # Add global elements
        for comment in self.global_comments:
            script += f"/* {comment} */\n"

        for definition in self.global_definitions:
            script += f"{definition}\n"

        for random_script in self.random_scripts:
            script += f"{random_script}\n"

        for conditional in self.conditional_scripts:
            script += f"{conditional}\n"
        logging.debug("%s - Global elements scripted.", self.__class__.__name__)

        script += "\n"

        # Compile each section in order
        script += self.player_setup.compile()
        logging.debug("%s - Player setup scripted.", self.__class__.__name__)

        script += self.land_generation.compile()
        logging.debug("%s - Land generation scripted.", self.__class__.__name__)

        if self.elevation_generation:
            script += self.elevation_generation.compile()
            logging.debug(
                "%s - Elevation generation scripted.", self.__class__.__name__
            )

        if self.cliff_generation:
            script += self.cliff_generation.compile()
            logging.debug("%s - Cliff generation scripted.", self.__class__.__name__)

        if self.terrain_generation:
            script += self.terrain_generation.compile()
            logging.debug("%s - Terrain generation scripted.", self.__class__.__name__)

        if self.connection_generation:
            script += self.connection_generation.compile()
            logging.debug(
                "%s - Connection generation scripted.", self.__class__.__name__
            )

        if self.objects_generation:
            script += self.objects_generation.compile()
            logging.debug("%s - Objects generation scripted.", self.__class__.__name__)

        return script.strip()

    def save_to_file(self, file_path, overwrite=False):
        if os.path.exists(file_path) and not overwrite:
            raise FileExistsError(f"File {file_path} already exists. Set explicitly `overwrite=True` to write anyway.")
        with open(file_path, "w") as file:
            file.write(self.compile())
