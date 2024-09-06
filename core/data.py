from dataclasses import dataclass


@dataclass
class UsersData:
    """
    A data class that represents a user's information.
    """
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


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
