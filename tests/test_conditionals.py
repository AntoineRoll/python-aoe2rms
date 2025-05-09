from aoe2rms.conditional import ConditionalConstant, Variable
from aoe2rms.constants import TerrainConstant

def test_variable():
    
    var = Variable(name="TEST_VAR")
    assert var.compile() == "#define TEST_VAR\n"
    
def test_variable_with_prefix():
    var = Variable(name="TEST_VAR")
    assert var.compile(prefix="\t") == "\t#define TEST_VAR\n"
    

def test_minimal_condition():
    
    conditional_script = ConditionalConstant(
        first_condition="TINY_MAP",
        first_output=TerrainConstant(id=3, name="TEST_TERRAIN")
    )
    
    assert conditional_script.compile() == "if TINY_MAP\n\t#const TEST_TERRAIN 3 /* Dirt 3 */\nendif\n"
    
def test_additional_conditions():
    
    conditional_script = ConditionalConstant(
        first_condition="TINY_MAP",
        first_output=TerrainConstant(id=3, name="TEST_TERRAIN"),
        additional_conditions=[
            ("SMALL_MAP", TerrainConstant(id=4, name="TEST_TERRAIN")),
            ("MEDIUM_MAP", TerrainConstant(id=5, name="TEST_TERRAIN")),
            ("LARGE_MAP", TerrainConstant(id=6, name="TEST_TERRAIN")),
            ("HUGE_MAP", TerrainConstant(id=7, name="TEST_TERRAIN")),
            ("GIGANTIC_MAP", TerrainConstant(id=8, name="TEST_TERRAIN")),
            ("LUDIKRIS_MAP", TerrainConstant(id=9, name="TEST_TERRAIN"))
        ]
    )
    
    assert conditional_script.compile() == """if TINY_MAP
	#const TEST_TERRAIN 3 /* Dirt 3 */
elseif SMALL_MAP
	#const TEST_TERRAIN 4 /* Shallows */
elseif MEDIUM_MAP
	#const TEST_TERRAIN 5 /* Underbrush */
elseif LARGE_MAP
	#const TEST_TERRAIN 6 /* Dirt 1 */
elseif HUGE_MAP
	#const TEST_TERRAIN 7 /* Farm */
elseif GIGANTIC_MAP
	#const TEST_TERRAIN 8 /* Farm, Dead */
elseif LUDIKRIS_MAP
	#const TEST_TERRAIN 9 /* Grass 3 */
endif
"""


def test_else_conditions():
    
    conditional_script = ConditionalConstant(
        first_condition="TINY_MAP",
        first_output=TerrainConstant(id=3, name="TEST_TERRAIN"),
        else_output= TerrainConstant(id=4, name="TEST_TERRAIN")
    )
    
    assert conditional_script.compile() == """if TINY_MAP
	#const TEST_TERRAIN 3 /* Dirt 3 */
else
	#const TEST_TERRAIN 4 /* Shallows */
endif
"""
    
def test_full_conditions():
    
    conditional_script = ConditionalConstant(
        first_condition="TINY_MAP",
        first_output=TerrainConstant(id=3, name="TEST_TERRAIN"),
        additional_conditions=[
            ("SMALL_MAP", TerrainConstant(id=4, name="TEST_TERRAIN")),
            ("MEDIUM_MAP", TerrainConstant(id=5, name="TEST_TERRAIN")),
            ("LARGE_MAP", TerrainConstant(id=6, name="TEST_TERRAIN")),
            ("HUGE_MAP", TerrainConstant(id=7, name="TEST_TERRAIN")),
            ("GIGANTIC_MAP", TerrainConstant(id=8, name="TEST_TERRAIN")),
            ("LUDIKRIS_MAP", TerrainConstant(id=9, name="TEST_TERRAIN"))
        ],
        else_output=TerrainConstant(id=10, name="OTHER_TERRAIN")
    )
    
    assert conditional_script.compile() == """if TINY_MAP
	#const TEST_TERRAIN 3 /* Dirt 3 */
elseif SMALL_MAP
	#const TEST_TERRAIN 4 /* Shallows */
elseif MEDIUM_MAP
	#const TEST_TERRAIN 5 /* Underbrush */
elseif LARGE_MAP
	#const TEST_TERRAIN 6 /* Dirt 1 */
elseif HUGE_MAP
	#const TEST_TERRAIN 7 /* Farm */
elseif GIGANTIC_MAP
	#const TEST_TERRAIN 8 /* Farm, Dead */
elseif LUDIKRIS_MAP
	#const TEST_TERRAIN 9 /* Grass 3 */
else
	#const OTHER_TERRAIN 10 /* Forest, Oak */
endif
"""

def test_several_outputs():
    conditional_script = ConditionalConstant(
        first_condition="TINY_MAP",
        first_output=[
            TerrainConstant(id=6, name="TEST_TERRAIN"),
            TerrainConstant(id=7, name="SECOND_TERRAIN")
        ],
        else_output=[
            TerrainConstant(id=4, name="TEST_TERRAIN"),
            TerrainConstant(id=5, name="SECOND_TERRAIN"),
        ]
    )
    
    assert conditional_script.compile() == """if TINY_MAP
	#const TEST_TERRAIN 6 /* Dirt 1 */
	#const SECOND_TERRAIN 7 /* Farm */
else
	#const TEST_TERRAIN 4 /* Shallows */
	#const SECOND_TERRAIN 5 /* Underbrush */
endif
"""
