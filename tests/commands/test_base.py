from aoe2rms.commands.base import CommandModel

def test_dummy_command():

    class DummyCommand(CommandModel):
        _command_name = "create_something"
        some_parameter: str

    command = DummyCommand(
        some_parameter="some_value"
    )

    command_script = command.compile()

    print(command_script)
    assert command_script == """create_something {
	some_parameter some_value
}

"""