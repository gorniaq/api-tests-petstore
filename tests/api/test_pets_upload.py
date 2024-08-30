import allure
from dataclasses import asdict


class TestPetImageUpload:

    @allure.feature("Pet Management")
    @allure.story("Update Pet’s Image")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_pet_image(self, api_client, pet_data, image_file):
        """
        Test to verify that an image can be uploaded to a pet and the response is correct.
        """
        # Преобразуем данные питомца в словарь с использованием asdict
        pet_payload = asdict(pet_data)

        # Загружаем изображение для питомца
        with open(image_file, 'rb') as img:
            files = {'file': img}
            response = api_client.post(f'pet/{pet_data.id}/uploadImage', files=files)

        # Проверка статуса ответа
        assert response.status_code == 200
        # Проверка, что ответ содержит информацию о загруженном изображении
        response_data = response.json()
        assert "message" in response_data
        assert "uploaded to" in response_data["message"]

