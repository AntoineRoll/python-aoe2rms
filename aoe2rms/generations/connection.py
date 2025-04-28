import pydantic as pdt

from aoe2rms.generations import BaseGenerationModel


class ConnectionGeneration(BaseGenerationModel):
    """
    Model for CONNECTION_GENERATION section in RMS scripts.

    This section is used to replace terrains with other terrains along paths between
    the origins of lands. It can create roads between players, shallows across rivers,
    and ensure that forests do not completely separate players.

    Note: You can only specify whole systems of connections, not individual connections.
    Connections are processed in order, and if a connection between two locations is
    not possible, that connection will not be produced at all.
    """

    _header: str = "<CONNECTION_GENERATION>"

    accumulate_connections: bool | None = pdt.Field(
        default=None,
        description="DE only: Reverts a DE-specific behavior change where all connections are based on "
        "the terrain prior to connection generation. Using this allows you to replace "
        "terrains created in previous connections.",
        examples=[True],
    )

    commands: list[pdt.BaseModel] = pdt.Field(
        default_factory=list,
        description="List of connection commands that define how lands should be connected.",
    )

    def compile(self):
        print(self._header, end="\n\n")

        if self.accumulate_connections is not None and self.accumulate_connections:
            print("accumulate_connections\n")

        for command in self.commands:
            command.compile()
