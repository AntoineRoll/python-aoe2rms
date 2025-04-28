from aoe2rms.map import Map


def test_empty_map():
    map = Map(name="test_map")
    map_script = map.compile()

    assert (
        map_script
        == """/* test_map */


<PLAYER_SETUP>

random_placement

<LAND_GENERATION>

base_terrain GRASS"""
    )


def test_metadata_map():
    map = Map(
        name="Test Map with Metadata",
        author="pytest",
        description="An empty map to test generation of Metadata",
    )
    map_script = map.compile()

    assert (
        map_script
        == """/* Test Map with Metadata */
/* Author: pytest */
/* An empty map to test generation of Metadata */


<PLAYER_SETUP>

random_placement

<LAND_GENERATION>

base_terrain GRASS"""
    )
