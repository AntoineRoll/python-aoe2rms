import pydantic as pdt

from aoe2rms.commands import CommandModel


class ConnectionCommandBase(CommandModel):
    """
    Base class for connection commands according to the RMS specification.

    Connection commands replace terrains with other terrains along paths between land origins.
    They can create roads, shallows, or ensure passable paths through forests.
    """

    default_terrain_replacement: str | None = pdt.Field(
        default=None,
        description="Terrain type used to replace any terrain type that is not explicitly specified. "
        "Used when a connection passes through terrain that doesn't match any replace_terrain entry.",
        examples=["DIRT", "ROAD", "SHALLOW"],
    )
    replace_terrain: tuple[str, str] | None = pdt.Field(
        default=None,
        description="Replace the first terrain with the second terrain when making connections. "
        "Multiple replace_terrain commands can be used to handle different terrain types.",
        examples=[("FOREST", "GRASS"), ("WATER", "SHALLOW")],
    )
    terrain_cost: tuple[str, int] | None = pdt.Field(
        default=None,
        description="Cost of crossing the specified terrain when calculating path. "
        "Higher values make the pathfinding algorithm avoid this terrain.",
        examples=[("WATER", 15), ("FOREST", 7)],
    )
    terrain_size: tuple[str, int, int] | None = pdt.Field(
        default=None,
        description="Width and variability of the connection when it crosses the specified terrain. "
        "First number is width, second is variability (0 for straight paths).",
        examples=[("FOREST", 10, 0), ("GRASS", 1, 1)],
    )

    def compile(self):
        print(f"{self._command_name}", end=" {\n")

        for attr, val in self.__dict__.items():
            if attr != "_command_name" and val is not None:
                if attr == "replace_terrain" and val is not None:
                    print(f"\t{attr} {val[0]} {val[1]}")
                elif attr == "terrain_cost" and val is not None:
                    print(f"\t{attr} {val[0]} {val[1]}")
                elif attr == "terrain_size" and val is not None:
                    print(f"\t{attr} {val[0]} {val[1]} {val[2]}")
                else:
                    print(f"\t{attr} {val}")

        print("}\n")


class ConnectAllPlayersLand(ConnectionCommandBase):
    """
    Command to connect all players' lands.

    Creates paths between the origins of all player lands and all lands assigned to players.
    Connections may pass through neutral lands if the cost is favorable.
    """

    _command_name: str = "create_connect_all_players_land"


class ConnectTeamsLand(ConnectionCommandBase):
    """
    Command to connect lands belonging to the same team.

    Creates paths between lands of players that are on the same team.
    Useful for team games where you want teammates connected but not enemies.
    """

    _command_name: str = "create_connect_teams_lands"


class ConnectAllLands(ConnectionCommandBase):
    """
    Command to connect all lands regardless of ownership.

    Creates paths between all lands on the map, including player lands and neutral lands.
    Useful for ensuring all areas of the map are accessible.
    """

    _command_name: str = "create_connect_all_lands"


class ConnectSameLandZones(ConnectionCommandBase):
    """
    Command to connect lands with the same zone.

    Creates paths between lands that share the same zone value.
    Useful when you've manually set up land zones and want specific connectivity.
    """

    _command_name: str = "create_connect_same_land_zones"


class ConnectToNonplayerLand(ConnectionCommandBase):
    """
    Command to connect to non-player lands.

    Creates paths between player lands and neutral lands.
    Useful when you have important resources or objectives on neutral lands.
    """

    _command_name: str = "create_connect_to_nonplayer_land"
