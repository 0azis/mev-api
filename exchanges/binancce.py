from sender import handleCoins

from binance.client import Client
from binance import ThreadedWebsocketManager

class Binance:
	def Init(self):
		print("Binance Started")

		client = Client()
		twm = ThreadedWebsocketManager()
		twm.start()

		coinList = []
		for x in client.get_all_tickers():
			coinList.append(x['symbol'])
			if len(coinList) > 500:
				break
		
		for x in coinList:
			twm.start_kline_socket(callback=lambda data, exchange="binance", **kw: handleCoins(data, exchange), symbol=x)
		# for x in client.get_all_tickers():
		# 	twm.start_kline_socket(callback=lambda data, exchange="binance", **kw: handleCoins(data, exchange), symbol=x['symbol'])
		twm.join()
	
	def GetCoinsList(self) -> list:
		client = Client()
		coinList = []
		for x in client.get_all_tickers():
			coinList.append(x['symbol'])
		return coinList
		 
	


