
from time import sleep
from analyzer import *
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext
)
from analyzer import full_analyzer


def start(update: Update, context: CallbackContext):
   crypto_sym = ["btcusdt","ethusdt","trxusdt","shibusdt","xrpusdt","ltcusdt"]
   stock_sym = ["msft","goog","tsla","aapl"]
   while True:
    #crypto_sym,stock_sym = read_data() NO LONGER USABLE
    # print(crypto_sym , stock_sym)
     for sym in crypto_sym:
           # print(i)
            
            #I could not solve the problem with the db so I created this method to repair my text
            results = full_analyzer(sym,"binance")
            for result in results:
                context.bot.send_message("@Your_Channel_ID",result)
                sleep(8)
            sleep(10)
     for sym in stock_sym:
            results = full_analyzer(sym,"nasdaq")
            for result in results:
                context.bot.send_message("@Your_Channel_ID",result)
                sleep(8)
            sleep(10)


def main():
     updater = Updater(token="Your Bot Token")
     
     dis = updater.dispatcher

     dis.add_handler(CommandHandler("start",start))
     print("Bot Started...")
     updater.start_polling()
     updater.idle()


main()