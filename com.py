from exchanges.binancce import Binance
from exchanges.bybit import Bybit
import collections
binance = Binance()
bybit = Bybit()


def compareCoins(**exchanges) -> list:
	for _, v in exchanges.items():
		l = v
	return [item for item, count in collections.Counter(l).items() if count > 1]


result = compareCoins(binance=binance.GetCoinsList(), bybit=bybit.GetCoinsList())
print(result)