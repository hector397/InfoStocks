from dataclasses import dataclass

"""
This dataclass models the price information about a stock
"""
@dataclass
class InfoPrecio:
    open: float
    high: float
    low: float
    close: float
    volume: int

    def to_string(self) -> str:
        return "open: " + str(self.open) + "\nhigh: " + str(self.high) + "\nlow: " + str(self.low) + \
               "\nclose: " + str(self.close) + "\nvolume: " + str(self.volume)


