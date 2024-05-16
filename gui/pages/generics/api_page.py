from .page import BasePage

# API Version
VERSION = 1


class BaseAPIPage(BasePage):
    """
    Base class for connecting to the API.
    """
    # Url to connect to the API
    api_url_base = 'http://localhost:8080/api/v{}/'.format(str(VERSION))

    def get_api_url(self):
        """
        Method to get the API URL.

        @return: API url
        """
        return self.api_url_base

    def call_api(self, response):
        """
        Method to call the API.

        @param response: API response
        @return: JSON response or None
        """
        if response.status_code == 200:
            return response.json()
        print(f"Erreur : {response.status_code}, {response.text}")
        return None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
