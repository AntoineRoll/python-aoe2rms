from aoe2rms.commands.objects import CreateObject


def generate_standard_resources():
    """
    Generate the standard starting resources for a random map mode game.
    """

    # Create a Town Center for each player
    town_center = CreateObject(
        object_type="TOWN_CENTER",
        set_place_for_every_player=True,
        max_distance_to_players=0,
    )

    # Create starting villagers
    villagers = CreateObject(
        object_type="VILLAGER",
        set_place_for_every_player=True,
        min_distance_to_players=6,
        max_distance_to_players=7,
        min_distance_group_placement=2,
    )

    # Create a scout cavalry for each player
    scout = CreateObject(
        object_type="SCOUT",
        set_place_for_every_player=True,
        min_distance_to_players=7,
        max_distance_to_players=9,
        min_distance_group_placement=2,
    )

    # Create forage (berries) for each player
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

    # Create sheep for each player
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

    # Create boar for each player
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

    # Create deer for each player
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

    # Create primary gold mine for each player
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

    # Create additional gold and stone for each player
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

    # Create additional gold and stone in the map
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

    # Create Relic
    relic = CreateObject(
        object_type="RELIC",
        # Only valid for 1v1
        number_of_objects=5,
        min_distance_to_players=25,
        temp_min_distance_group_placement=35,
        avoid_forest_zone=2,
        avoid_cliff_zone=3,
        min_distance_group_placement=1,
    )

    # TODO: straggler tree (home & shared), shore fish, other fish, hawk, wolf

    return [
        town_center,
        villagers,
        scout,
        forage,
        main_sheep,
        additional_sheep,
        boar,
        deer,
        primary_gold,
        secondary_gold,
        third_gold,
        primary_stone,
        secondary_stone,
        neutral_gold,
        neutral_stone,
        relic,
    ]
