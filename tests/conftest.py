import random
import string
import pytest

from config import BASE_URL
from core.client import ApiClient
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


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)