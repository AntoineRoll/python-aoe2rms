import pydantic as pdt

from aoe2rms.commands import CommandModel


class CreateObject(CommandModel):
    """
    Command to create objects and its attributes according to the RMS specification.
    """

    _command_name: str = "create_object"

    # The object_type parameter is part of the command syntax itself
    # e.g. create_object TOWN_CENTER { ... }
    object_type: str = pdt.Field(
        ...,
        description="The type of object to create. Must be a valid object constant.",
        examples=["TOWN_CENTER", "GOLD", "RELIC", "SHEEP", "VILLAGER", "SCOUT"],
    )

    # Basic object attributes
    number_of_objects: int | None = pdt.Field(
        default=None,
        description="Number of individual objects to create. For villagers, omitting this will give "
        "each civilization their correct number of starting villagers.",
        examples=[1, 4, 10],
    )
    number_of_groups: int | None = pdt.Field(
        default=None,
        description="Place the specified number of groups. Each group consists of the number of individual "
        "objects chosen in number_of_objects. Total objects = number_of_objects × number_of_groups.",
        examples=[1, 2, 10],
    )
    group_variance: int | None = pdt.Field(
        default=None,
        description="Randomly varies the number_of_objects by up to the amount specified. "
        "A minimum of 1 object will always be generated even if the variance would make the count 0 or negative.",
        examples=[1, 2, 3],
    )
    group_placement_radius: int | None = pdt.Field(
        default=None,
        description="Number of tiles out from the central tile that objects belonging to the same group may spawn. "
        "Activates grouping behavior. Useful for keeping resources from forming long lines.",
        examples=[1, 2, 3],
    )
    set_tight_grouping: bool | None = pdt.Field(
        default=None,
        description="Objects belonging to the same group must be in adjacent tiles. Commonly used for berries, gold and stone. "
        "Mutually exclusive with set_loose_grouping.",
        examples=[True],
    )
    set_loose_grouping: bool | None = pdt.Field(
        default=None,
        description="Objects belonging to the same group can be placed anywhere within the confines of group_placement_radius. "
        "This is the default type of grouping. Commonly used for sheep and deer.",
        examples=[True],
    )
    min_connected_tiles: int | None = pdt.Field(
        default=None,
        description="Prevents grouped objects from being placed in an area with fewer tiles than the specified amount. "
        "Intended to keep objects off tiny islands and out of tiny forest clearings. "
        "Note: This can cause objects to be biased toward being placed in the top left of the map.",
        examples=[10, 20, 50],
    )
    resource_delta: int | None = pdt.Field(
        default=None,
        description="Modifies the resource amount of resources. Can be positive or negative. "
        "For example, gold mines with -100 will have 100 less gold.",
        examples=[-100, 0, 100],
    )
    second_object: str | None = pdt.Field(
        default=None,
        description="Specifies any object to be placed on top of the main object. If you are placing multiple objects, "
        "each will get the specified second object.",
        examples=["VILLAGER", "SHEEP", "FORAGE_BUSH"],
    )

    # Scaling attributes
    set_scaling_to_map_size: bool | None = pdt.Field(
        default=None,
        description="Scales number_of_groups to the map size. If no grouping is present, "
        "scaling applies to number_of_objects instead.",
        examples=[True],
    )
    set_scaling_to_player_number: bool | None = pdt.Field(
        default=None,
        description="Scales number_of_groups to player count. This means ×2 for a 2-player game "
        "and ×8 for an 8-player game. If no grouping is present, scaling applies to number_of_objects instead.",
        examples=[True],
    )

    # Placement attributes
    set_place_for_every_player: bool | None = pdt.Field(
        default=None,
        description="Place the object(s) as a personal object for each player. Objects that cannot be owned by players "
        "(boar, gold, trees, etc.) also require set_gaia_object_only. "
        "Mutually exclusive with place_on_specific_land_id.",
        examples=[True],
    )
    place_on_specific_land_id: int | None = pdt.Field(
        default=None,
        description="Place the object(s) on each land of the specified identifier. IDs are set in LAND_GENERATION by using "
        "the land_id attribute. Mutually exclusive with set_place_for_every_player.",
        examples=[1, 13, 42],
    )
    generate_for_first_land_only: bool | None = pdt.Field(
        default=None,
        description="When used with player objects, this will place objects only for the first player, "
        "rather than for all players.",
        examples=[True],
    )

    # Gaia object attributes
    set_gaia_object_only: bool | None = pdt.Field(
        default=None,
        description="Use with set_place_for_every_player to place gaia (neutral) objects on a per-player basis. "
        "Must be used when placing player's gold/stone/berries/deer/boar.",
        examples=[True],
    )
    set_gaia_unconvertible: bool | None = pdt.Field(
        default=None,
        description="Makes monks and missionaries unable to convert the units. Does not work when testing "
        "from the scenario editor. Unrescuable status does not apply to second_object.",
        examples=[True],
    )
    set_building_capturable: bool | None = pdt.Field(
        default=None,
        description="Used to make a building switch control to whoever most recently has units nearby. "
        "Has no effect on units or other non-building objects.",
        examples=[True],
    )
    make_indestructible: bool | None = pdt.Field(
        default=None,
        description="Make a building indestructible. The building receives 9999 HP, 1000/1000 armor, "
        "and cannot be attacked, damaged or deleted. Has no effect on units or other non-building objects.",
        examples=[True],
    )

    # Distance constraints
    min_distance_to_players: int | None = pdt.Field(
        default=None,
        description="Minimum distance in tiles from the origin of player lands that the object can be placed. "
        "When used with set_place_for_every_player or place_on_specific_land_id, this applies to ALL lands in "
        "versions before April 2025 update.",
        examples=[0, 7, 15],
    )
    max_distance_to_players: int | None = pdt.Field(
        default=None,
        description="Maximum distance in tiles from the origin of player lands that the object can be placed. "
        "If min exceeds max, no objects are placed.",
        examples=[9, 15, 30],
    )
    set_circular_placement: bool | None = pdt.Field(
        default=None,
        description="Changes min_distance_to_players and max_distance_to_players to use the circular (Euclidean) distance, "
        "rather than a square radius. This prevents resources on the diagonal from being very far away.",
        examples=[True],
    )

    # Terrain constraints
    terrain_to_place_on: str | None = pdt.Field(
        default=None,
        description="Object will only be placed on the specified terrain type. Using this largely overrides "
        "the default terrain restrictions for the object.",
        examples=["GRASS", "DESERT", "WATER"],
    )
    layer_to_place_on: str | None = pdt.Field(
        default=None,
        description="Object will only be placed on the specified layered terrain. This allows placement "
        "on visual layers, not just base terrains.",
        examples=["GRASS", "DESERT", "SNOW"],
    )
    ignore_terrain_restrictions: bool | None = pdt.Field(
        default=None,
        description="Objects can be placed on terrains they are normally restricted from. Must be used "
        "with set_place_for_every_player or place_on_specific_land_id.",
        examples=[True],
    )

    # Zone constraints
    max_distance_to_other_zones: int | None = pdt.Field(
        default=None,
        description="Minimum distance, in tiles, that objects will stay away from terrains that they are "
        "restricted from being placed on. Useful for keeping resources away from coastlines.",
        examples=[1, 3, 5],
    )
    place_on_forest_zone: bool | None = pdt.Field(
        default=None,
        description="Place objects only on, and directly next to, tiles with trees on them (including straggler "
        "trees and scenario editor trees).",
        examples=[True],
    )
    avoid_forest_zone: int | None = pdt.Field(
        default=None,
        description="Objects will stay the specified number of tiles away from any trees. "
        "Defaults to 1 if you specify the attribute but omit the distance.",
        examples=[1, 2, 5],
    )
    avoid_cliff_zone: int | None = pdt.Field(
        default=None,
        description="Objects will stay the specified number of tiles away from cliffs. "
        "Defaults to 1 if you specify the attribute but omit the distance.",
        examples=[1, 2, 3],
    )

    # Edge constraints
    min_distance_to_map_edge: int | None = pdt.Field(
        default=None,
        description="Minimum distance, in tiles, that objects will stay away from the edge of the map.",
        examples=[3, 5, 10],
    )

    # Other group placement constraints
    min_distance_group_placement: int | None = pdt.Field(
        default=None,
        description="Minimum distance, in tiles, that individual objects of the same create_object command, "
        "and ALL future objects, must stay away from each object.",
        examples=[2, 4, 8],
    )
    temp_min_distance_group_placement: int | None = pdt.Field(
        default=None,
        description="Like min_distance_group_placement, but only applies to the current create_object command - "
        "future objects are unaffected. Useful for scattering objects like neutral resources and relics.",
        examples=[15, 25, 40],
    )

    # Placement logic
    find_closest: bool | None = pdt.Field(
        default=None,
        description="Place the object on the closest free tile to the origin of its associated land. "
        "Uses circular (Euclidean) distance, while other distance constraints use square distance by default.",
        examples=[True],
    )
    find_closest_to_map_center: bool | None = pdt.Field(
        default=None,
        description="Place the object on the closest free tile to the center of the map. "
        "Overridden by find_closest.",
        examples=[True],
    )
    find_closest_to_map_edge: bool | None = pdt.Field(
        default=None,
        description="Place the object on the closest free tile to the edge of the map. "
        "Overridden by find_closest and find_closest_to_map_center.",
        examples=[True],
    )
    require_path: int | None = pdt.Field(
        default=None,
        description="Objects with this attribute must have a path to the origin of their associated land. "
        "Use this attribute to prevent player resources from being trapped in or behind forests.",
        examples=[1, 2],
    )
    force_placement: bool | None = pdt.Field(
        default=None,
        description="Allows multiple objects to be placed on the same tile at once, if necessary. "
        "Only works for objects that can overlap on the same tile (units, not buildings). "
        "Disabled when using set_loose_grouping.",
        examples=[True],
    )

    # Actor area attributes
    actor_area: int | None = pdt.Field(
        default=None,
        description="Specifies a numerical identifier which can be referred to in future objects with "
        "avoid_actor_area or actor_area_to_place_in.",
        examples=[1234, 5678],
    )
    actor_area_radius: int | None = pdt.Field(
        default=None,
        description="Radius in tiles of the actor_area around the placed object. "
        "Actor areas are useful for making certain objects avoid certain positions or areas of the map.",
        examples=[1, 3, 7],
    )
    override_actor_radius_if_required: bool | None = pdt.Field(
        default=None,
        description="Prevents buildings from overlapping when placed in an actor_area with a radius "
        "that is too small to contain them, by expanding the valid placement area outwards.",
        examples=[True],
    )
    actor_area_to_place_in: int | None = pdt.Field(
        default=None,
        description="Place the object within the radius of the actor area with the specified ID.",
        examples=[1234, 5678],
    )
    avoid_actor_area: int | None = pdt.Field(
        default=None,
        description="Objects will avoid the specified actor_area by its radius.",
        examples=[1234, 5678],
    )  # TODO: avoid_actor_area can be repeated multiple times
    avoid_all_actor_areas: bool | None = pdt.Field(
        default=None,
        description="Objects will avoid all actor areas that have been defined so far.",
        examples=[True],
    )

    # Miscellaneous
    enable_tile_shuffling: bool | None = pdt.Field(
        default=None,
        description="Increases randomness of object positions by shuffling the list of candidate tiles rather than just "
        "using the first entry. Useful when using both find_closest and set_circular_placement.",
        examples=[True],
    )
    set_facet: int | None = pdt.Field(
        default=None,
        description="For units, this corresponds to the angle they are facing. For other objects, "
        "this may correspond to alternative appearances.",
        examples=[0, 90, 180, 270],
    )
    match_player_civ: bool | None = pdt.Field(
        default=None,
        description="Makes objects match the architectural style of the player they're assigned to, "
        "rather than using the default style.",
        examples=[True],
    )

    def compile(self):
        # Override to include the object_type parameter in the command name
        result = f"{self._command_name} {self.object_type} {{\n"

        # Skip the object_type parameter when printing attributes
        for attr, val in self.__dict__.items():
            if attr != "_command_name" and attr != "object_type" and val is not None:
                # Handle boolean flags that don't need values
                if isinstance(val, bool) and val and attr.startswith("set_"):
                    result += f"\t{attr}\n"
                elif (
                    isinstance(val, bool)
                    and val
                    and (
                        attr
                        in [
                            "place_on_forest_zone",
                            "find_closest",
                            "find_closest_to_map_center",
                            "find_closest_to_map_edge",
                            "force_placement",
                            "override_actor_radius_if_required",
                            "avoid_all_actor_areas",
                            "enable_tile_shuffling",
                            "match_player_civ",
                            "make_indestructible",
                            "ignore_terrain_restrictions",
                        ]
                    )
                ):
                    result += f"\t{attr}\n"
                else:
                    result += f"\t{attr} {val}\n"

        result += "}\n\n"
        return result


class CreateActorAreaCommand(CommandModel):
    """
    Command to create an actor area according to the RMS specification.
    """

    _command_name: str = "create_actor_area"

    # The four coordinates are part of the command syntax itself
    x1: int
    y1: int
    x2: int
    y2: int

    def compile(self):
        # Override to include the coordinates in the command name
        result = f"{self._command_name} {self.x1} {self.y1} {self.x2} {self.y2}\n\n"
        return result
