import json
import os
import threading
from dataclasses import dataclass
from typing import List

import websocket

from .black_scholes import price


@dataclass
class MarketData:
    symbol: str
    price: float
    timestamp: int


def _build_subscribe_params(symbols: List[str]) -> str:
    return ",".join(f"T.{s}" for s in symbols)


class PolygonWebSocketClient:
    def __init__(self, api_key: str, symbols: List[str]):
        self.api_key = api_key
        self.symbols = symbols
        self.ws_url = "wss://socket.polygon.io/stocks"

    def run(self):
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.start()

    def on_open(self, ws):
        auth_data = {"action": "auth", "params": self.api_key}
        ws.send(json.dumps(auth_data))
        sub_data = {"action": "subscribe", "params": _build_subscribe_params(self.symbols)}
        ws.send(json.dumps(sub_data))

    def on_message(self, ws, message):
        print("Received:", message)
        # Here you would parse the message and trigger trading logic.

    def on_error(self, ws, error):
        print("WebSocket error", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket closed", close_status_code, close_msg)


class BlackScholesTrader:
    def __init__(self, client: PolygonWebSocketClient):
        self.client = client

    def start(self):
        self.client.run()


if __name__ == "__main__":
    api_key = os.getenv("POLYGON_API_KEY")
    if not api_key:
        raise RuntimeError("POLYGON_API_KEY environment variable not set")

    symbols = ["AAPL"]  # Example symbol list
    client = PolygonWebSocketClient(api_key, symbols)
    trader = BlackScholesTrader(client)
    trader.start()
