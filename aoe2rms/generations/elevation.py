import pydantic as pdt

from aoe2rms.generations import BaseGenerationModel


class ElevationGeneration(BaseGenerationModel):
    """
    Optional section used to place hills on the map.
    - Elevation avoids the origins of player lands by about 9 tiles.
    - If base_elevation was specified for any lands, this section must be included, even if empty.
    - Elevation provides a combat bonus to higher units, and a debuff to lower units.
    """

    _header: str = "<ELEVATION_GENERATION>"

    commands: list[pdt.BaseModel] = pdt.Field(
        default_factory=list,
        description="List of create_elevation commands to generate hills on the map",
    )
