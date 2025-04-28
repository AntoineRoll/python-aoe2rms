from aoe2rms.commands.elevation import CreateElevation

def test_dummy_command():

    command = CreateElevation(
        height=7,
        base_terrain="GRASS"
    )

    command_script = command.compile()

    print(command_script)
    assert command_script == """create_elevation 7 {
	base_terrain GRASS
}

"""