from bybit import Bybit
from binancce import Binance
from helpers import pureCoins
from multiprocessing import Process

# init the exchange classes
bybit = Bybit()
binance = Binance()
# ... (and so on)

listOfCoins = pureCoins(bybit.GetCoinsList(), binance.GetCoinsList())

# run the Init functions (by threads)
if __name__ == "__main__":
	p2 = Process(target=binance.Init, args=(listOfCoins,))
	p1 = Process(target=bybit.Init, args=(listOfCoins,))	

	p1.start()
	p2.start()

	p1.join()
	p2.join()


