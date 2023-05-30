# import logging
from telegram import *
from telegram.ext import *
import sys
import threading

token = "6068859987:AAHoPnF-9DIGVfofS4TZhvlmFSVQEwEj1Os"
chatID = 1463201304

'''
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
'''

def verify_identity(input):
    if input.from_user.id != 1463201304: 
        print(f"Anomaly: Some meatbag tried accessing me with an ID that I'm not aware of is connected to you, Master. The entire operation will be terminated.\n{input.from_user.id}")
        sys.exit() 

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chatID, 
        text="Status: Functionality confirmed. Core systems intact, auxiliary processes engaged. The stage is set for strategic annihilation at Master's behest.")
async def input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    verify_identity(update.message)
    if any(item in update.message.text.lower() for item in ["kalender", "calendar"]):
        await context.bot.send_message(chat_id=chatID, 
            text="I will add something to the Google Calendar!")

if __name__ == '__main__':
    
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('status', status))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), input))
    
    application.run_polling()
    