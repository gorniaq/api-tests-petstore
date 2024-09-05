import allure
from dataclasses import asdict


class TestPetManagement:

    @allure.feature("Pet Management")
    @allure.story("Add a new pet to the store")
    def test_add_new_pet(self, api_client, pet_data):
        """
        Test to verify that a pet can be added and then retrieved successfully.
        """
        # Prepare the pet payload using the pets_data fixture
        pet_payload = asdict(pet_data)

        # Add a new pet
        with allure.step("Send POST request to add a new pet"):
            add_response = api_client.post("pet", body=pet_payload)
            add_response.check_status(200)  # Verify that the status code is 200 (OK)

            # Add a new pet
            with allure.step("Send POST request to add a new pet"):
                add_response = api_client.post("pet", body=pet_payload)
                add_response.check_status(200)  # Verify that the status code is 200 (OK)

            # Retrieve the added pet
            with allure.step("Send GET request to retrieve the pet"):
                get_response = api_client.get(f"pet/{pet_payload['id']}")
                get_response.check_status(200)  # Verify that the status code is 200 (OK)

            # Verify the retrieved pet data matches the added pet data
            with allure.step("Verify the retrieved pet data matches the expected data"):
                expected_pet = pet_payload
                get_response.exact_body(expected_pet)

    @allure.feature("Pet Management")
    @allure.story("Create and Delete Pet")
    def test_delete_pet(self, api_client, pet_data):
        """
            Test to verify that a pet can be created and then deleted.
            This includes creating a pet, verifying its creation,
            deleting the pet, and checking that it is no longer available.
        """
        with allure.step("Create a new pet"):
            # Create the pet
            response = api_client.post("pet", body=pet_data.__dict__)
            response.check_status(200)
            response_body = response.body()
            created_pet_id = response_body.get("id")

            # Verify that the pet was created
            assert created_pet_id == pet_data.id

        with allure.step("Delete the pet"):
            # Delete the pet
            delete_response = api_client.delete(f"pet/{created_pet_id}")
            delete_response.check_status(200)

        with allure.step("Verify the pet is no longer available"):
            # Optionally verify the pet is no longer available
            get_response = api_client.get(f"pet/{created_pet_id}")
            get_response.check_status(404)

