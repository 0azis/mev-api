from analyzer import helloSocket

from binance.client import Client
from binance import ThreadedWebsocketManager

def BinancePy():
	print("Binance Started")

	client = Client()
	twm = ThreadedWebsocketManager()
	twm.start()

	coinsList = []
	for x in client.get_all_tickers():
		twm.start_kline_socket(helloSocket, x["symbol"])

	twm.join()