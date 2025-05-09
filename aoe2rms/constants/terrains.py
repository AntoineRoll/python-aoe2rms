from aoe2rms.constants import TerrainConstant


class Grass(TerrainConstant):
    id: int = 0
    name: str = "GRASS"
    description: str = "Grass 1, default terrain"
    __doc__ = description


GRASS = Grass()
# GRASS = TerrainConstant(id=0, name="GRASS", description="Grass 1, default terrain")
WATER = TerrainConstant(id=1, name="WATER", description="Water, Shallow, normal water")
BEACH = TerrainConstant(
    id=2,
    name="BEACH",
    description="Beach, automatically placed when land terrains border water",
)
DIRT3 = TerrainConstant(id=3, name="DIRT3", description="Dirt 3, grassy")
SHALLOW = TerrainConstant(
    id=4, name="SHALLOW", description="Shallows, can be used to create river crossings"
)
LEAVES = TerrainConstant(
    id=5,
    name="LEAVES",
    description="Underbrush, used as the underlying texture for many forest types",
)
DIRT = TerrainConstant(
    id=6, name="DIRT", description="Dirt 1, brown with the occasional cactus"
)
FARM = TerrainConstant(id=7, name="FARM", description="Farm, no food")
DEAD_FARM = TerrainConstant(id=8, name="DEAD_FARM", description="Farm, Dead, no food")
GRASS3 = TerrainConstant(id=9, name="GRASS3", description="Grass 3, brownish grass")
FOREST = TerrainConstant(
    id=10, name="FOREST", description="Forest, Oak, placed on LEAVES"
)
DIRT2 = TerrainConstant(id=11, name="DIRT2", description="Dirt 2, dirt/grass mixture")
GRASS2 = TerrainConstant(id=12, name="GRASS2", description="Grass 2, very green grass")
PALM_DESERT = TerrainConstant(
    id=13, name="PALM_DESERT", description="Forest, Palm Desert, placed on DESERT"
)
DESERT = TerrainConstant(
    id=14, name="DESERT", description="Desert, Sand, sandy and light colored"
)
WATER_2D_SHORELESS = TerrainConstant(
    id=15,
    name="WATER_2D_SHORELESS",
    description="Water 2D, Shoreless, looks like WATER; no beaches; not dockable",
)
ROCK1 = TerrainConstant(
    id=16,
    name="ROCK1",
    description="Grass, Other, looks like GRASS; automatically placed under cliffs",
)
JUNGLE = TerrainConstant(
    id=17, name="JUNGLE", description="Forest, Jungle, placed on LEAVES"
)
BAMBOO = TerrainConstant(
    id=18, name="BAMBOO", description="Forest, Bamboo, placed on LEAVES"
)
PINE_FOREST = TerrainConstant(
    id=19, name="PINE_FOREST", description="Forest, Pine, placed on LEAVES"
)
OAK_BUSH = TerrainConstant(
    id=20, name="OAK_BUSH", description="Forest, Oak Bush, placed on LEAVES"
)
SNOW_FOREST = TerrainConstant(
    id=21,
    name="SNOW_FOREST",
    description="Forest, Pine Snow, placed on underbrush snow",
)
DEEP_WATER = TerrainConstant(
    id=22, name="DEEP_WATER", description="Water, Deep, not dockable"
)
MED_WATER = TerrainConstant(
    id=23, name="MED_WATER", description="Water, Medium, not dockable"
)
ROAD = TerrainConstant(
    id=24, name="ROAD", description="Road, clean road; cannot place natural resources"
)
ROAD2 = TerrainConstant(
    id=25,
    name="ROAD2",
    description="Road, Broken, road with dirt patches; cannot place natural resources",
)
ICE_NAVIGABLE = TerrainConstant(
    id=26, name="ICE_NAVIGABLE", description="Ice, Navigable, looks like ICE"
)
FOUNDATION = TerrainConstant(
    id=27,
    name="FOUNDATION",
    description="Grass, Foundation, looks like DIRT2; no beaches; still dockable; foundation terrain for buildings",
)
WATER_2D_BRIDGE = TerrainConstant(
    id=28,
    name="WATER_2D_BRIDGE",
    description="Water 2D, Bridge, no beaches; produced by bridge objects; acts as a land terrain",
)
FARM_0_PERCENT = TerrainConstant(
    id=29, name="FARM_0_PERCENT", description="Farm, 0%, no food"
)
FARM_33_PERCENT = TerrainConstant(
    id=30, name="FARM_33_PERCENT", description="Farm, 33%, no food"
)
FARM_67_PERCENT = TerrainConstant(
    id=31, name="FARM_67_PERCENT", description="Farm, 67%, no food"
)
SNOW = TerrainConstant(
    id=32, name="SNOW", description="Snow, icy beach when bordering water"
)
DIRT_SNOW = TerrainConstant(
    id=33,
    name="DIRT_SNOW",
    description="OBSOLETE: Snow Grass, icy beach when bordering water; cannot be layered",
)
GRASS_SNOW = TerrainConstant(
    id=34,
    name="GRASS_SNOW",
    description="OBSOLETE: Snow Dirt, icy beach when bordering water; cannot be layered",
)
ICE = TerrainConstant(
    id=35, name="ICE", description="Ice, cannot place natural resources"
)
SNOW_FOUNDATION = TerrainConstant(
    id=36,
    name="SNOW_FOUNDATION",
    description="Snow, Foundation, looks like SNOW_DIRT; no beaches; still dockable; foundation terrain for buildings on snowy terrains; cannot be layered",
)
ICYSHORE = TerrainConstant(
    id=37,
    name="ICYSHORE",
    description="Beach, Ice, created when snowy terrains border water; looks different from other ice terrains",
)
ROAD_SNOW = TerrainConstant(
    id=38,
    name="ROAD_SNOW",
    description="OBSOLETE: Road, Snow, road with dirt and snow patches; cannot place natural resources; cannot be layered",
)
ROAD_FUNGUS = TerrainConstant(
    id=39,
    name="ROAD_FUNGUS",
    description="OBSOLETE: Road, Fungus, road with dirt and grass patches; cannot place natural resources; cannot be layered",
)
DLC_ROCK = TerrainConstant(
    id=40,
    name="DLC_ROCK",
    description="Rock 1, used for King of the Hill; cannot place natural resources",
)
DLC_SAVANNAH = TerrainConstant(
    id=41, name="DLC_SAVANNAH", description="Dirt, Savannah, light brown"
)
DLC_DIRT4 = TerrainConstant(
    id=42, name="DLC_DIRT4", description="Dirt 4, dirt with some grass"
)
DLC_DRYROAD = TerrainConstant(
    id=43,
    name="DLC_DRYROAD",
    description="OBSOLETE: Road, Desert, road with sand patches; cannot place natural resources; cannot be layered",
)
DLC_MOORLAND = TerrainConstant(
    id=44,
    name="DLC_MOORLAND",
    description="OBSOLETE: Dirt, Mud, mud with some grass; cannot be layered",
)
DLC_CRACKED = TerrainConstant(
    id=45,
    name="DLC_CRACKED",
    description="Desert, Cracked, buildings take 25% more damage",
)
DLC_QUICKSAND = TerrainConstant(
    id=46,
    name="DLC_QUICKSAND",
    description="Desert, Quicksand, cannot place natural resources",
)
DLC_BLACK = TerrainConstant(
    id=47,
    name="DLC_BLACK",
    description="Black, completely black; units have buggy pathfinding when trying to cross",
)
DLC_DRAGONFOREST = TerrainConstant(
    id=48, name="DLC_DRAGONFOREST", description="Forest, Dragon Tree, placed on DIRT"
)
DLC_BAOBABFOREST = TerrainConstant(
    id=49,
    name="DLC_BAOBABFOREST",
    description="Forest, Baobab, 200 wood per tree; 25% tree density; placed on DLC_DIRT4",
)
DLC_ACACIAFOREST = TerrainConstant(
    id=50,
    name="DLC_ACACIAFOREST",
    description="Forest, Acacia, 150 wood per tree; 50% tree density; placed on DLC_SAVANNAH",
)
DLC_BEACH2 = TerrainConstant(
    id=51,
    name="DLC_BEACH2",
    description="Beach, White, Vegatation, alternative beach terrain",
)
DLC_BEACH3 = TerrainConstant(
    id=52, name="DLC_BEACH3", description="Beach, Vegetation, alternative beach terrain"
)
DLC_BEACH4 = TerrainConstant(
    id=53, name="DLC_BEACH4", description="Beach, White, alternative beach terrain"
)
DLC_MANGROVESHALLOW = TerrainConstant(
    id=54,
    name="DLC_MANGROVESHALLOW",
    description="Shallows, Mangrove, light blue with mangrove roots",
)
DLC_MANGROVEFOREST = TerrainConstant(
    id=55,
    name="DLC_MANGROVEFOREST",
    description="Forest, Mangrove, 80% tree density; placed on DLC_MANGROVESHALLOW",
)
DLC_RAINFOREST = TerrainConstant(
    id=56,
    name="DLC_RAINFOREST",
    description="Forest, Rainforest, placed on underbrush jungle",
)
DLC_WATER4 = TerrainConstant(
    id=57,
    name="DLC_WATER4",
    description="Water, Deep Ocean, not dockable; darker than DEEP_WATER",
)
DLC_WATER5 = TerrainConstant(
    id=58, name="DLC_WATER5", description="Water, Azure, brighter than WATER"
)
DLC_NEWSHALLOW = TerrainConstant(
    id=59, name="DLC_NEWSHALLOW", description="Shallows, Azure, bright blue"
)
DLC_JUNGLEGRASS = TerrainConstant(
    id=60, name="DLC_JUNGLEGRASS", description="Grass, Jungle, dark green"
)
DLC_JUNGLEROAD = TerrainConstant(
    id=61,
    name="DLC_JUNGLEROAD",
    description="OBSOLETE: Road, Jungle, road covered in grass; no resource restrictions; cannot be layered",
)
DLC_JUNGLELEAVES = TerrainConstant(
    id=62,
    name="DLC_JUNGLELEAVES",
    description="OBSOLETE: Underbrush, Jungle, jungle grass with leafy patches; cannot be layered",
)
RICE_FARM = TerrainConstant(id=63, name="RICE_FARM", description="Rice Farm, no food")
RICE_FARM_DEAD = TerrainConstant(
    id=64, name="RICE_FARM_DEAD", description="Rice Farm, Dead, no food"
)
RICE_FARM_0_PERCENT = TerrainConstant(
    id=65, name="RICE_FARM_0_PERCENT", description="Rice Farm, 0%, no food"
)
RICE_FARM_33_PERCENT = TerrainConstant(
    id=66, name="RICE_FARM_33_PERCENT", description="Rice Farm, 33%, no food"
)
RICE_FARM_66_PERCENT = TerrainConstant(
    id=67, name="RICE_FARM_66_PERCENT", description="Rice Farm, 66%, no food"
)
UNUSED_68 = TerrainConstant(
    id=68,
    name="UNUSED_68",
    description="Unused Land 68, uses the classic grass texture from AoC",
)
CORRUPTION = TerrainConstant(
    id=69,
    name="CORRUPTION",
    description="Corruption, used for battle royale; visible through fog of war; does not cause damage; makes farms invisible; units have buggy pathfinding when trying to cross",
)
GRAVEL = TerrainConstant(
    id=70, name="GRAVEL", description="Gravel, Default, gray gravel"
)
LEAVES2 = TerrainConstant(
    id=71, name="LEAVES2", description="Underbrush, Leaves, more leafy than LEAVES"
)
SNOW_UNDERBRUSH = TerrainConstant(
    id=72,
    name="SNOW_UNDERBRUSH",
    description="Underbrush, Snow, used for snowy forest terrains",
)
SNOW_LIGHT = TerrainConstant(
    id=73,
    name="SNOW_LIGHT",
    description="Snow, Light, snow that layers weakly with terrain_mask",
)
SNOW_STRONG = TerrainConstant(
    id=74,
    name="SNOW_STRONG",
    description="Snow, Strong, snow that layers strongly with terrain_mask",
)
ROAD_FUNGUS2 = TerrainConstant(
    id=75,
    name="ROAD_FUNGUS2",
    description="Road, Fungus, very mossy road; no resource restrictions",
)
DIRT_MUD = TerrainConstant(id=76, name="DIRT_MUD", description="Dirt, Mud, brown mud")
JUNGLE_UNDERBRUSH = TerrainConstant(
    id=77, name="JUNGLE_UNDERBRUSH", description="Underbrush, Jungle, greenish leaves"
)
ROAD_GRAVEL = TerrainConstant(
    id=78,
    name="ROAD_GRAVEL",
    description="Road, Gravel, road with gravel; no resource restrictions",
)
BEACH_NON_NAVIGABLE = TerrainConstant(
    id=79,
    name="BEACH_NON_NAVIGABLE",
    description="Beach (Non-Navigable), looks like BEACH; acts as a land terrain",
)
BEACH_WET_SAND = TerrainConstant(
    id=80,
    name="BEACH_WET_SAND",
    description="Beach (Non-Navigable), Wet Sand, looks like DLC_WETBEACH; acts as a land terrain",
)
BEACH_WET_GRAVEL = TerrainConstant(
    id=81,
    name="BEACH_WET_GRAVEL",
    description="Beach (Non-Navigable), Wet Gravel, looks like DLC_GRAVELBEACH; acts as a land terrain",
)
BEACH_WET_ROCK = TerrainConstant(
    id=82,
    name="BEACH_WET_ROCK",
    description="Beach (Non-Navigable), Wet Rock, looks like DLC_WETROCKBEACH; acts as a land terrain",
)
GRASS_JUNGLE = TerrainConstant(
    id=83,
    name="GRASS_JUNGLE",
    description="Grass, Jungle (Rainforest), dark green; like DLC_JUNGLEGRASS but with slightly different plant coverage",
)
UNUSED_84 = TerrainConstant(
    id=84, name="UNUSED_84", description="Moddable Land 84, uses placeholder texture"
)
UNUSED_85 = TerrainConstant(
    id=85, name="UNUSED_85", description="Moddable Land 85, uses placeholder texture"
)
UNUSED_86 = TerrainConstant(
    id=86, name="UNUSED_86", description="Moddable Land 86, uses placeholder texture"
)
UNUSED_87 = TerrainConstant(
    id=87, name="UNUSED_87", description="Moddable Land 87, uses placeholder texture"
)
MEDITERRANEAN_FOREST = TerrainConstant(
    id=88,
    name="MEDITERRANEAN_FOREST",
    description="Forest, Mediteranean, mixture of cypress, olive and italian pine trees; placed on LEAVES",
)
FOREST_BUSH = TerrainConstant(
    id=89, name="FOREST_BUSH", description="Forest, Bush, bushes; placed on LEAVES"
)
FOREST_REEDS = TerrainConstant(
    id=90,
    name="FOREST_REEDS",
    description="Forest, Reeds (Shallows), 50 wood per tree; placed on SHALLOW; looks like SHALLOW on the minimap",
)
DLC_REEDSBEACH = TerrainConstant(
    id=91,
    name="DLC_REEDSBEACH",
    description="Forest, Reeds (Beach), 50 wood per tree; placed on DLC_WETBEACH",
)
FOREST_REEDS2 = TerrainConstant(
    id=92,
    name="FOREST_REEDS2",
    description="Forest, Reeds, 50 wood per tree; placed on LEAVES",
)
UNUSED_93 = TerrainConstant(
    id=93,
    name="UNUSED_93",
    description="Moddable Walkable Shallows 93, uses placeholder texture",
)
UNUSED_94 = TerrainConstant(
    id=94,
    name="UNUSED_94",
    description="Moddable Walkable Shallows 94, uses placeholder texture",
)
WATER_GREEN = TerrainConstant(
    id=95, name="WATER_GREEN", description="Water, Green, dockable"
)
WATER_BROWN = TerrainConstant(
    id=96, name="WATER_BROWN", description="Water, Brown, dockable"
)
UNUSED_97 = TerrainConstant(
    id=97,
    name="UNUSED_97",
    description="Moddable Water 97, uses placeholder texture; not dockable",
)
UNUSED_98 = TerrainConstant(
    id=98,
    name="UNUSED_98",
    description="Moddable Water 98, uses placeholder texture; not dockable",
)
UNUSED_99 = TerrainConstant(
    id=99,
    name="UNUSED_99",
    description="Moddable Deep Water 99, uses placeholder texture; not dockable",
)
DLC_DRYGRASS = TerrainConstant(
    id=100, name="DLC_DRYGRASS", description="Grass, Dry, brownish grass"
)
DLC_BOGLAND = TerrainConstant(
    id=101,
    name="DLC_BOGLAND",
    description="Swamp, Bogland, blueish grass; cannot place natural resources",
)
DLC_DESERTGRAVEL = TerrainConstant(
    id=102,
    name="DLC_DESERTGRAVEL",
    description="Gravel, Desert, lighter version of gravel",
)
DLC_ROADGRAVEL = TerrainConstant(
    id=103,
    name="DLC_ROADGRAVEL",
    description="OBSOLETE: Road, Gravel, gravel road with dirt patches; no resource restrictions; cannot be layered",
)
DLC_FORESTAUTUMN = TerrainConstant(
    id=104, name="DLC_FORESTAUTUMN", description="Forest, Autumn, placed on LEAVES"
)
DLC_FORESTSNOWAUTUMN = TerrainConstant(
    id=105,
    name="DLC_FORESTSNOWAUTUMN",
    description="Forest, Autumn Snow, snowy version of DLC_FORESTAUTUMN; placed on underbrush snow",
)
DLC_FORESTDEAD = TerrainConstant(
    id=106,
    name="DLC_FORESTDEAD",
    description="Forest, Dead, snowy bushes and dead trees; placed on underbrush snow",
)
DLC_WETBEACH = TerrainConstant(
    id=107, name="DLC_WETBEACH", description="Beach, Wet, alternative beach terrain"
)
DLC_GRAVELBEACH = TerrainConstant(
    id=108,
    name="DLC_GRAVELBEACH",
    description="Beach, Wet Gravel, alternative beach terrain",
)
DLC_WETROCKBEACH = TerrainConstant(
    id=109,
    name="DLC_WETROCKBEACH",
    description="Beach, Wet Rock, alternative beach terrain",
)
BIRCH_FOREST = TerrainConstant(
    id=110, name="BIRCH_FOREST", description="Forest, Birch, placed on LEAVES"
)
MUDDY_SHALLOW = TerrainConstant(
    id=111, name="MUDDY_SHALLOW", description="Swamp, Shallows, acts like SHALLOW"
)
PALM_GRASS_FOREST = TerrainConstant(
    id=112,
    name="PALM_GRASS_FOREST",
    description="Forest, Palm Grass, like PALM_DESERT, but placed on GRASS2",
)
LUSH_BAMBOO_FOREST = TerrainConstant(
    id=113,
    name="LUSH_BAMBOO_FOREST",
    description="Forest, Lush Bamboo, placed on underbrush jungle",
)
YELLOW_SHALLOW_WATER = TerrainConstant(
    id=114, name="YELLOW_SHALLOW_WATER", description="Water, Yellow (Shallow), dockable"
)
YELLOW_SHALLOW = TerrainConstant(
    id=115, name="YELLOW_SHALLOW", description="Shallows, Yellow, acts like SHALLOW"
)
YELLOW_DEEP_WATER = TerrainConstant(
    id=116, name="YELLOW_DEEP_WATER", description="Water, Yellow (Deep), not dockable"
)
PASTURE = TerrainConstant(id=117, name="PASTURE", description="Pasture, no food")
PASTURE_DEAD = TerrainConstant(
    id=118, name="PASTURE_DEAD", description="Pasture, Dead, no food"
)
PASTURE_0_PERCENT = TerrainConstant(
    id=119, name="PASTURE_0_PERCENT", description="Pasture, 0%, no food"
)
PASTURE_33_PERCENT = TerrainConstant(
    id=120, name="PASTURE_33_PERCENT", description="Pasture, 33%, no food"
)
PASTURE_66_PERCENT = TerrainConstant(
    id=121, name="PASTURE_66_PERCENT", description="Pasture, 66%, no food"
)
UNDEFINED_122 = TerrainConstant(id=122, name="UNDEFINED_122", description="Unused 122")
UNDEFINED_123 = TerrainConstant(id=123, name="UNDEFINED_123", description="Unused 123")
UNDEFINED_124 = TerrainConstant(id=124, name="UNDEFINED_124", description="Unused 124")
UNDEFINED_125 = TerrainConstant(id=125, name="UNDEFINED_125", description="Unused 125")
UNDEFINED_126 = TerrainConstant(id=126, name="UNDEFINED_126", description="Unused 126")
UNDEFINED_127 = TerrainConstant(id=127, name="UNDEFINED_127", description="Unused 127")
UNDEFINED_128 = TerrainConstant(id=128, name="UNDEFINED_128", description="Unused 128")
UNDEFINED_129 = TerrainConstant(id=129, name="UNDEFINED_129", description="Unused 129")
UNDEFINED_130 = TerrainConstant(id=130, name="UNDEFINED_130", description="Unused 130")
UNDEFINED_131 = TerrainConstant(id=131, name="UNDEFINED_131", description="Unused 131")
UNDEFINED_132 = TerrainConstant(id=132, name="UNDEFINED_132", description="Unused 132")
UNDEFINED_133 = TerrainConstant(id=133, name="UNDEFINED_133", description="Unused 133")
UNDEFINED_134 = TerrainConstant(id=134, name="UNDEFINED_134", description="Unused 134")
UNDEFINED_135 = TerrainConstant(id=135, name="UNDEFINED_135", description="Unused 135")
UNDEFINED_136 = TerrainConstant(id=136, name="UNDEFINED_136", description="Unused 136")
UNDEFINED_137 = TerrainConstant(id=137, name="UNDEFINED_137", description="Unused 137")
UNDEFINED_138 = TerrainConstant(id=138, name="UNDEFINED_138", description="Unused 138")
UNDEFINED_139 = TerrainConstant(id=139, name="UNDEFINED_139", description="Unused 139")
UNDEFINED_140 = TerrainConstant(id=140, name="UNDEFINED_140", description="Unused 140")
UNDEFINED_141 = TerrainConstant(id=141, name="UNDEFINED_141", description="Unused 141")
UNDEFINED_142 = TerrainConstant(id=142, name="UNDEFINED_142", description="Unused 142")
UNDEFINED_143 = TerrainConstant(id=143, name="UNDEFINED_143", description="Unused 143")
UNDEFINED_144 = TerrainConstant(id=144, name="UNDEFINED_144", description="Unused 144")
UNDEFINED_145 = TerrainConstant(id=145, name="UNDEFINED_145", description="Unused 145")
UNDEFINED_146 = TerrainConstant(id=146, name="UNDEFINED_146", description="Unused 146")
UNDEFINED_147 = TerrainConstant(id=147, name="UNDEFINED_147", description="Unused 147")
UNDEFINED_148 = TerrainConstant(id=148, name="UNDEFINED_148", description="Unused 148")
UNDEFINED_149 = TerrainConstant(id=149, name="UNDEFINED_149", description="Unused 149")
UNDEFINED_150 = TerrainConstant(id=150, name="UNDEFINED_150", description="Unused 150")
UNDEFINED_151 = TerrainConstant(id=151, name="UNDEFINED_151", description="Unused 151")
UNDEFINED_152 = TerrainConstant(id=152, name="UNDEFINED_152", description="Unused 152")
UNDEFINED_153 = TerrainConstant(id=153, name="UNDEFINED_153", description="Unused 153")
UNDEFINED_154 = TerrainConstant(id=154, name="UNDEFINED_154", description="Unused 154")
UNDEFINED_155 = TerrainConstant(id=155, name="UNDEFINED_155", description="Unused 155")
UNDEFINED_156 = TerrainConstant(id=156, name="UNDEFINED_156", description="Unused 156")
UNDEFINED_157 = TerrainConstant(id=157, name="UNDEFINED_157", description="Unused 157")
UNDEFINED_158 = TerrainConstant(id=158, name="UNDEFINED_158", description="Unused 158")
UNDEFINED_159 = TerrainConstant(id=159, name="UNDEFINED_159", description="Unused 159")
UNDEFINED_160 = TerrainConstant(id=160, name="UNDEFINED_160", description="Unused 160")
UNDEFINED_161 = TerrainConstant(id=161, name="UNDEFINED_161", description="Unused 161")
UNDEFINED_162 = TerrainConstant(id=162, name="UNDEFINED_162", description="Unused 162")
UNDEFINED_163 = TerrainConstant(id=163, name="UNDEFINED_163", description="Unused 163")
UNDEFINED_164 = TerrainConstant(id=164, name="UNDEFINED_164", description="Unused 164")
UNDEFINED_165 = TerrainConstant(id=165, name="UNDEFINED_165", description="Unused 165")
UNDEFINED_166 = TerrainConstant(id=166, name="UNDEFINED_166", description="Unused 166")
UNDEFINED_167 = TerrainConstant(id=167, name="UNDEFINED_167", description="Unused 167")
UNDEFINED_168 = TerrainConstant(id=168, name="UNDEFINED_168", description="Unused 168")
UNDEFINED_169 = TerrainConstant(id=169, name="UNDEFINED_169", description="Unused 169")
UNDEFINED_170 = TerrainConstant(id=170, name="UNDEFINED_170", description="Unused 170")
UNDEFINED_171 = TerrainConstant(id=171, name="UNDEFINED_171", description="Unused 171")
UNDEFINED_172 = TerrainConstant(id=172, name="UNDEFINED_172", description="Unused 172")
UNDEFINED_173 = TerrainConstant(id=173, name="UNDEFINED_173", description="Unused 173")
UNDEFINED_174 = TerrainConstant(id=174, name="UNDEFINED_174", description="Unused 174")
UNDEFINED_175 = TerrainConstant(id=175, name="UNDEFINED_175", description="Unused 175")
UNDEFINED_176 = TerrainConstant(id=176, name="UNDEFINED_176", description="Unused 176")
UNDEFINED_177 = TerrainConstant(id=177, name="UNDEFINED_177", description="Unused 177")
UNDEFINED_178 = TerrainConstant(id=178, name="UNDEFINED_178", description="Unused 178")
UNDEFINED_179 = TerrainConstant(id=179, name="UNDEFINED_179", description="Unused 179")
UNDEFINED_180 = TerrainConstant(id=180, name="UNDEFINED_180", description="Unused 180")
UNDEFINED_181 = TerrainConstant(id=181, name="UNDEFINED_181", description="Unused 181")
UNDEFINED_182 = TerrainConstant(id=182, name="UNDEFINED_182", description="Unused 182")
UNDEFINED_183 = TerrainConstant(id=183, name="UNDEFINED_183", description="Unused 183")
UNDEFINED_184 = TerrainConstant(id=184, name="UNDEFINED_184", description="Unused 184")
UNDEFINED_185 = TerrainConstant(id=185, name="UNDEFINED_185", description="Unused 185")
UNDEFINED_186 = TerrainConstant(id=186, name="UNDEFINED_186", description="Unused 186")
UNDEFINED_187 = TerrainConstant(id=187, name="UNDEFINED_187", description="Unused 187")
UNDEFINED_188 = TerrainConstant(id=188, name="UNDEFINED_188", description="Unused 188")
UNDEFINED_189 = TerrainConstant(id=189, name="UNDEFINED_189", description="Unused 189")
UNDEFINED_190 = TerrainConstant(id=190, name="UNDEFINED_190", description="Unused 190")
UNDEFINED_191 = TerrainConstant(id=191, name="UNDEFINED_191", description="Unused 191")
UNDEFINED_192 = TerrainConstant(id=192, name="UNDEFINED_192", description="Unused 192")
UNDEFINED_193 = TerrainConstant(id=193, name="UNDEFINED_193", description="Unused 193")
UNDEFINED_194 = TerrainConstant(id=194, name="UNDEFINED_194", description="Unused 194")
UNDEFINED_195 = TerrainConstant(id=195, name="UNDEFINED_195", description="Unused 195")
UNDEFINED_196 = TerrainConstant(id=196, name="UNDEFINED_196", description="Unused 196")
UNDEFINED_197 = TerrainConstant(id=197, name="UNDEFINED_197", description="Unused 197")
UNDEFINED_198 = TerrainConstant(id=198, name="UNDEFINED_198", description="Unused 198")
UNDEFINED_199 = TerrainConstant(id=199, name="UNDEFINED_199", description="Unused 199")
