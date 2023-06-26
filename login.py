from telegram import Update
from telegram.ext import Updater
import time


# This project is using Python Telegram Bot v13.7, because the newer v20.3 uses asyncio and is super ANNOYING!!!

message = "Statement: Some meatbag logged into your Thinkpad."
token = "6068859987:AAHoPnF-9DIGVfofS4TZhvlmFSVQEwEj1Os"
chatID = 1463201304
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher
    

if __name__ == '__main__':
    while True:
        try:
            updater.bot.send_message(chat_id = chatID, text = message)
            break
        except:
            print("FENSTER NICHT SCHLIEßEN", "Bitte stelle eine Verbindung zum Internet her.", sep="\n")
            time.sleep(1)
if __name__ != '__main__':
    print("__name__ ist nicht main")
