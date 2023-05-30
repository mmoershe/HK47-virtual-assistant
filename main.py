from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging, sys, json, random

# This project is using Python Telegram Bot v13.7, because the newer v20.3 uses asyncio and is super ANNOYING!!!

json_file = open("data.json", "r")
json_data = json.load(json_file)
token = json_data["token"]
chatID = json_data["chatID"]
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher

'''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
'''

def verify_user(input):
    if input.from_user.id != chatID: 
        bot_send("Anomaly: Some meatbag tried accessing me with an ID that I'm not aware of is connected to you, master. The entire operation will be terminated.", f"{input.from_user.id = }", f"{input.from_user.name = }", sep="\n")
        sys.exit() 
    print("User has been verified!")

def bot_send(message): 
    updater.bot.send_message(chat_id = chatID, text = message)
    print("--------------", f"Answered: \t{message}", "--------------", sep="\n")

def startup():
    print("Bot has been started...")
    bot_send(json_data["startup"][random.randint(0, len(json_data["startup"])-1)])

def status(update: Update, context: CallbackContext):
    verify_user(update.message)
    bot_send(json_data["status"][random.randint(0, len(json_data["status"])-1)])

if __name__ == '__main__':
    startup()

    dispatcher.add_handler(CommandHandler('status', status))
    
    # loop and making it closeable
    updater.start_polling()
    updater.idle()
