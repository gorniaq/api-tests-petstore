import allure
from dataclasses import asdict

from hamcrest import assert_that, equal_to

from config import BASE_URL
from core.client import ApiClient


class TestUserManagement:

    @allure.feature("Create User")
    @allure.story("Create Single User")
    def test_create_user(self, api_client, user_data):
        """
        Test to verify that a user can be created and then retrieved successfully.
        """
        # Prepare the user payload using the user_data fixture
        user_payload = asdict(user_data)

        # Create a new user
        with allure.step("Send POST request to create a user"):
            create_response = api_client.post("user", body=user_payload)
            create_response.check_status(200)  # Verify that the status code is 200 (OK)

        # Retrieve the created user
        with allure.step("Send GET request to retrieve the user"):
            get_response = api_client.get(f"user/{user_payload['username']}")
            get_response.check_status(200)  # Verify that the status code is 200 (OK)

        # Verify the retrieved user data matches the created user data
        with allure.step("Verify the retrieved user data matches the expected data"):
            expected_user = user_payload  # No need to recreate the expected data
            get_response.exact_body(expected_user)

    @allure.feature("Create Users")
    @allure.story("Create list of users with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_users_with_list(self, user_data, api_client):
        client = ApiClient(BASE_URL)

        # Prepare the 2 users payload using the user_data fixture
        users_payload = [asdict(user_data) for _ in range(2)]

        # Creating a list of users
        with allure.step("Create list of users with provided array"):
            response = api_client.post("user/createWithList", body=users_payload)
            response.check_status(200)  # Проверка, что статус-код 200 (OK)

        # Verifying that the response message matches expectations
        with allure.step("Verify response message content"):
            response_body = response.body()
            assert_that(response_body["message"], equal_to("ok"), "Response message should be 'ok'")
