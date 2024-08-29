from hamcrest import assert_that, equal_to
import allure
from config import BASE_URL
from core.client import ApiClient


@allure.feature("Login Functionality")
@allure.story("Login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_user():
    client = ApiClient(BASE_URL)

    with allure.step("Log in as user"):
        response = client.login(client.username, client.password)

    with allure.step("Verify login response status code is 200"):
        response.check_status(200)

    with allure.step("Verify login message format"):
        login_data = response.body()
        session_message = "logged in user session:" + login_data['message'].split(":")[1]
        assert_that(login_data['message'], equal_to(session_message), "Login message should match expected pattern")



