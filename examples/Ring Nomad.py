from aoe2rms.map import Map, PlayerSetup
from aoe2rms.generations.land import LandGeneration
from aoe2rms.generations.elevation import ElevationGeneration
from aoe2rms.generations.terrain import TerrainGeneration
from aoe2rms.generations.connection import ConnectionGeneration
from aoe2rms.generations.objects import ObjectsGeneration

from aoe2rms.commands.land import CreateLand, CreatePlayerLand
from aoe2rms.commands.elevation import CreateElevation
from aoe2rms.commands.objects import CreateObject
from aoe2rms.commands.terrain import CreateTerrain
from aoe2rms.commands.connection import ConnectAllPlayersLand
import aoe2rms.constants.terrains as ter

from aoe2rms.presets.resources import generate_standard_relics
from aoe2rms.conditionals import ConditionalScript


# Create a new map
my_map = Map(
    name="W4 - Ring Nomad",
    author="Zetnus",
    description="A map reproducing Ring Nomnd created by Zetnus with python-aoe2rms",
    player_setup=PlayerSetup(
        random_placement=True,
        nomad_resources=True,
        ai_info_map_type=["CUSTOM", 1, 0, 0],
        behavior_version=2,
    ),
    effect_amount=["SET_ATTRIBUTE", "TRANSPORT_SHIP", "ATTR_GARRISON_CAPACITY", "10"],
)

# Still need to define some variables related to map_size

# Define land generation
with LandGeneration(base_terrain=ter.GRASS, map=my_map):
    CreatePlayerLand(
        land_percent=10,
        terrain_type=ter.DLC_WATER5,
        base_size=10,
        circle_radius=(40, 0),
        left_border=5,
        right_border=5,
        top_border=5,
        bottom_border=5,
        other_zone_avoidance_distance=8,
        border_fuzziness=100,
    )

    CreateLand(
        terrain_type=ter.GRASS2,
        land_percent=100,
        land_position=(50, 50),
        left_border=22,
        right_border=22,
        top_border=22,
        bottom_border=22,
        land_id=555,
    )


# Define elevation generation
with ElevationGeneration(map=my_map):
    for _ in range(5):
        CreateElevation(
            height=2,
            base_terrain=ter.GRASS2,
            number_of_tiles=99999,
        )

    CreateElevation(
        height=2,
        base_terrain=ter.GRASS2,
        set_scale_by_size=True,
        number_of_tiles=99999,
        number_of_clumps=9320,
        enable_balanced_elevation=True,
    )

# Define terrain generation
with TerrainGeneration(map=my_map):
    CreateTerrain(
        terrain_type=ter.FOREST,
        base_terrain=ter.GRASS,
        land_percent=7,
        number_of_clumps=14,
        set_scale_by_groups=True,
        spacing_to_other_terrain_types=4,
        comment="forests",
    )

    CreateTerrain(
        terrain_type=ter.FOREST,
        base_terrain=ter.GRASS2,
        land_percent=3,
        number_of_clumps=5,
        set_scale_by_groups=True,
        spacing_to_other_terrain_types=8,
    )

    CreateTerrain(
        terrain_type=ter.DIRT2,
        base_terrain=ter.GRASS,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
        comment="cosmetic terrain mixing",
    )

    CreateTerrain(
        terrain_type=ter.LEAVES, land_percent=8, number_of_clumps=30, terrain_mask=1
    )
    CreateTerrain(
        terrain_type="UNDERBRUSH",
        base_terrain=ter.GRASS,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.DLC_DIRT4,
        base_terrain=ter.GRASS,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.DLC_JUNGLEGRASS,
        base_terrain=ter.GRASS2,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type="UNDERBRUSH",
        base_terrain=ter.GRASS2,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.LEAVES,
        base_terrain=ter.GRASS2,
        land_percent=8,
        number_of_clumps=30,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.WATER,
        base_terrain=ter.DLC_WATER5,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=1,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.WATER,
        base_terrain=ter.DLC_WATER5,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=2,
    )
    CreateTerrain(
        terrain_type=ter.MED_WATER,
        base_terrain=ter.WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=1,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.MED_WATER,
        base_terrain=ter.WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=2,
    )
    CreateTerrain(
        terrain_type=ter.DEEP_WATER,
        base_terrain=ter.MED_WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=1,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.DEEP_WATER,
        base_terrain=ter.MED_WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=2,
    )
    CreateTerrain(
        terrain_type=ter.DLC_WATER4,
        base_terrain=ter.DEEP_WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=1,
        terrain_mask=1,
    )
    CreateTerrain(
        terrain_type=ter.DLC_WATER4,
        base_terrain=ter.DEEP_WATER,
        land_percent=100,
        number_of_clumps=999,
        spacing_to_other_terrain_types=2,
    )


# Define connection generation
with ConnectionGeneration(map=my_map):
    ConnectAllPlayersLand(
        replace_terrain=[
            (ter.GRASS, ter.SHALLOW),
            (ter.BEACH, ter.SHALLOW),
            (ter.FOREST, ter.SHALLOW),
        ],
        terrain_cost=[
            (ter.GRASS, 2),
            (ter.FOREST, 2),
            (ter.DLC_WATER5, 2),
            (ter.WATER, 2),
            (ter.MED_WATER, 2),
            (ter.DEEP_WATER, 2),
            (ter.DLC_WATER4, 2),
            (ter.SHALLOW, 1),
            (ter.BEACH, 15),
            (ter.GRASS2, 15),
        ],
        terrain_size=[(ter.GRASS, 2, 0), (ter.FOREST, 2, 0), (ter.SHALLOW, 2, 0)],
    )

