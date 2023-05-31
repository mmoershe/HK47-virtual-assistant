from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging, os, json, random, time

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
        stop('stop', stop)

def bot_send(message): 
    updater.bot.send_message(chat_id = chatID, text = message)
    print("\t--------------", f"\t{message}", "\t--------------", sep="\n\n")

def startup():
    print("Bot has been started")
    startup_message = json_data["startup"][random.randint(0, len(json_data["startup"])-1)]
    bot_send(f"{startup_message} /standard")

def stop(update: Update, context: CallbackContext):
    bot_send(json_data["stop"][random.randint(0, len(json_data["stop"])-1)])
    print("Bot is shutting down.")
    os._exit(0)

def status(update: Update, context: CallbackContext):
    
    verify_user(update.message)
    bot_send(json_data["status"][random.randint(0, len(json_data["status"])-1)])
    
def standard(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Antwort 1")],
        [KeyboardButton("/calendar")],
        [KeyboardButton("Antwort 3")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    update.message.reply_text("standard reply", reply_markup=reply_markup)    

def calendar(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Calendar Option 1")], 
        [KeyboardButton("Calendar Option 2")], 
        [KeyboardButton("Calendar Option 3")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    #update.message.reply_text("Choose a Calendar option: ", reply_markup=reply_markup)
    updater.bot._replace_keyboard(reply_markup=reply_markup)

if __name__ == '__main__':
    startup()

    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("standard", standard))
    dispatcher.add_handler(CommandHandler("calendar", calendar))

   


    # loop and making it closeable
    updater.start_polling()
    updater.idle()
