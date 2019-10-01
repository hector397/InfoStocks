import source.data.data_requester as dt
import unittest


class CodeRetreat(unittest.TestCase):
    def test_get_data_badURL(self):
        url = ""
        data_requester = dt.DataRequester()

        self.assertIs("", data_requester.get_data_from_url(url))

    def test_get_data_goodURL(self):
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&" \
              "outputsize=full&apikey=LH3WNUH2LPYLE6R9"
        data_requester = dt.DataRequester()
        data = data_requester.get_data_from_url(url)

        self.assertTrue(isinstance(data, dict))


if __name__ == '__main__':
    unittest.main()
