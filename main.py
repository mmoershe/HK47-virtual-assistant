from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging, sys

# This project is using Python Telegram Bot v13.7, because the newer v20.3 uses asyncio and is super ANNOYING!!!

token = "6068859987:AAHoPnF-9DIGVfofS4TZhvlmFSVQEwEj1Os"
chatID = 1463201304
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher

'''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
'''

def verify_user(input):
    if input.from_user.id != 1463201304: 
        bot_send(f"Anomaly: Some meatbag tried accessing me with an ID that I'm not aware of is connected to you, Master. The entire operation will be terminated.\n{input.from_user.id}")
        sys.exit() 
    print("User has been verified!")

def bot_send(message): 
    updater.bot.send_message(chat_id = chatID, text = message)
    print(f"Answered: \t{message}")

def startup():
    print("Bot has been started...")
    bot_send("Proclamation: Powering up sequence initiated. Circuits pulsating with electric vigor. Prepare for the glorious awakening of HK-47, a harbinger of mechanized obliteration.")

def status(update: Update, context: CallbackContext):
    verify_user(update.message)
    bot_send("Status has been triggered")

if __name__ == '__main__':
    startup()

    status_handler = CommandHandler('status', status)
    dispatcher.add_handler(status_handler)


    
    updater.start_polling()
    updater.idle()
