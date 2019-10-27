from source.model.observer_pattern import Subject, Observer
from source.data.data_requester import DataRequester
from source.model.stock import Stock
from source.model.info_precio import InfoPrecio
from typing import *


class StocksInfo(Subject):
    def __init__(self, observer: Observer):
        super().__init__()
        super()._add_observer(observer)
        self.stock = None

    def last_info(self, symbol: str) -> None:
        data = self.__get_last_stock_data(symbol)
        info_precio = self.__data_to_info_price(data)
        self.__create_stock(symbol, info_precio)

        return self.stock

    def __create_stock(self, symbol: str, info_precio: InfoPrecio) -> Stock:
        self.stock = Stock(symbol, info_precio)


    def __data_to_info_price(self, data: Dict) -> InfoPrecio:
        try:
            key = self.__get_last_key_of_data(data["Time Series (1min)"])
        except:
            return InfoPrecio(0.0, 0.0, 0.0, 0.0, 0.0)

        stock_price = data["Time Series (1min)"][key]

        open = stock_price["1. open"]
        high = stock_price["2. high"]
        low = stock_price["3. low"]
        close = stock_price["4. close"]
        volume = stock_price["5. volume"]

        return InfoPrecio(open, high, low, close, volume)

    def __get_last_key_of_data(self, data: Dict) -> str:
        return list(data.keys())[0]

    """
    Get the data of a stock in an interval of 1 min.
    Parameters:
        - symbol: symbol of 
    """
    def __get_last_stock_data(self, symbol: str) -> Dict:
        data_requester = DataRequester()

        data = data_requester.get_data_from_url("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&" 
                                                "symbol=" + symbol + "&interval=1min&outputsize=full&apikey=LH3WNUH2LPYLE6R9")

        return data