# Define objects generation
with ObjectsGeneration(map=my_map) as objects:
    CreateObject(
        object_type="TRANSPORT_SHIP",
        set_place_for_every_player=True,
        max_distance_to_players=0,
    )

    CreateObject(
        object_type="VILLAGER",
        number_of_objects=9,
        set_place_for_every_player=True,
        min_distance_to_players=1,
        find_closest=True,
        force_placement=True,
        ignore_terrain_restrictions=True,
    )

    objects.commands.append(
        ConditionalScript(
            cases=[
                (
                    "REGICIDE",
                    CreateObject(
                        autoregister=False,
                        comment="test",
                        object_type="KING",
                        ignore_terrain_restrictions=True,
                        set_place_for_every_player=True,
                        min_distance_to_players=1,
                        find_closest=True,
                        force_placement=True,
                    ),
                )
            ]
        )
    )

    generate_standard_relics()

    CreateObject(
        comment="scatter ressources evenly across the map",
        object_type="FORAGE",
        number_of_groups=9999,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=1,
        actor_area_radius=24,
    )

    CreateObject(
        object_type="GOLD",
        number_of_groups=9999,
        number_of_objects=6,
        temp_min_distance_group_placement=22,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=2,
        actor_area_radius=22,
    )
    CreateObject(
        object_type="STONE",
        number_of_groups=9999,
        number_of_objects=4,
        temp_min_distance_group_placement=24,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=3,
        actor_area_radius=24,
    )

    CreateObject(
        object_type="SHEEP",
        number_of_groups=9999,
        number_of_objects=1,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=15,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=4,
        actor_area_radius=15,
    )

    CreateObject(
        object_type="DEER",
        number_of_groups=9999,
        number_of_objects=3,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=20,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=5,
        actor_area_radius=20,
    )

    CreateObject(
        object_type="BOAR",
        number_of_groups=9999,
        number_of_objects=1,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=23,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS2,
        max_distance_to_other_zones=2,
        actor_area=6,
        actor_area_radius=23,
    )

    CreateObject(
        object_type="FORAGE",
        number_of_groups=9999,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        number_of_objects=6,
        temp_min_distance_group_placement=34,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=1,
    )

    CreateObject(
        object_type="GOLD",
        number_of_groups=9999,
        number_of_objects=6,
        temp_min_distance_group_placement=32,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=2,
    )

    CreateObject(
        object_type="STONE",
        number_of_groups=9999,
        number_of_objects=4,
        temp_min_distance_group_placement=34,
        group_placement_radius=2,
        set_tight_grouping=True,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        avoid_forest_zone=3,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=3,
    )

    CreateObject(
        object_type="SHEEP",
        number_of_groups=9999,
        number_of_objects=1,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=20,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=4,
    )

    CreateObject(
        object_type="DEER",
        number_of_groups=9999,
        number_of_objects=3,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=30,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=5,
    )

    CreateObject(
        object_type="BOAR",
        number_of_groups=9999,
        number_of_objects=1,
        set_gaia_object_only=True,
        temp_min_distance_group_placement=33,
        avoid_forest_zone=2,
        terrain_to_place_on=ter.GRASS,
        max_distance_to_other_zones=2,
        min_distance_to_map_edge=2,
        avoid_actor_area=6,
    )

    CreateObject(
        comment="fish",
        object_type="SHORE_FISH",
        number_of_objects=12,
        set_scaling_to_map_size=True,
        set_gaia_object_only=True,
        min_distance_group_placement=3,
        temp_min_distance_group_placement=7,
        set_place_for_every_player=True,
        find_closest=True,
    )
    CreateObject(
        object_type="MARLIN2",
        number_of_objects=1,
        set_scaling_to_map_size=True,
        terrain_to_place_on=ter.DLC_WATER4,
        set_gaia_object_only=True,
        min_distance_group_placement=4,
        temp_min_distance_group_placement=12,
        max_distance_to_other_zones=7,
        set_place_for_every_player=True,
        find_closest=True,
    )
    CreateObject(
        object_type="SALMON",
        number_of_objects=5,
        set_scaling_to_map_size=True,
        set_gaia_object_only=True,
        max_distance_to_other_zones=4,
        min_distance_group_placement=4,
        temp_min_distance_group_placement=10,
        min_distance_to_players=5,
        set_circular_placement=True,
        set_place_for_every_player=True,
        find_closest=True,
    )
    CreateObject(
        object_type="FISH_PERCH",
        number_of_objects=5,
        set_scaling_to_map_size=True,
        set_gaia_object_only=True,
        max_distance_to_other_zones=4,
        min_distance_group_placement=4,
        temp_min_distance_group_placement=8,
        min_distance_to_players=8,
        set_circular_placement=True,
        set_place_for_every_player=True,
        find_closest=True,
    )
    CreateObject(
        object_type="OAKTREE",
        number_of_groups=30,
        set_scaling_to_map_size=True,
        set_gaia_object_only=True,
        min_distance_group_placement=1,
        avoid_forest_zone=1,
        temp_min_distance_group_placement=4,
    )
    CreateObject(
        comment="birds",
        object_type="HAWK",
        number_of_objects=6,
        set_scaling_to_map_size=True,
    )

if __name__ == "__main__":
    # Generate the RMS script
    rms_script = my_map.compile()

    # Write it to a file
    with open(__file__ + ".rms", "w") as f:
        f.write(rms_script)
