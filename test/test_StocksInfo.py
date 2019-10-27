import unittest
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

    """
    Test that the info returned by a stock is a string
    """
    def test_show_stock_info_existing_symbol(self):
        stock = self.stocks_info.last_info("TSLA")

        info_stock = stock.to_string()

        self.assertTrue(isinstance(info_stock, str))

    """
    Test that if the symbol doesn't exists, the info returned has no values.
    """
    def test_show_stock_info_empty_symbol(self):
        stock = self.stocks_info.last_info("")

        info_stock = stock.to_string()
        print(info_stock)

        self.assertTrue(isinstance(info_stock, str))

if __name__ == '__main__':
    unittest.main()
