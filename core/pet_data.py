from dataclasses import dataclass


@dataclass
class PetData:
    """
    A data class that represents the data associated with a pet.
    """
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str
