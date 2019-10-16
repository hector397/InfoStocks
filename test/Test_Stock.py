from source.model.stock import Stock
import unittest
from unittest.mock import patch

"""
This class test the  get_data method from DataRequester class
"""
class TestStockGetters(unittest.TestCase):
    @patch("source.model.info_precio")
    def setUp(self, MockInfoPrecio):
        self.info_precio = MockInfoPrecio()
        self.info_precio.open = 1.58
        self.info_precio.close = 7.58
        self.info_precio.high = 10.78
        self.stock = Stock("TSLA", self.info_precio)

    """
    Test if high price is a float.
    """
    def test_get_high_price(self):
        price = self.stock.get_high_price()

        self.assertEqual(10.78, price)

    """
    Test if open price is a float.
    """
    def test_get_open_price(self):
        price = self.stock.get_open_price()

        self.assertEqual(1.58, price)

    """
    Test if close price is a float.
    """
    def test_get_close_price(self):
        price = self.stock.get_close_price()

        self.assertEqual(7.58, price)
