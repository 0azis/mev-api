from pybit.unified_trading import MarketHTTP, WebSocket
from sender import handleCoins



class Bybit:
	def Init(self):
		print("Bybit started")

		ws = WebSocket(
			testnet=False,
			channel_type="spot",
		)

		for x in range(0, 510, 10):
			ws.trade_stream(self.GetCoinsList()[x:x+10], lambda data, exchange="bybit", **kw: handleCoins(data, exchange))

		while True:
			pass

	def GetCoinsList(self) -> list:
		client = MarketHTTP(
			testnet=False
		)
		coinsList = []
		for x in client.get_tickers(category="spot")["result"]["list"]:
			coinsList.append(x["symbol"])
		
		return coinsList	

