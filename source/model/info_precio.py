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
