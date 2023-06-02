from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup        
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, CallbackContext, Filters
import logging, os, json, random, time
from pytube import YouTube

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

def get_random_sentence(input):
    return json_data[input][random.randint(0, len(json_data[input])-1)]

def verify_user(input):
    if input.from_user.id != chatID: 
        bot_send("Anomaly: Some meatbag tried accessing me with an ID that I'm not aware of is connected to you, master. The entire operation will be terminated.", f"{input.from_user.id = }", f"{input.from_user.name = }", sep="\n")
        stop('stop', stop)

def bot_send(message): 
    updater.bot.send_message(chat_id = chatID, text = message)
    print("\t--------------", f"\t{message}", "\t--------------", sep="\n\n")

def startup():
    print("Bot has been started")
    startup_message = get_random_sentence("startup")
    bot_send(f"{startup_message} /youtube")

def stop(update: Update, context: CallbackContext):
    bot_send(json_data["stop"][random.randint(0, len(json_data["stop"])-1)])
    print("Bot is shutting down.")
    os._exit(0)

def status(update: Update, context: CallbackContext):
    
    verify_user(update.message)
    bot_send(get_random_sentence(status))
    
def standard(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Antwort 1")],
        [KeyboardButton("/calendar")],
        [KeyboardButton("Antwort 3")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    update.message.reply_text("standard reply", reply_markup=reply_markup)    

def calendar(update: Update, context: CallbackContext):
    bot_send("calendar has been triggered.")
def youtube(update: Update, context: CallbackContext):
    bot_send(get_random_sentence("youtube_link_request"))
    return STATE1_youtube

def STATE1_youtube_handler(update, context):
    input_video = YouTube(update.message.text.strip())
    keyboard = [
        [KeyboardButton("Yes")],
        [KeyboardButton("No")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    update.message.reply_text(f"Statement: The video is called:\n'{input_video.title}' [{input_video.length} seconds]\nby {input_video.author}\nQuestion: Is that correct?", reply_markup=reply_markup) 
    return STATE2_youtube
    
def STATE2_youtube_handler(update, context):
    if update.message.text.lower() != "Yes":
        return ConversationHandler.END
    
    keyboard = [
        [KeyboardButton("MP3")],
        [KeyboardButton("MP4")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=False)
    update.message.reply_text(f"Query: Choose a file format.", reply_markup=reply_markup)
    return STATE3_youtube

def STATE3_youtube_handler(update, context): 
    if update.message.text == "MP3":
        bot_send("You chose MP3")
    
    return ConversationHandler.END
    

    

if __name__ == '__main__':
    startup()

    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("standard", standard))

    # Youtube Handlers and states 
    STATE1_youtube, STATE2_youtube, STATE3_youtube = range(3)
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler("youtube", youtube)],
        states={
            STATE1_youtube: [MessageHandler(Filters.text, STATE1_youtube_handler)],
            STATE2_youtube: [MessageHandler(Filters.text, STATE2_youtube_handler)],
            STATE3_youtube: [MessageHandler(Filters.text, STATE3_youtube_handler)],
        },
        fallbacks = []
    ))
   


    # loop and making it closeable
    updater.start_polling()
    updater.idle()
