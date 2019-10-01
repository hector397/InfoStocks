import requests
from typing import *


class DataRequester:
    def __init__(self):
        pass

    def get_data_from_url(self, url: str) -> Dict:
        try:
            request_data = requests.get(url)
        except:
            return ""

        return request_data.json()
