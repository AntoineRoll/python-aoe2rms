from aoe2rms.commands.objects import CreateObject
from aoe2rms.conditionals import Attribute, ConditionalAttribute

def generate_standard_relics():
    """
    Generate the standard starting relics for a random map mode game.
    """
    return CreateObject(
        object_type="RELIC",
        max_distance_to_other_zones=2,
        avoid_forest_zone=2,
        min_distance_to_players=25,
        set_circular_placement=True,
        min_distance_group_placement=1,
        number_of_objects=ConditionalAttribute(
            cases=[
                ("TINY_MAP", Attribute(name="number_of_objects", value=5)), 
                ("SMALL_MAP", Attribute(name="number_of_objects", value=5)),
                ("MEDIUM_MAP", Attribute(name="number_of_objects", value=5)),
                ("LARGE_MAP", Attribute(name="number_of_objects", value=7)),
                ("HUGE_MAP", Attribute(name="number_of_objects", value=8)),
            ],
            else_case=Attribute(name="number_of_objects", value=999),
        ),
        temp_min_distance_group_placement=ConditionalAttribute(
            cases=[
                ("TINY_MAP", Attribute(name="temp_min_distance_group_placement", value=35)),
                ("SMALL_MAP", Attribute(name="temp_min_distance_group_placement", value=38)),
                ("MEDIUM_MAP", Attribute(name="temp_min_distance_group_placement", value=38)),
                ("LARGE_MAP", Attribute(name="temp_min_distance_group_placement", value=48)),
                ("HUGE_MAP", Attribute(name="temp_min_distance_group_placement", value=52)),
            ],
            else_case=Attribute(name="temp_min_distance_group_placement", value=52),
        ),
        min_distance_to_map_edge=2
    )
