from exchanges.bybit import BybitInit
from exchanges.binancce import BinanceInit
from multiprocessing import Process


if __name__ == "__main__":
	p1 = Process(target=BinanceInit)
	p1.start()
	p2 = Process(target=BybitInit)
	p2.start()
	p1.join()
	p2.join()

