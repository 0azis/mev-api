from bybit import BybitPy
from binancce import BinancePy
from multiprocessing import Process


if __name__ == "__main__":
	p1 = Process(target=BinancePy)
	p1.start()
	p2 = Process(target=BybitPy)
	p2.start()
	p1.join()
	p2.join()

