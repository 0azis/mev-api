from store import Store
# p - price
# s - symbol

def handleCoins(msg, exchange):
	store = Store()
	match exchange:
		case "bybit":
			store.Insert(msg['data'][0]['p'], msg['data'][0]['s'], exchange)
		case "binance":
			store.Insert(msg['k']['o'], msg['s'], exchange)


