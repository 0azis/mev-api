import psycopg2

class Store:

    def Cursor(self):
        connection = psycopg2.connect(dbname='mevdb', user='roller', password='roller123', host='localhost', port='5433')
        connection.autocommit = True
        return connection.cursor()

    def Insert(self, price: int, coin: str, exchange: str):
        try:
            self.Cursor().execute(f"INSERT INTO coins (pair, {exchange}) VALUES ('{coin}', {price}) ON CONFLICT (pair) DO UPDATE SET {exchange} = excluded.{exchange}")
        except Exception as _ex:
            print(_ex)



# The another option to use store in our service

# class LocalStore:
#     store = {
#         'bybit': [],
#         'binance': []
#     }

#     def Insert(self, price: int, coin: str, exchange: str):
#         self.store[exchange] = {coin: price}

#     def Select(self):
#         print(self.store)

