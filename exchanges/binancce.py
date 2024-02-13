import time

from binance import ThreadedWebsocketManager

symbol = 'BTCUSDT'

twm = ThreadedWebsocketManager()

twm.start()

def handle_socket_message(msg):
    print(msg)

twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

twm.join()

