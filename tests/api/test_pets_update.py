import allure
from dataclasses import asdict
from hamcrest import assert_that, equal_to


class TestPetUpdates:

    @allure.feature("Pet Management")
    @allure.story("Update Pet Details")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_pet_name_and_status(self, api_client, pet_data):
        """
        Test to verify that a pet's name and status can be updated successfully.
        """
        with allure.step("Create a new pet"):
            # Create the pet
            response = api_client.post("pet", body=asdict(pet_data))
            response.check_status(200)
            response_body = response.body()
            pet_id = response_body.get("id")

        with allure.step("Update pet's name and status"):
            # Prepare form data for update
            form_data = {
                'name': 'updated_name',
                'status': 'sold'
            }
            # Update pet details using form data
            update_response = api_client.post_form(f"pet/{pet_id}", body=form_data,
                                                   headers={'Content-Type': 'application/x-www-form-urlencoded'})
            update_response.check_status(200)

        with allure.step("Verify pet details after update"):
            # Get updated pet details
            get_response = api_client.get(f"pet/{pet_id}")
            get_response.check_status(200)
            get_response_body = get_response.body()
            assert_that(get_response_body['name'], equal_to('updated_name'))
            assert_that(get_response_body['status'], equal_to('sold'))
