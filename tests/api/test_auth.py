import allure
from hamcrest import assert_that, equal_to

from config import BASE_URL
from core.client import ApiClient


class TestAuth:
    @allure.feature("Login Functionality")
    @allure.story("Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user(self):
        client = ApiClient(BASE_URL)

        with allure.step("Log in as user"):
            response = client.login(client.username, client.password)

        with allure.step("Verify login response status code is 200"):
            response.check_status(200)

        with allure.step("Verify login message format"):
            login_data = response.body()
            session_message = "logged in user session:" + login_data['message'].split(":")[1]
            assert_that(login_data['message'], equal_to(session_message), "Login message should match expected pattern")

    @allure.feature("User Authentication")
    @allure.story("Logout User")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout_user(self):
        client = ApiClient(BASE_URL)

        with allure.step("Login as user to obtain session"):
            login_response = client.login(client.username, client.password)
            login_response.check_status(200)

        with allure.step("Log out the current user session"):
            logout_response = client.get("user/logout")

        with allure.step("Verify response status code is 200"):
            logout_response.check_status(200)

        with allure.step("Verify response message content"):
            response_body = logout_response.body()
            assert_that(response_body["message"], equal_to("ok"), "Response message should be 'ok' after logout")
