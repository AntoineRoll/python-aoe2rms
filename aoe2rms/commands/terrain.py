import pydantic as pdt

from aoe2rms.commands import CommandModel
from aoe2rms.constants import TerrainConstant


class CreateTerrain(CommandModel):
    """
    Command to create terrain and its attributes according to the RMS specification.
    """

    _command_name: str = "create_terrain"
    _command_parameters = ("terrain_type",)

    # The terrain_type parameter is part of the command syntax itself
    # e.g. create_terrain FOREST { ... }
    terrain_type: str | TerrainConstant

    # Attributes
    base_terrain: str | TerrainConstant | None = None
    base_layer: str | TerrainConstant | None = None
    beach_terrain: str | None = None
    terrain_mask: int | None = pdt.Field(default=None, ge=1, le=2)
    spacing_to_other_terrain_types: int | None = None
    set_flat_terrain_only: bool | None = None

    # Mutually exclusive attributes - either land_percent or number_of_tiles
    land_percent: int | None = pdt.Field(default=None, ge=1, le=100)
    number_of_tiles: int | None = None

    number_of_clumps: int | None = None
    clumping_factor: int | None = None

    # Scaling options (mutually exclusive)
    set_scale_by_size: bool | None = None
    set_scale_by_groups: bool | None = None

    # Player start area avoidance
    set_avoid_player_start_areas: int | None = None

    # Height-based placement
    height_limits: list[int] | None = pdt.Field(default=None, min_items=2, max_items=2)
