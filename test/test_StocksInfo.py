import unittest
from unittest.mock import patch
from source.model.stocks_info import StocksInfo
from source.model.stock import Stock


"""
Tests for StocksInfo class
"""
class TestStocksInfo(unittest.TestCase):
    def setUp(self):
        self.stocks_info = StocksInfo(None)


    """
    Test if the object returned is a stock
    """
    def test_last_info_exist_stock(self):
        stock = self.stocks_info.last_info("TSLA")

        self.assertTrue(isinstance(stock, Stock))

    """
    Test that if the symbol doesn't exists, still return an Stock object.
    """
    def test_last_info_empty_symbol(self):
        stock = self.stocks_info.last_info("")

        self.assertTrue(isinstance(stock, Stock))

    def test_show_stock_info_existing_symbol(self):
        stock = self.stocks_info.last_info("TSLA")

        info_stock = stock.to_string()
        print(info_stock)

        self.assertTrue(isinstance(stock, Stock))

    def test_show_stock_info_empty_symbol(self):
        stock = self.stocks_info.last_info("")

        info_stock = stock.to_string()
        print(info_stock)

        self.assertTrue(isinstance(stock, Stock))

if __name__ == '__main__':
    unittest.main()
