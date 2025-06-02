from aoe2rms.constants import TerrainConstant


class DefaultTerrain(TerrainConstant):
    _is_default = True


GRASS = DefaultTerrain(
    id=0,
    name="GRASS",
    description="Grass 1 (default terrain)",
)
WATER = DefaultTerrain(
    id=1,
    name="WATER",
    description="Water, Shallow (normal water)",
)
BEACH = DefaultTerrain(
    id=2,
    name="BEACH",
    description="Beach (automatically placed when land terrains border water)",
)
DIRT3 = DefaultTerrain(
    id=3,
    name="DIRT3",
    description="Dirt 3 (grassy)",
)
SHALLOW = DefaultTerrain(
    id=4,
    name="SHALLOW",
    description="Shallows (can be used to create river crossings)",
)
LEAVES = DefaultTerrain(
    id=5,
    name="LEAVES",
    description="Underbrush (used as the underlying texture for many forest types)",
)
DIRT = DefaultTerrain(
    id=6,
    name="DIRT",
    description="Dirt 1 (brown with the occasional cactus)",
)
GRASS3 = DefaultTerrain(
    id=9,
    name="GRASS3",
    description="Grass 3 (brownish grass)",
)
FOREST = DefaultTerrain(
    id=10,
    name="FOREST",
    description="Forest, Oak (placed on LEAVES)",
)
DIRT2 = DefaultTerrain(
    id=11,
    name="DIRT2",
    description="Dirt 2 (dirt/grass mixture)",
)
GRASS2 = DefaultTerrain(
    id=12,
    name="GRASS2",
    description="Grass 2 (very green grass)",
)
PALM_DESERT = DefaultTerrain(
    id=13,
    name="PALM_DESERT",
    description="Forest, Palm Desert (placed on DESERT)",
)
DESERT = DefaultTerrain(
    id=14,
    name="DESERT",
    description="Desert, Sand (sandy and light colored)",
)
ROCK1 = DefaultTerrain(
    id=16,
    name="ROCK1",
    description="Grass, Other (looks like GRASS; automatically placed under cliffs)",
)
JUNGLE = DefaultTerrain(
    id=17,
    name="JUNGLE",
    description="Forest, Jungle (placed on LEAVES)",
)
BAMBOO = DefaultTerrain(
    id=18,
    name="BAMBOO",
    description="Forest, Bamboo (placed on LEAVES)",
)
PINE_FOREST = DefaultTerrain(
    id=19,
    name="PINE_FOREST",
    description="Forest, Pine (placed on LEAVES)",
)
SNOW_FOREST = DefaultTerrain(
    id=21,
    name="SNOW_FOREST",
    description="Forest, Pine Snow (placed on underbrush snow)",
)
DEEP_WATER = DefaultTerrain(
    id=22,
    name="DEEP_WATER",
    description="Water, Deep (not dockable)",
)
MED_WATER = DefaultTerrain(
    id=23,
    name="MED_WATER",
    description="Water, Medium (not dockable)",
)
ROAD = DefaultTerrain(
    id=24,
    name="ROAD",
    description="Road (clean road; cannot place natural resources)",
)
ROAD2 = DefaultTerrain(
    id=25,
    name="ROAD2",
    description="Road, Broken (road with dirt patches; cannot place natural resources)",
)
SNOW = DefaultTerrain(
    id=32,
    name="SNOW",
    description="Snow (icy beach when bordering water)",
)
DIRT_SNOW = DefaultTerrain(
    id=33,
    name="DIRT_SNOW",
    description="OBSOLETE: Snow Grass (icy beach when bordering water; cannot be layered)",
)
GRASS_SNOW = DefaultTerrain(
    id=34,
    name="GRASS_SNOW",
    description="OBSOLETE: Snow Dirt (icy beach when bordering water; cannot be layered)",
)
ICE = DefaultTerrain(
    id=35,
    name="ICE",
    description="Ice (cannot place natural resources)",
)
ICYSHORE = DefaultTerrain(
    id=37,
    name=" ICYSHORE",
    description="Beach, Ice (created when snowy terrains border water; looks different from other ice terrains)",
)
DLC_ROCK = DefaultTerrain(
    id=40,
    name="DLC_ROCK",
    description="Rock 1 (used for King of the Hill; cannot place natural resources)",
)
DLC_SAVANNAH = DefaultTerrain(
    id=41,
    name="DLC_SAVANNAH",
    description="Dirt, Savannah (light brown)",
)
DLC_DIRT4 = DefaultTerrain(
    id=42,
    name="DLC_DIRT4",
    description="Dirt 4 (dirt with some grass)",
)
DLC_DRYROAD = DefaultTerrain(
    id=43,
    name="DLC_DRYROAD",
    description="OBSOLETE: Road, Desert (road with sand patches; cannot place natural resources; cannot be layered)",
)
DLC_MOORLAND = DefaultTerrain(
    id=44,
    name="DLC_MOORLAND",
    description="OBSOLETE: Dirt, Mud (mud with some grass; cannot be layered)",
)
DLC_CRACKED = DefaultTerrain(
    id=45,
    name="DLC_CRACKED",
    description="Desert, Cracked (buildings take 25% more damage)",
)
DLC_QUICKSAND = DefaultTerrain(
    id=46,
    name="DLC_QUICKSAND",
    description="Desert, Quicksand (cannot place natural resources)",
)
DLC_BLACK = DefaultTerrain(
    id=47,
    name="DLC_BLACK",
    description="Black (completely black; units have buggy pathfinding when trying to cross)",
)
DLC_DRAGONFOREST = DefaultTerrain(
    id=48,
    name="DLC_DRAGONFOREST",
    description="Forest, Dragon Tree (placed on DIRT)",
)
DLC_BAOBABFOREST = DefaultTerrain(
    id=49,
    name="DLC_BAOBABFOREST",
    description="Forest, Baobab (200 wood per tree; 25% tree density; placed on DLC_DIRT4)",
)
DLC_ACACIAFOREST = DefaultTerrain(
    id=50,
    name="DLC_ACACIAFOREST",
    description="Forest, Acacia (150 wood per tree; 50% tree density; placed on DLC_SAVANNAH)",
)
DLC_BEACH2 = DefaultTerrain(
    id=51,
    name="DLC_BEACH2",
    description="Beach, White, Vegatation (alternative beach terrain)",
)
DLC_BEACH3 = DefaultTerrain(
    id=52,
    name="DLC_BEACH3",
    description="Beach, Vegetation (alternative beach terrain)",
)
DLC_BEACH4 = DefaultTerrain(
    id=53,
    name="DLC_BEACH4",
    description="Beach, White (alternative beach terrain)",
)
DLC_MANGROVESHALLOW = DefaultTerrain(
    id=54,
    name="DLC_MANGROVESHALLOW",
    description="Shallows, Mangrove (light blue with mangrove roots)",
)
DLC_MANGROVEFOREST = DefaultTerrain(
    id=55,
    name="DLC_MANGROVEFOREST",
    description="Forest, Mangrove (80% tree density; placed on DLC_MANGROVESHALLOW)",
)
DLC_RAINFOREST = DefaultTerrain(
    id=56,
    name="DLC_RAINFOREST",
    description="Forest, Rainforest (placed on underbrush jungle)",
)
DLC_WATER4 = DefaultTerrain(
    id=57,
    name="DLC_WATER4",
    description="Water, Deep Ocean (not dockable; darker than DEEP_WATER)",
)
DLC_WATER5 = DefaultTerrain(
    id=58,
    name="DLC_WATER5",
    description="Water, Azure (brighter than WATER)",
)
DLC_NEWSHALLOW = DefaultTerrain(
    id=59,
    name="DLC_NEWSHALLOW",
    description="Shallows, Azure (bright blue)",
)
DLC_JUNGLEGRASS = DefaultTerrain(
    id=60,
    name="DLC_JUNGLEGRASS",
    description="Grass, Jungle (dark green)",
)
DLC_JUNGLEROAD = DefaultTerrain(
    id=61,
    name="DLC_JUNGLEROAD",
    description="OBSOLETE: Road, Jungle (road covered in grass; no resource restrictions; cannot be layered)",
)
DLC_JUNGLELEAVES = DefaultTerrain(
    id=62,
    name="DLC_JUNGLELEAVES",
    description="OBSOLETE: Underbrush, Jungle (jungle grass with leafy patches; cannot be layered)",
)
MEDITERRANEAN_FOREST = DefaultTerrain(
    id=88,
    name="MEDITERRANEAN_FOREST",
    description="Forest, Mediteranean (mixture of cypress, olive and italian pine trees; placed on LEAVES)",
)
DLC_REEDSBEACH = DefaultTerrain(
    id=91,
    name="DLC_REEDSBEACH",
    description="Forest, Reeds (Beach) (50 wood per tree; placed on DLC_WETBEACH)",
)
DLC_DRYGRASS = DefaultTerrain(
    id=100,
    name="DLC_DRYGRASS",
    description="Grass, Dry (brownish grass)",
)
DLC_BOGLAND = DefaultTerrain(
    id=101,
    name="DLC_BOGLAND",
    description="Swamp, Bogland (blueish grass; cannot place natural resources)",
)
DLC_DESERTGRAVEL = DefaultTerrain(
    id=102,
    name="DLC_DESERTGRAVEL",
    description="Gravel, Desert (lighter version of gravel)",
)
DLC_ROADGRAVEL = DefaultTerrain(
    id=103,
    name="DLC_ROADGRAVEL",
    description="OBSOLETE: Road, Gravel (gravel road with dirt patches; no resource restrictions; cannot be layered)",
)
DLC_FORESTAUTUMN = DefaultTerrain(
    id=104,
    name="DLC_FORESTAUTUMN",
    description="Forest, Autumn (placed on LEAVES)",
)
DLC_FORESTSNOWAUTUMN = DefaultTerrain(
    id=105,
    name="DLC_FORESTSNOWAUTUMN",
    description="Forest, Autumn Snow (snowy version of DLC_FORESTAUTUMN; placed on underbrush snow)",
)
DLC_FORESTDEAD = DefaultTerrain(
    id=106,
    name="DLC_FORESTDEAD",
    description="Forest, Dead (snowy bushes and dead trees; placed on underbrush snow)",
)
DLC_WETBEACH = DefaultTerrain(
    id=107,
    name="DLC_WETBEACH",
    description="Beach, Wet (alternative beach terrain)",
)
DLC_GRAVELBEACH = DefaultTerrain(
    id=108,
    name="DLC_GRAVELBEACH",
    description="Beach, Wet Gravel (alternative beach terrain)",
)
DLC_WETROCKBEACH = DefaultTerrain(
    id=109,
    name="DLC_WETROCKBEACH",
    description="Beach, Wet Rock (alternative beach terrain)",
)
BIRCH_FOREST = DefaultTerrain(
    id=110,
    name="BIRCH_FOREST",
    description="Forest, Birch (placed on LEAVES)",
)
MUDDY_SHALLOW = DefaultTerrain(
    id=111,
    name="MUDDY_SHALLOW",
    description="Swamp, Shallows (acts like SHALLOW)",
)
PALM_GRASS_FOREST = DefaultTerrain(
    id=112,
    name="PALM_GRASS_FOREST",
    description="Forest, Palm Grass (like PALM_DESERT, but placed on GRASS2)",
)
LUSH_BAMBOO_FOREST = DefaultTerrain(
    id=113,
    name="LUSH_BAMBOO_FOREST",
    description="Forest, Lush Bamboo (placed on underbrush jungle)",
)
YELLOW_SHALLOW_WATER = DefaultTerrain(
    id=114,
    name="YELLOW_SHALLOW_WATER",
    description="Water, Yellow (Shallow) (dockable)",
)
YELLOW_SHALLOW = DefaultTerrain(
    id=115,
    name="YELLOW_SHALLOW",
    description="Shallows, Yellow (acts like SHALLOW)",
)
YELLOW_DEEP_WATER = DefaultTerrain(
    id=116,
    name="YELLOW_DEEP_WATER",
    description="Water, Yellow (Deep) (not dockable)",
)
