from aoe2rms.random import RandomChances
from aoe2rms.conditionals import Variable


def test_random_chances():
    random_chances = RandomChances(
        percent_chances=[
            (50, Variable(name="A")),
            (50, Variable(name="B")),
        ]
    )

    assert (
        random_chances.compile()
        == "start_random\npercent_chance 50\n\t#define A\npercent_chance 50\n\t#define B\nend_random\n"
    )
