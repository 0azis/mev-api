from db import Store


# p - price
# s - symbol

def handleCoins(msg, exchange):
	store = Store()
	if exchange == "bybit":
		store.Insert(msg['data'][0]['p'], msg['data'][0]['s'], exchange)
	if exchange == "binance":
		# store.Insert(msg['k']['o'], msg['s'], exchange)
		print(msg)
