import pydantic as pdt
from aoe2rms.commands import CommandModel
from aoe2rms.constants import TerrainConstant


class CreateElevation(CommandModel):
    """Command to create hills of various heights on the map."""

    _command_name: str = "create_elevation"
    _command_parameters = ("height",)

    height: int = pdt.Field(
        ge=1,
        le=16,
        description="Maximum height of hills (1-16). In pre-DE versions, maximum is 7. "
        "Hills with a small number of base tiles may not reach max height.",
    )

    base_terrain: str | TerrainConstant | None = pdt.Field(
        default=None,
        description="Terrain on which the hill(s) should generate. Multiple terrain types "
        "require multiple create_elevation commands.",
        examples=["GRASS"],
    )

    base_layer: str | TerrainConstant | None = pdt.Field(
        default=None,
        description="Used in combination with base_terrain if a base layer was specified in "
        "LAND_GENERATION. DE only.",
        examples=["SNOW"],
    )

    number_of_tiles: int | None = pdt.Field(
        default=None,
        description="Total base tile count allocated to this command. If number_of_clumps is "
        "specified, this value is divided among the clumps.",
        examples=[600],
    )

    number_of_clumps: int | None = pdt.Field(
        default=None,
        description="Number of individual hills to create. If clumps are adjacent, "
        "the hills may merge.",
        examples=[4],
    )

    set_scale_by_size: bool | None = pdt.Field(
        default=None,
        description="Scales number_of_tiles to the map size. Unscaled value refers to a "
        "100x100 map. In AoC/UP/HD this scales number_of_clumps instead (bug).",
    )

    set_scale_by_groups: bool | None = pdt.Field(
        default=None,
        description="Scales number_of_clumps to the map size. Unscaled value refers to a "
        "100x100 map. In AoC/UP/HD this scales number_of_tiles instead (bug).",
    )

    spacing: int | None = pdt.Field(
        default=None,
        description="Number of tiles between each elevation level. Numbers larger than 1 "
        "will produce rings of flat terrain on each level of a hill.",
        examples=[4],
    )

    enable_balanced_elevation: bool | None = pdt.Field(
        default=None,
        description="Removes the bias of hill placement towards the bottom (south) of the map. "
        "DE only, recommended to always include this.",
    )
