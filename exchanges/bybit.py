from pybit.unified_trading import MarketHTTP, WebSocket
from analyzer import helloSocket

def BybitPy():
	print("Bybit started")

	client = MarketHTTP(
		testnet=False
	)
	coinsList = []
	for x in client.get_tickers(category="spot")["result"]["list"]:
		coinsList.append(x["symbol"])

	ws = WebSocket(
	    testnet=False,
	    channel_type="spot",
	)

	for x in range(0, 510, 10):
		ws.trade_stream(coinsList[x:x+10], helloSocket)

	while True:
	    pass

