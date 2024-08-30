from dataclasses import dataclass


@dataclass
class PetData:
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str
