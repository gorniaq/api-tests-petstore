import allure
from dataclasses import asdict
from hamcrest import assert_that, equal_to


class TestPetUpdates:
    @allure.feature("Pet Management")
    @allure.story("Update Pet Image")
    def test_update_pet_image(self, api_client, pet_data, image_file_path):
        """
        Test to verify that an image can be uploaded for a specific pet and that
        the response status is as expected.
        """
        with allure.step("Open and read the image file for upload"):
            with open(image_file_path, 'rb') as image_file:
                file_content = image_file.read()
                files = {'file': ('image.jpg', file_content, 'image/jpeg')}
                body = {'additionalMetadata': 'Test image'}

        # Send POST request to upload the image for the specified pet
        with allure.step(f"Send POST request to upload the image for pet ID {pet_data.id}"):
            response = api_client.post_form(f"pet/{pet_data.id}/uploadImage", body=body, files=files)
            # Check the response status to ensure the request was successful
            response.check_status(200)

    @allure.feature("Pet Management")
    @allure.story("Update Pet Details")
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
