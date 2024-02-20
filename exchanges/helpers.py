from store import Store
# p - price
# s - symbol

def handleCoins(msg, exchange):
	store = Store()
	if exchange == "bybit":
		store.Insert(msg['data'][0]['p'], msg['data'][0]['s'], exchange)
	if exchange == "binance":
		store.Insert(msg['k']['o'], msg['s'], exchange)

def pureCoins(*exchanges) -> list:
    # print(len(exchanges['binance']) + len(exchanges['bybit'])) # 2990
	coinsList = []
	for v in exchanges:
		coinsList += v
	return list(set([x for x in coinsList if coinsList.count(x) > 1]))
