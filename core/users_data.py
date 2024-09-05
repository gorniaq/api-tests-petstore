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

