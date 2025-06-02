from aoe2rms.generations.base import BaseGenerationModel


class TerrainGeneration(BaseGenerationModel):
    """
    Model for TERRAIN_GENERATION section in RMS scripts.
    """

    _header: str = "<TERRAIN_GENERATION>"

    # Section-level attributes
    color_correction: str | None = None


    def assign_to_map(self):
        self.map.terrain_generation = self