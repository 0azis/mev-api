from bybit import Bybit
from binancce import Binance
from helpers import pureCoins
from multiprocessing import Process

# init the exchange classes
bybit = Bybit()
binance = Binance()
# ... (and so on)


# run the Init functions (by threads)
if __name__ == "__main__":
	p2 = Process(target=binance.Init, args=(binance.GetCoinsList(),))
	p1 = Process(target=bybit.Init, args=(bybit.GetCoinsList(),))	

	p1.start()
	p2.start()

	p1.join()
	p2.join()


