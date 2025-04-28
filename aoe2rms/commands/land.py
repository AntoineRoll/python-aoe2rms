import pydantic as pdt

from aoe2rms.commands import CommandModel


class CreateLand(CommandModel):
    """Create a single land area on the map.

    This command creates a non-player (neutral) land which can be assigned to a player
    with assign_to_player or assign_to attributes.
    """

    _command_name: str = "create_land"

    terrain_type: str = pdt.Field(
        description="Specifies which terrain the land should have",
        examples=["GRASS", "WATER", "DESERT", "SNOW"],
    )
    land_percent: int = pdt.Field(
        default=None,
        strict=True,
        ge=0,
        le=100,
        description="Percentage of the total map that the land should grow to cover. "
        "If land growth is constrained by borders or other lands, "
        "lands may be smaller than specified.",
        examples=[10, 20, 50],
    )

    number_of_tiles: int = pdt.Field(
        default=None,
        description="Fixed number of tiles that the land should grow by. "
        "Total size of the land is number_of_tiles in addition "
        "to the square origin specified by base_size.",
        examples=[100, 250, 500],
    )

    base_size: int = pdt.Field(
        default=3,
        description="Square radius of the initially placed land origin, before any growth. "
        "The default of 3 results in a 7x7 land origin (49 tiles total).",
        examples=[3, 6, 12],
    )

    land_position: str = pdt.Field(
        default=None,
        description="Specifies the exact origin point for a land, as a percentage of total map dimensions. "
        "Format: 'X Y' where both are percentages. 50 50 is the center of the map.",
        examples=["50 50", "25 75", "10 90"],
    )

    left_border: int = pdt.Field(
        default=None,
        description="Percentage of map width for land placement and growth to stay away from the left (southwest) border",
        examples=[5, 10, 40],
    )

    right_border: int = pdt.Field(
        default=None,
        description="Percentage of map width for land placement and growth to stay away from the right (northeast) border",
        examples=[5, 10, 40],
    )

    top_border: int = pdt.Field(
        default=None,
        description="Percentage of map width for land placement and growth to stay away from the top (northwest) border",
        examples=[5, 10, 40],
    )

    bottom_border: int = pdt.Field(
        default=None,
        description="Percentage of map width for land placement and growth to stay away from the bottom (southeast) border",
        examples=[5, 10, 40],
    )

    border_fuzziness: int = pdt.Field(
        default=20,
        description="Specifies the extent to which land growth respects borders. "
        "Low values allow lands to exceed borders, high values (closer to 100) "
        "make borders more strict.",
        examples=[0, 20, 100],
    )

    clumping_factor: int = pdt.Field(
        default=8,
        description="The extent to which land growth prefers to clump together. "
        "Moderate values (11-40) create rounder lands, while low values (0-10) "
        "create more irregular lands.",
        examples=[2, 8, 30],
    )

    base_elevation: int = pdt.Field(
        default=None,
        ge=0,
        le=16,
        description="Elevate the entire land to the specified height. "
        "Values higher than 7 may cause rendering issues.",
        examples=[1, 2, 3],
    )

    assign_to_player: int = pdt.Field(
        default=None,
        description="Assign a land to one specific player (1-8), allows placing starting "
        "objects for that player on this land.",
        examples=[1, 2, 3],
    )

    zone: int = pdt.Field(
        default=None,
        description="Set a numeric zone. Lands sharing the same zone can grow to touch each other.",
        examples=[1, 2, -1],
    )

    other_zone_avoidance_distance: int = pdt.Field(
        default=None,
        description="Number of tiles away from a land with a different zone to stop land growth. "
        "Used to create river maps and island maps.",
        examples=[5, 10, 20],
    )

    min_placement_distance: int = pdt.Field(
        default=None,
        description="Number of tiles to stay away from the origins of previously created lands "
        "when randomly selecting an origin for this land.",
        examples=[10, 25, 40],
    )

    land_id: int = pdt.Field(
        default=None,
        description="Assign a numeric label to a land, which can later be used to place objects "
        "specifically on that land with place_on_specific_land_id.",
        examples=[1, 13, 42],
    )


class CreatePlayerLands(CreateLand):
    _command_name = "create_player_lands"
