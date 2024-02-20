from binance.client import Client
from binance import ThreadedWebsocketManager
from helpers import handleCoins

class Binance():
	def Init(self, coins):
		print("Binance Started")

		twm = ThreadedWebsocketManager()
		twm.start()

		for x in coins:
			twm.start_kline_socket(callback=lambda data, exchange="binance", **kw: handleCoins(data, exchange), symbol=x)
		twm.join()
	
	def GetCoinsList(self) -> list:
		client = Client()
		coinList = []
		for x in client.get_all_tickers():
			coinList.append(x['symbol'])
		return coinList
		 
	


