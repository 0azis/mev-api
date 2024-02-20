import psycopg2

class Store:
    connection = psycopg2.connect(dbname='mevdb', user='roller', password='roller123', host='localhost', port='5433')
    connection.autocommit = True
    cursor = connection.cursor()

    def Insert(self, price: int, coin: str, exchange: str):
        try:
            self.cursor.execute(f"INSERT INTO coins (pair, {exchange}) VALUES ('{coin}', {price}) ON CONFLICT (pair) DO UPDATE SET {exchange} = excluded.{exchange}")
        except Exception as _ex:
            print(_ex)

class LocalStore:
    store = {
        'bybit': [],
        'binance': []
    }

    def Insert(self, price: int, coin: str, exchange: str):
        self.store[exchange] = {coin: price}

    def Select(self):
        print(self.store)

