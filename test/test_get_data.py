import source.data.data_requester
import unittest
from unittest.mock import patch

"""
This class test the  get_data method from DataRequester class
"""
class TestGetData(unittest.TestCase):
    @patch("source.data.data_requester.DataRequester")
    def setUp(self, MockDataRequester):
        self.data_requester = MockDataRequester()

    """
    Test if the url is incorrect.
    """
    def test_get_data_badURL(self):
        url = ""
        self.data_requester.get_data_from_url.return_value = ""

        response = self.data_requester.get_data_from_url(url)

        self.assertIs("", response)

    """
    Test if the returned data is a Dictionary (JSON).
    """
    def test_get_data_response_is_dict(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&" \
              "outputsize=full&apikey=LH3WNUH2LPYLE6R9"
        self.data_requester.get_data_from_url.return_value = {}
        response = self.data_requester.get_data_from_url(url)

        self.assertTrue(isinstance(response, dict))

    """
    Test if the returned JSON is not empty.
    """
    def test_get_data_notEmptyDict(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&" \
              "outputsize=full&apikey=LH3WNUH2LPYLE6R9"
        self.data_requester.get_data_from_url.return_value = {"h": "h"}
        response = self.data_requester.get_data_from_url(url)

        self.assertTrue(len(response) != 0)


if __name__ == '__main__':
    unittest.main()
