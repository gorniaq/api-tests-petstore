# conftest.py
import random
import string
import pytest
from PIL import Image
import os

from config import BASE_URL
from core.client import ApiClient
from core.pet_data import PetData
from core.users_data import UsersData


@pytest.fixture(scope="session")
def user_data():
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
    return ApiClient(BASE_URL)



