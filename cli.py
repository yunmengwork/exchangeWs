#!/usr/bin/env python
"""
Command line interface for exchange-websocket package
"""

import argparse
import asyncio
import sys
from typing import List

from .exchange.okx import Okx, getAllOkxSymbols
from .exchange.binance import Binance, getAllBinanceSymbols
from .exchange.bitget import Bitget, getAllBitgetSymbols


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Exchange WebSocket CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  exchange-websocket symbols okx        # List all OKX symbols
  exchange-websocket symbols binance    # List all Binance symbols
  exchange-websocket symbols bitget     # List all Bitget symbols
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Symbols command
    symbols_parser = subparsers.add_parser("symbols", help="Get exchange symbols")
    symbols_parser.add_argument(
        "exchange", choices=["okx", "binance", "bitget"], help="Exchange name"
    )

    # Version command
    version_parser = subparsers.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "symbols":
        if args.exchange == "okx":
            symbols = getAllOkxSymbols()
            print(f"OKX USDT-SWAP symbols ({len(symbols)}):")
            for symbol in symbols:
                print(f"  {symbol}")
        elif args.exchange == "binance":
            symbols = getAllBinanceSymbols()
            print(f"Binance USDT symbols ({len(symbols)}):")
            for symbol in symbols:
                print(f"  {symbol}")
        elif args.exchange == "bitget":
            symbols = getAllBitgetSymbols()
            print(f"Bitget USDT-FUTURES symbols ({len(symbols)}):")
            for symbol in symbols:
                print(f"  {symbol}")

    elif args.command == "version":
        from . import __version__

        print(f"exchange-websocket version {__version__}")

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
