# aoe2rms - Pythonic Age of Empires II Random Map Scripts

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`aoe2rms` is a Python package that allows you to write Age of Empires II random map scripts (RMS) using a modern, Pythonic interface based on Pydantic models. It can be thought as a Python SDK for RMS scripting.

**Not affiliated with Microsoft, or any other official developer of Age of Empires franchise.**

## Features

- Create AoE2 random map scripts using Python instead of the traditional RMS syntax
- Strong typing and validation with Pydantic to catch errors before generating scripts
- Intuitive, object-oriented API that closely mirrors the RMS structure
- Well-documented models with descriptions and examples for each attribute
- Easy to extend and customize with your own functionality
- Leverage programmatic features such as loops and modularity to develop your maps

## Installation

### From source
```bash
pip install https://www.github.com/.../
```
### From PyPi
```bash
pip install aoe2rms
```

## Quick Start

```python
from aoe2rms.map import Map
from aoe2rms.generations.land import CreateLand
from aoe2rms.generations.objects import CreateObject

# Create a simple map
my_map = Map(
    name="My First Map",
    author="Your Name",
    description="A map created with aoe2rms"
)

# Add a create_land command to the land_generation section
my_map.land_generation.commands.append(
    CreateLand(
        terrain_type="GRASS",
        land_percent=100
    )
)

# Add player lands
my_map.land_generation.commands.append(
    CreateLand(
        _command_name="create_player_lands",
        terrain_type="DIRT",
        land_percent=20,
        base_size=12,
        other_zone_avoidance_distance=5
    )
)

# Add some gold
if my_map.objects_generation is None:
    from aoe2rms.generations.objects import ObjectsGeneration
    my_map.objects_generation = ObjectsGeneration()

my_map.objects_generation.commands.append(
    CreateObject(
        object_type="GOLD",
        number_of_objects=8,
        group_placement_radius=3,
        set_place_for_every_player=True,
        min_distance_to_players=10,
        max_distance_to_players=20
    )
)

# Generate the RMS script
rms_script = my_map.compile()

# Write it to a file
with open("my_map.rms", "w") as f:
    f.write(rms_script)
```

## Sections

The RMS structure in `aoe2rms` follows the official RMS sections:

1. `player_setup` - Player positioning and global parameters
2. `land_generation` - Main landmasses and terrain
3. `elevation_generation` - Hills and varying heights
4. `cliff_generation` - Impassible cliff formations
5. `terrain_generation` - Detailed terrain features (forests, etc.)
6. `connection_generation` - Paths between players/land areas
7. `objects_generation` - Resources, buildings, units, etc.

## Documentation

For detailed documentation on RMS scripting, refer to Zetnus' [Definitive Random Map Scripting Guide
](https://docs.google.com/document/d/1jnhZXoeL9mkRUJxcGlKnO98fIwFKStP_OBozpr0CHXo/edit?pli=1&tab=t.0)
which contains comprehensive information on Age of Empires II random map scripting. The included `RmsGuide.md` was generated from an extract of the guide in April 2025 and used as context for AI-assisted coding.

## Advanced Usage

You can use Python's context manager to create more complex maps:

```python
from aoe2rms.map import Map
from aoe2rms.generations.land import CreateLand
from aoe2rms.generations.terrain import CreateTerrain
from aoe2rms.generations.objects import CreateObject, ObjectsGeneration
from random import randint

# Create a map
my_map = Map(
    name="Advanced Map Example",
    author="Your Name"
)

# Define base terrain
my_map.land_generation.base_terrain = "WATER"

# Add player islands
with my_map.land_generation:
    CreateLand(
        _command_name="create_player_lands",
        terrain_type="GRASS",
        land_percent=10,
        base_size=10,
        other_zone_avoidance_distance=10,
        zone=1
    )

# Add some neutral islands
for i in range(5):
    with my_map.land_generation:
        CreateLand(
            terrain_type="DIRT",
            land_percent=2,
            base_size=3,
            land_id=i+10
        )

# Add objects generation
my_map.objects_generation = ObjectsGeneration()

# Add starting resources
with my_map.objects_generation:
    CreateObject(
        object_type="TOWN_CENTER",
        set_place_for_every_player=True
    )
    
    CreateObject(
        object_type="VILLAGER",
        number_of_objects=4,
        set_place_for_every_player=True,
        min_distance_to_players=3,
        max_distance_to_players=6
    )

    for resource in ["GOLD", "STONE", "FORAGE_BUSH"]:
        CreateObject(
            object_type=resource,
            number_of_objects=randint(3, 6),
            group_placement_radius=3,
            set_place_for_every_player=True,
            min_distance_to_players=10,
            max_distance_to_players=15
        )
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.