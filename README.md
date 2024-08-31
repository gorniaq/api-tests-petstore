# API Tests for Petstore

This repository contains automated API tests for the [Swagger Petstore](https://petstore.swagger.io) using Python and pytest.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gorniaq/api-tests-petstore.git
   cd api-tests-petstore
   
2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

3. Running Tests

   To run all tests:
      ```bash
      pytest
      ```
   To run tests and generate Allure reports:
      ```bash
      pytest --alluredir=reports
      allure serve reports
      ```

## Allure Test Report
![Allure Report](https://i.imgur.com/gy8vEGw.png)
