"""
ExchangeWebsocket - A Python package for connecting to cryptocurrency exchange WebSocket APIs

This package provides a unified interface for connecting to various cryptocurrency
exchange WebSocket APIs including Binance, OKX, Bitget, Bybit, and Gate.io.
"""

__version__ = "0.1.0"
__author__ = "yunmengwork"
__email__ = "yunmengwork2940494978@gmail.com"

from .lib.baseWebsocket import ExchangeWebsocket
from .exchange.okx import Okx
from .exchange.binance import Binance
from .exchange.bitget import Bitget
from .exchange.bybit import Bybit

__all__ = [
    "ExchangeWebsocket",
    "Okx",
    "Binance",
    "Bitget",
    "Bybit",
]
