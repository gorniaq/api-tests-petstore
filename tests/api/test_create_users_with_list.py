import allure
from dataclasses import asdict
from hamcrest import assert_that, equal_to

from config import BASE_URL
from core.client import ApiClient


@allure.feature("Create Users")
@allure.story("Create list of users with valid data")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_users_with_list(user_data):
    client = ApiClient(BASE_URL)

    # Prepare the 2 users payload using the user_data fixture
    user_payload = [asdict(user_data) for _ in range(2)]

    with allure.step("Create list of users with provided array"):
        response = client.post("user/createWithList", body=user_payload)

    with allure.step("Verify response status code is 200"):
        response.check_status(200)

    with allure.step("Verify response message content"):
        response_body = response.body()
        assert_that(response_body["message"], equal_to("ok"), "Response message should be 'ok'")
