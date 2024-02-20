from exchanges.store import Store
import time
from bot import bot


class Analyzer(Store):
    def SlideThrough(self, message):
        while True:
            cur = self.Cursor()
            cur.execute("select * from coins offset ((select count(*) from coins)-1)")
            lastCoins = cur.fetchall()[0]
            columns = cur.description
            for x in range(1, len(lastCoins)):
                if (lastCoins[x] != None and lastCoins[x+1] != None) and lastCoins[x] - lastCoins[x+1] < 1:
                    bot.send_message(message.from_user.id, lastCoins)
            time.sleep(0.5)

anal = Analyzer()
anal.SlideThrough()

# if __name__ == "__main__":
#     task = threading.Thread(target=anal.SlideThrough)
#     task.start()
#     while True:
#         pass
