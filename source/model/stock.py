from dataclasses import dataclass
from source.model.info_precio import InfoPrecio


"""
This dataclass models a Stock.
"""
@dataclass
class Stock:
    name: str
    info_precio: InfoPrecio

    def get_open_price(self) -> float:
        return self.info_precio.open

    def get_close_price(self) -> float:
        return self.info_precio.close

    def get_high_price(self) -> float:
        return self.info_precio.high
