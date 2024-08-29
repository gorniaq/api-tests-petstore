import allure
from dataclasses import asdict


def test_create_user(api_client, user_data):
    """
    Test to verify that a user can be created and then retrieved successfully.
    """
    # Prepare the user payload using the user_data fixture
    user_payload = asdict(user_data)

    # Debugging: Print user_payload to ensure it has all necessary fields
    print("User Payload:", user_payload)

    # Step 1: Create a new user
    with allure.step("Send POST request to create a user"):
        create_response = api_client.post("user", body=user_payload)
        create_response.check_status(200)  # Verify that the status code is 200 (OK)

        # Attach response body to Allure report for debugging
        allure.attach(
            name="Create User Response",
            body=str(create_response.body()),
            attachment_type=allure.attachment_type.JSON
        )

    # Step 2: Retrieve the created user
    with allure.step("Send GET request to retrieve the user"):
        get_response = api_client.get(f"user/{user_payload['username']}")
        get_response.check_status(200)  # Verify that the status code is 200 (OK)

        # Attach response body to Allure report for debugging
        allure.attach(
            name="Get User Response",
            body=str(get_response.body()),
            attachment_type=allure.attachment_type.JSON
        )

    # Step 3: Verify the retrieved user data matches the created user data
    with allure.step("Verify the retrieved user data matches the expected data"):
        expected_user = user_payload  # No need to recreate the expected data
        get_response.exact_body(expected_user)
