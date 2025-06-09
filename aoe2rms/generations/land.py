import pydantic as pdt

from aoe2rms.generations.base import BaseGenerationModel
from aoe2rms.constants import TerrainConstant


class LandGeneration(BaseGenerationModel):
    """Land Generation section of the RMS script.

    This section places large areas of terrain, including the player starting areas.
    It's required if you want to place players.
    """

    _header: str = "<LAND_GENERATION>"

    base_terrain: str | TerrainConstant = pdt.Field(
        default="GRASS",
        description="Specify a terrain to initially fill the map. Maps with rivers or oceans "
        "usually use water. Maps with forest on the outside usually use forest terrain.",
        examples=["GRASS", "WATER", "DIRT", "DESERT"],
    )
    base_layer: str | TerrainConstant = pdt.Field(
        default=None,
        description="Specify a terrain to layer on top of the map's base_terrain. "
        "This layered terrain is visual only, and does not confer any "
        "terrain properties or object restrictions.",
        examples=["SNOW", "DESERT", "DLC_CRACKED"],
    )

    enable_waves: bool | None = pdt.Field(
        default=None,
        description="Enables or disables animated beach waves on your map. "
        "Waves are only visible if the player has 'Render Beach Waves' turned on in the game settings.",
        examples=[True, False],
    )

    def assign_to_map(self):
        self.map.land_generation = self
