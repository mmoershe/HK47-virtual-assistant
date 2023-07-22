from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto     
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, InlineQueryHandler, CallbackQueryHandler, CallbackContext, Filters
from pytube import YouTube
from bs4 import BeautifulSoup
from beautiful_date import * 
from dateutil import parser
import logging, os, sys, json, random, time, requests, pyautogui


# This project is using Python Telegram Bot v13.7, because the newer v20.3 uses asyncio and is super ANNOYING!!!

current_path = os.path.dirname(os.path.abspath(__file__))
json_file = open(os.path.join(current_path, "memory", "memory.json"), "r")
json_data = json.load(json_file)
token = json_data["token"]
chatID = json_data["chatID"]
updater = Updater(token = token, use_context=True)
dispatcher = updater.dispatcher
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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

def bot_send(message, reply_markup=None, image_path=None): 
    if not image_path:
        updater.bot.send_message(chat_id = chatID, text = message, reply_markup = reply_markup)
        print("\t--------------", f"\t{message}", "\t--------------", sep="\n\n")
        return 
    updater.bot.sendMediaGroup(chat_id=chatID, media=[InputMediaPhoto(media=open(image_path, "rb"), caption=message)])
    print("\t--------------", f"\t{image_path}\n\tcaption: {message}", "\t--------------", sep="\n\n")



def startup():
    print("Bot has been started")
    startup_message = get_random_sentence("startup")
    bot_send(startup_message)

def stop(update: Update, context: CallbackContext):
    bot_send(json_data["stop"][random.randint(0, len(json_data["stop"])-1)])
    print("Bot is shutting down.")
    os._exit(0)

def status(update: Update, context: CallbackContext):
    verify_user(update.message)
    screenshot_path = os.path.join(current_path, "memory", "temporary_image.png")
    pyautogui.screenshot(screenshot_path)
    bot_send(f"Status: Functionality confirmed.\n\n{sys.version}", image_path=screenshot_path)
    os.remove(screenshot_path)
    
def standard(update: Update, context: CallbackContext):
    stopbutton = [[InlineKeyboardButton("STOP", callback_data="timer_stop")]]
    bot_send("meine caption", image_path=os.path.join(current_path, "memory", "testimage.jpg"))

# COMICS
def comics(update: Update, context: CallbackContext):
    def tableDataText(table):    
        """Parses a html segment started with tag <table> followed 
        by multiple <tr> (table rows) and inner <td> (table data) tags. 
        It returns a list of rows with inner columns. 
        Accepts only one <th> (table header/data) in the first row.
        """
        def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
            return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
        rows = []
        trs = table.find_all('tr')
        headerow = rowgetDataText(trs[0], 'th')
        if headerow: # if there is a header row include first
            rows.append(headerow)
            trs = trs[1:]
        for tr in trs: # for every table row
            rows.append(rowgetDataText(tr, 'td') ) # data row       
        return rows

    def convertToBeautifulDate(date):
        if not isinstance(date, str):
            print(f"convertToBeautifulDate() has received a {type(date) = } instead of a String.")
            return
        try: 
            parsed_date = parser.parse(date)
            return BeautifulDate(parsed_date.year, parsed_date.month, parsed_date.day)
        except: 
            return 


    url = "https://starwars.fandom.com/wiki/List_of_future_comics"
    html = requests.get(url, auth=("user", "pass")).text
    future_swcomics_html = BeautifulSoup(html, "html.parser")
    table = future_swcomics_html.find(id="prettytable")
    table = tableDataText(table)
    table.pop(0)
    current_date = D.today()
    date_range = []
    for i in range(7):
        date_range.append(current_date+i*days)

    bot_send("Statement: In the next 7 days the following comics will be released:")
    for row in table:
        title= row[0]
        type_comic = "Issue" if row[1].lower() == "comic book" else row[1].title()
        publish_date = convertToBeautifulDate(row[2])
        if not all([title, type_comic, publish_date]): 
            continue
        if publish_date in date_range: 
            bot_send(f"{type_comic}: {title} [{weekdays[publish_date.weekday()][:3]}]")


def calendar(update: Update, context: CallbackContext):
    bot_send("calendar has been triggered.")


# TIMER 
TIMER_start = None
def timerstart(update: Update, context: CallbackContext):
    global TIMER_start
    if TIMER_start:
        bot_send("Rectification: The timer has already been started. Did you perhaps try to end the timer?\n/timerend")
        return
    TIMER_start = D.now()
    stopbutton = [[InlineKeyboardButton("STOP", callback_data="timer_stop")]]
    bot_send(f"Statement: You started the timer @{TIMER_start}.", InlineKeyboardMarkup(stopbutton))
def timerend(update: Update, context: CallbackContext):
    global TIMER_start
    if not TIMER_start: 
        bot_send("Rectification: The timer hasn't been started, thus cannot end. Did you perhaps try to start the timer?\n/timerstart")
        return
    bot_send(f"Statement: Timer has been stopped.\n\nResult: {D.now()-TIMER_start}\nStarttime: {TIMER_start}\nEndtime: {D.now()}\n\nStatus: I'm not yet programmed to save and archive your result.")
    TIMER_start = None
def timerterminate(update: Update, context: CallbackContext):
    global TIMER_start
    if not TIMER_start:
        bot_send("Rectification: The timer isn't running right now, thus cannot be terminated.")
        return
    TIMER_start = None
    bot_send("Statement: The timer has been terminated. You may start a new timer now:\n/timerstart")

# Query Handler
def queryhandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    if query == "timer_stop":
        timerend(Update, CallbackContext)


if __name__ == '__main__':
    startup()

    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("standard", standard))
    dispatcher.add_handler(CommandHandler("comics", comics))
    dispatcher.add_handler(CommandHandler("timerstart", timerstart))
    dispatcher.add_handler(CommandHandler("timerend", timerend))
    dispatcher.add_handler(CommandHandler("timerterminate", timerterminate))

    dispatcher.add_handler(CallbackQueryHandler(queryhandler))


    # loop and making it closeable
    updater.start_polling()
    updater.idle()
