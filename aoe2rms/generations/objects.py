from aoe2rms.generations.base import BaseGenerationModel


class ObjectsGeneration(BaseGenerationModel):
    """
    Model for OBJECTS_GENERATION section in RMS scripts.
    """

    _header: str = "<OBJECTS_GENERATION>"
