import requests
from typing import *


"""
This class models a data requester to get data from an external API.
"""
class DataRequester:
    def __init__(self):
        pass

    """
    Sends a request to some endpoint and return the data.
    Arguments:
        url : (str) endpoint to make the request    
    """
    def get_data_from_url(self, url: str) -> Dict:
        try:
            request_data = requests.get(url)
        except:
            return ""

        return request_data.json()
