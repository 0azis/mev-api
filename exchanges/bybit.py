from pybit.unified_trading import WebSocket
from time import sleep
import json

ws = WebSocket(
    testnet=False,
    channel_type="spot",
)

def handle_orderbook(message):
    print(message["data"])

ws.orderbook_stream(1, "BTCUSDT", handle_orderbook)

while True:
	pass