def generate_standard_resources(
    town_center=True,
    villagers=True,
    scout=True,
    forage=True,
    sheep=True,
    boar=True,
    deer=True,
    primary_gold=True,
    secondary_gold=True,
    third_gold=True,
    primary_stone=True,
    secondary_stone=True,
    neutral_gold=True,
    neutral_stone=True,
    relic=True,
):
    """
    Generate the standard starting resources for a random map mode game.

    Args:
        town_center (bool): Whether to include a town center for each player. Defaults to True.
        villagers (bool): Whether to include starting villagers for each player. Defaults to True.
        scout (bool): Whether to include a scout cavalry for each player. Defaults to True.
        forage (bool): Whether to include forage (berries) for each player. Defaults to True.
        sheep (bool): Whether to include sheep for each player. Defaults to True.
        boar (bool): Whether to include boar for each player. Defaults to True.
        deer (bool): Whether to include deer for each player. Defaults to True.
        primary_gold (bool): Whether to include primary gold mine for each player. Defaults to True.
        secondary_gold (bool): Whether to include additional gold for each player. Defaults to True.
        third_gold (bool): Whether to include third gold for each player. Defaults to True.
        primary_stone (bool): Whether to include primary stone for each player. Defaults to True.
        secondary_stone (bool): Whether to include secondary stone for each player. Defaults to True.
        neutral_gold (bool): Whether to include neutral gold in the map. Defaults to True.
        neutral_stone (bool): Whether to include neutral stone in the map. Defaults to True.
        relic (bool): Whether to include relics in the map. Defaults to True.
    """

    standard_resources = []
    
    # Create a Town Center for each player
    if town_center:
        town_center = CreateObject(
            object_type="TOWN_CENTER",
            set_place_for_every_player=True,
            max_distance_to_players=0,
        )
        standard_resources.append(town_center)

    # Create starting villagers
    if villagers:
        villagers = CreateObject(
            object_type="VILLAGER",
            set_place_for_every_player=True,
            min_distance_to_players=6,
            max_distance_to_players=7,
            min_distance_group_placement=2,
        )
        standard_resources.append(villagers)

    # Create a scout cavalry for each player
    if scout:
        scout = CreateObject(
            object_type="SCOUT",
            set_place_for_every_player=True,
            min_distance_to_players=7,
            max_distance_to_players=9,
            min_distance_group_placement=2,
        )
        standard_resources.append(scout)

    # Create forage (berries) for each player
    if forage:
        forage = CreateObject(
            object_type="FORAGE",
            number_of_objects=6,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=9,
            max_distance_to_players=13,
            avoid_forest_zone=4,
            avoid_cliff_zone=3,
            actor_area=14,
            actor_area_radius=4,
            min_distance_group_placement=2,
        )
        standard_resources.append(forage)

    # Create sheep for each player
    if sheep:
        main_sheep = CreateObject(
            object_type="SHEEP",
            number_of_objects=4,
            set_loose_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=7,
            max_distance_to_players=10,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
        )
        additional_sheep = CreateObject(
            object_type="SHEEP",
            number_of_objects=2,
            number_of_groups=2,
            set_loose_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=16,
            max_distance_to_players=20,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            max_distance_to_other_zones=2,
            min_distance_group_placement=3,
            temp_min_distance_group_placement=3,
        )
        standard_resources.append(main_sheep)
        standard_resources.append(additional_sheep)

    # Create boar for each player
    if boar:
        boar = CreateObject(
            object_type="BOAR",
            number_of_groups=2,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=16,
            max_distance_to_players=19,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            max_distance_to_other_zones=2,
            min_distance_group_placement=1,
        )
        standard_resources.append(boar)

    # Create deer for each player
    if deer:
        deer = CreateObject(
            object_type="DEER",
            number_of_objects=3,
            group_placement_radius=3,
            set_loose_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=16,
            max_distance_to_players=20,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            max_distance_to_other_zones=2,
            min_distance_group_placement=2,
            actor_area=776,
            actor_area_radius=3,
        )
        standard_resources.append(deer)

    # Create primary gold mine for each player
    if primary_gold:
        primary_gold = CreateObject(
            object_type="GOLD",
            number_of_objects=7,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=12,
            max_distance_to_players=16,
            max_distance_to_other_zones=7,
            avoid_cliff_zone=3,
            actor_area=12,
            actor_area_radius=5,
            avoid_actor_area=14,  # berries
            avoid_forest_zone=2,
            min_distance_group_placement=2,
        )
        standard_resources.append(primary_gold)

    # Create additional gold and stone for each player
    if secondary_gold:
        secondary_gold = CreateObject(
            object_type="GOLD",
            number_of_objects=4,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=17,
            max_distance_to_players=22,
            max_distance_to_other_zones=7,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            actor_area=61,
            actor_area_radius=5,
            min_distance_group_placement=3,
            # avoid_actor_area=14,  # berries
            avoid_actor_area=12,  # close gold
        )
        standard_resources.append(secondary_gold)

    if third_gold:
        third_gold = CreateObject(
            object_type="GOLD",
            number_of_objects=4,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=23,
            max_distance_to_players=27,
            min_distance_group_placement=3,
            max_distance_to_other_zones=7,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            actor_area=62,
            actor_area_radius=5,
            avoid_actor_area=61,  # medium gold
            # avoid_actor_area=14,  # berries
            # avoid_actor_area=12,  # close gold
        )
        standard_resources.append(third_gold)

    if primary_stone:
        primary_stone = CreateObject(
            object_type="STONE",
            number_of_objects=5,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=13,
            max_distance_to_players=18,
            min_distance_group_placement=3,
            max_distance_to_other_zones=7,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            actor_area=63,
            actor_area_radius=5,
            avoid_actor_area=61,  # medium gold
            # avoid_actor_area=62,  # far gold
            # avoid_actor_area=14,  # berries
            # avoid_actor_area=12,  # close gold
        )
        standard_resources.append(primary_stone)

    if secondary_stone:
        secondary_stone = CreateObject(
            object_type="STONE",
            number_of_objects=4,
            group_placement_radius=3,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            set_place_for_every_player=True,
            min_distance_to_players=20,
            max_distance_to_players=24,
            min_distance_group_placement=3,
            max_distance_to_other_zones=7,
            avoid_forest_zone=2,
            avoid_cliff_zone=3,
            actor_area=65,
            actor_area_radius=5,
            avoid_actor_area=61,  # medium gold
            # avoid_actor_area=62,  # far gold
            # avoid_actor_area=63,  # close stone
            # avoid_actor_area=14,  # berries
            # avoid_actor_area=12,  # close gold
        )
        standard_resources.append(secondary_stone)

    # Create additional gold and stone in the map
    if neutral_gold:
        neutral_gold = CreateObject(
            object_type="GOLD",
            number_of_objects=3,
            number_of_groups=3,
            group_placement_radius=2,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            min_distance_to_players=40,
            avoid_forest_zone=3,
            avoid_cliff_zone=4,
            actor_area=66,
            actor_area_radius=5,
            min_distance_group_placement=4,
        )
        standard_resources.append(neutral_gold)

    if neutral_stone:
        neutral_stone = CreateObject(
            object_type="STONE",
            number_of_objects=3,
            number_of_groups=3,
            group_placement_radius=2,
            set_tight_grouping=True,
            set_gaia_object_only=True,
            min_distance_to_players=40,
            avoid_forest_zone=3,
            avoid_cliff_zone=4,
            actor_area=67,
            actor_area_radius=5,
        )
        standard_resources.append(neutral_stone)

    # Create Relic
    if relic:
        relic = generate_standard_relics()
        standard_resources.append(relic)

    # TODO: straggler tree (home & shared), shore fish, other fish, hawk, wolf

    return standard_resources
