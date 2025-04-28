from pydantic import Field
from typing import Tuple
from aoe2rms.commands.base import CommandModel


class CreateLand(CommandModel):
    """
    Command to create a single non-player (neutral) land according to the RMS specification.
    """

    _command_name: str = "create_land"
    _command_parameters = ("terrain_type",)

    # Parameters and attributes as described in RmsLandReference.md
    terrain_type: str | None = Field(
        default=None, description="Specify which terrain the land should have."
    )
    land_percent: int | None = Field(
        default=None,
        ge=0,
        le=100,
        description="Percentage of the total map that the land should grow to cover.",
    )
    number_of_tiles: int | None = Field(
        default=None, description="Fixed number of tiles that the land should grow by."
    )
    base_size: int | None = Field(
        default=3,
        ge=1,
        description="Square radius of the initially placed land origin, before any growth.",
    )
    land_position: Tuple[int, int] | None = Field(
        default=None,
        min_items=2,
        max_items=2,
        description="Exact origin point for a land, as a percentage of total map dimensions.",
    )
    circle_radius: Tuple[int, int] | None = Field(
        default=None,
        min_items=1,
        max_items=2,
        description="Position the player lands in a circle with equal distance to the center, with specified variance.",
    )
    left_border: int | None = Field(
        default=0,
        ge=0,
        le=99,
        description="Specify a percentage of map width for land placement and growth to stay away from the left border.",
    )
    right_border: int | None = Field(
        default=0,
        ge=0,
        le=99,
        description="Specify a percentage of map width for land placement and growth to stay away from the right border.",
    )
    top_border: int | None = Field(
        default=0,
        ge=0,
        le=99,
        description="Specify a percentage of map width for land placement and growth to stay away from the top border.",
    )
    bottom_border: int | None = Field(
        default=0,
        ge=0,
        le=99,
        description="Specify a percentage of map width for land placement and growth to stay away from the bottom border.",
    )
    border_fuzziness: int | None = Field(
        default=20,
        ge=0,
        le=100,
        description="Specifies the extent to which land growth respects borders and actually stops at a border.",
    )
    clumping_factor: int | None = Field(
        default=8,
        description="The extent to which land growth prefers to clump together near existing tiles.",
    )
    base_elevation: int | None = Field(
        default=0,
        ge=0,
        le=16,
        description="Elevate the entire land to the specified height.",
    )
    assign_to_player: int | None = Field(
        default=None, ge=1, le=8, description="Assign a land to one specific player."
    )
    assign_to: Tuple[str, int, int, int] | None = Field(
        default=None,
        description="A more powerful version of assign_to_player. Assign a land to one specific player, allowing you to place starting objects on that land for that player.",
    )
    zone: int | None = Field(
        default=None,
        ge=-99,
        description="Set a numeric zone. Lands sharing the same zone can grow to touch each other.",
    )
    other_zone_avoidance_distance: int | None = Field(
        default=0,
        ge=0,
        description="Number of tiles away from a land with a different zone to stop land growth.",
    )
    min_placement_distance: int | None = Field(
        default=None,
        ge=0,
        description="Number of tiles to stay away from the origins of previously created lands when randomly selecting an origin for this land.",
    )
