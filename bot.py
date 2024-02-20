import telebot
from exchanges.store import Store
import time


bot = telebot.TeleBot('7093677307:AAHbUfHv853df6Pv2l_OJfWiLwtLraRYjwo')

class Analyzer(Store):
    def SlideThrough(self, message):
        lastMsg = ''
        while True:
            cur = self.Cursor()
            cur.execute("select * from coins offset ((select count(*) from coins)-1)")
            lastCoins = cur.fetchall()[0]
            columns = cur.description
            
            for x in range(1, len(lastCoins)):
                if (lastCoins[x] != None and lastCoins[x+1] != None) and lastCoins[x] - lastCoins[x+1] < 1:
                    if lastMsg != lastCoins[0]:
                        print(lastCoins)
                        bot.send_message(message.from_user.id, f'''New Available Coin: {lastCoins[0]}\nPrice on {columns[x][0]}: {lastCoins[x]}$\nPrice on {columns[x+1][0]}: {lastCoins[x+1]}$''')
                        lastMsg = lastCoins[0]
            time.sleep(0.5)

anal = Analyzer()



@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, "hello")
    anal.SlideThrough(message)




bot.polling(none_stop=True, interval=0)