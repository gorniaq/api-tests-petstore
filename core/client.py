import logging
import os
import requests
import deepdiff

from dotenv import load_dotenv
from hamcrest import assert_that, equal_to

logging.basicConfig(level=logging.DEBUG)


class ApiClient(object):
    def __init__(self, base_url):
        """
        Initializes the ApiClient with the base URL and loads environment variables for authentication.
        """
        self.username = None
        self.password = None
        self.base_url = base_url
        self.session = requests.Session()
        self.load_env_variables()

    def _build_url(self, url):
        """
        Constructs the full URL for an API request.
        """
        logging.debug(f"Request url: {self.base_url}/{url}")
        return f"{self.base_url}/{url}"

    def load_env_variables(self):
        """
        Loads environment variables for username and password using dotenv.
        """
        load_dotenv()
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")

    def get(self, url, headers=None, cookies=None):
        return ApiResponse(self.session.get(self._build_url(url), headers=headers, cookies=cookies))

    def post(self, url, body=None, headers=None, cookies=None):
        """
        Sends a POST request with a JSON body to the specified URL.
        """
        response = self.session.post(self._build_url(url), json=body, headers=headers, cookies=cookies)
        return ApiResponse(response)

    def post_form(self, url, body=None, files=None, headers=None, cookies=None):
        """
        Sends a POST request with form data and files to the specified URL.
        """
        response = self.session.post(self._build_url(url), data=body, files=files, headers=headers, cookies=cookies)
        return ApiResponse(response)

    def delete(self, url, headers=None, cookies=None):
        """
        Sends a DELETE request to the specified URL.
        """
        response = self.session.delete(self._build_url(url), headers=headers, cookies=cookies)
        return ApiResponse(response)

    def login(self, username, password) -> "ApiResponse":
        """
        Logs in a user using the provided username and password.
        """
        url = f"user/login?username={username}&password={password}"
        return self.get(url)


class ApiResponse(object):
    """
    A wrapper for handling API responses.

    Attributes:
    _response (requests.Response): The raw response object from the requests library.
    """
    def __init__(self, response):
        """
        Initializes the ApiResponse with the raw response object.
        """
        self._response = response

    def body(self):
        """
        Returns the JSON body of the response.
        """
        return self._response.json()

    def check_status(self, status_code):
        """
        Asserts that the response status code matches the expected status code.
        """
        logging.info(f"Status code: {self._response.status_code}")
        assert_that(self._response.status_code, equal_to(status_code))

    def exact_body(self, expected_body):
        """
        Compares the response body with an expected body using deepdiff.
        """
        resp = self.body()
        diff = deepdiff.DeepDiff(resp, expected_body)
        if diff:
            logging.info(diff.to_json())
            assert_that(diff.to_json(), equal_to({}))
