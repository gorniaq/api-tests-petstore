from dataclasses import dataclass


@dataclass
class UsersData:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int
