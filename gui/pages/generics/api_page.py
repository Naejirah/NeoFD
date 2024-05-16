from .page import BasePage

VERSION = 1


class BaseAPIPage(BasePage):
    api_url_base = 'http://localhost:8080/api/v{}/'.format(str(VERSION))

    def get_api_url(self):
        return self.api_url_base

    def call_api(self, response):
        if response.status_code == 200:
            return response.json()
        print(f"Erreur : {response.status_code}, {response.text}")
        return None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
