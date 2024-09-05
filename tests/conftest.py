import random
import string
import pytest

from config import BASE_URL
from core.client import ApiClient
from core.pet_data import PetData
from core.users_data import UsersData


@pytest.fixture(scope="session")
def user_data():
    """
    Fixture to provide random user data for testing purposes.

    This fixture generates a `UsersData` object with random values for fields like
    `id`, `username`, `firstName`, `lastName`, `email`, `password`, `phone`, and `userStatus`.
    The data is used for tests that involve user-related API operations.
    """
    return UsersData(
            id=random.randint(100, 1000),
            username=''.join(random.sample(string.ascii_lowercase, 5)),
            firstName='John',
            lastName='Doe',
            email=f"{''.join(random.sample(string.ascii_lowercase, 5))}@example.com",
            password=''.join(random.sample(string.ascii_letters + string.digits, 8)),
            phone='123-456-7890',
            userStatus=0,
        )


@pytest.fixture(scope="session")
def pet_data():
    """
    Fixture to provide random pet data for testing purposes.

    This fixture generates a `PetData` object with random values for fields like
    `id`, `category`, `name`, `photoUrls`, `tags`, and `status`.
    The data is used for tests that involve pet-related API operations.
    """
    return PetData(
        id=random.randint(1000, 10000),
        category={"id": random.randint(1, 10), "name": "Dogs"},
        name='doggie',
        photoUrls=["https://example.com/photo1.jpg"],
        tags=[{"id": random.randint(1, 10), "name": "tag1"}],
        status="available"
    )


@pytest.fixture
def api_client():
    """
    Fixture to provide an instance of `ApiClient` for making API requests.

    This fixture creates and returns an `ApiClient` instance initialized with the base URL.
    It is used in tests to interact with the API endpoints.
    """
    return ApiClient(BASE_URL)


@pytest.fixture
def image_file_path():
    return "assets/image.jpg"



