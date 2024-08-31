import allure
from hamcrest import assert_that, equal_to

from config import BASE_URL
from core.client import ApiClient


class TestAuth:
    @allure.feature("Login Functionality")
    @allure.story("Login with valid credentials")
    def test_login_user(self):
        # Initialize the API client with the base URL
        client = ApiClient(BASE_URL)

        with allure.step("Verify login response status code is 200"):
            # Send a login request using the username and password
            response = client.login(client.username, client.password)
            # Ensure the login response status code is 200 (OK)
            response.check_status(200)

        with allure.step("Verify login message format"):
            # Extract the login response body and verify the message format
            login_data = response.body()
            session_message = "logged in user session:" + login_data['message'].split(":")[1]
            assert_that(login_data['message'], equal_to(session_message), "Login message should match expected pattern")

    @allure.feature("User Authentication")
    @allure.story("Logout User")
    def test_logout_user(self):
        # Initialize the API client with the base URL
        client = ApiClient(BASE_URL)

        with allure.step("Login as user to obtain session"):
            # Log in as a user to get a valid session
            login_response = client.login(client.username, client.password)
            login_response.check_status(200)

        with allure.step("Log out the current user session"):
            # Send a request to log out the current user session
            logout_response = client.get("user/logout")
            # Ensure the logout response status code is 200 (OK)
            logout_response.check_status(200)

        with allure.step("Verify response message content"):
            # Extract the logout response body and verify the message content
            response_body = logout_response.body()
            assert_that(response_body["message"], equal_to("ok"), "Response message should be 'ok' after logout")
