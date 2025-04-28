import pydantic as pdt
from typing import Literal

from aoe2rms.generations.base import BaseGenerationModel


class CliffGeneration(BaseGenerationModel):
    """
    Model for CLIFF_GENERATION section in RMS scripts.

    Unlike other section models, cliff generation doesn't use create_* commands.
    Instead, it uses section-level attributes to control cliff generation behavior.

    Simply including this section with no parameters will generate default cliffs.
    Do not include this section if you do not want cliffs on your map.
    """

    _header: str = "<CLIFF_GENERATION>"

    # Section-level attributes based on RmsGuide.md
    cliff_type: (
        Literal["CT_GRANITE", "CT_DESERT", "CT_SNOW", "CT_MARBLE", "CT_LIMESTONE"]
        | None
    ) = pdt.Field(
        default=None,
        description="Choose the color of the cliffs to match the theme of your map. (DE only)",
        examples=["CT_DESERT"],
    )
    # Number of cliffs
    min_number_of_cliffs: int | None = pdt.Field(
        default=None,  # default: 3
        description="Minimum number of distinct cliffs to create. Actual number is chosen randomly between min and max.",
        examples=[5],
    )
    max_number_of_cliffs: int | None = pdt.Field(
        default=None,  # default: 8
        description="Maximum number of distinct cliffs to create. Make sure min does not exceed max.",
        examples=[8],
    )

    # Length of cliffs
    min_length_of_cliff: int | None = pdt.Field(
        default=None,
        ge=3,  # minimum must be at least 3 for cliffs to appear
        description="Minimum length of cliffs in cliff segments. Length 3 is 12 tiles, 4 is 15 tiles, etc.",
        examples=[3],
    )
    max_length_of_cliff: int | None = pdt.Field(
        default=None,  # default: 9
        description="Maximum length of cliffs in cliff segments. Make sure min does not exceed max to avoid crashes.",
        examples=[5],
    )

    # Other attributes
    cliff_curliness: int | None = pdt.Field(
        default=None,
        ge=0,
        le=100,  # default: 36
        description="The chance (0-100) that a cliff changes direction at each segment. Low values for straight cliffs, high values for curly cliffs.",
        examples=[50],
    )
    min_distance_cliffs: int | None = pdt.Field(
        default=None,  # default: 2
        description="Minimum distance in cliff units between separate cliffs. 0 is 0 tiles, 1 is 3 tiles, 2 is 6 tiles, etc.",
        examples=[1],
    )
    min_terrain_distance: int | None = pdt.Field(
        default=None,  # default: 2
        description="Minimum distance in cliff units that cliffs will avoid water terrains by. 0 is 0 tiles, 1 is 3 tiles, 2 is 6 tiles, etc.",
        examples=[1],
    )

    def compile(self):
        """
        Override compile method to handle the different structure of cliff generation.
        """
        lines = [self._header]
        for attr, val in self.__dict__.items():
            if attr.startswith("_") or attr == "commands":
                continue
            if val is not None:
                lines.append(f"{attr} {val}")

        return "\n".join(lines)
