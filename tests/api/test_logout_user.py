import allure
from hamcrest import assert_that, equal_to

from config import BASE_URL
from core.client import ApiClient


@allure.feature("User Authentication")
@allure.story("Logout User")
@allure.severity(allure.severity_level.NORMAL)
def test_logout_user():
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
