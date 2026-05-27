from typing import Final
import dotenv
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes
from fastapi import FastAPI
import sqlalchemy as sa
import json
import requests
import worldnewsapi


TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TELEGRAM_TOKEN")
WN_TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "WNAPI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I am accute bot!")

async def first_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("This is the first message!")

def handle_response(text: str) -> str:
    text = text.lower()
    print(text)  
    return text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    print(f"User said: {message_text}")  
    handle_response(message_text)        
    
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()



def search_news():
    wn_topic = input("What topic are you interested in? ")


    response = newsapi_instance.search_news(
    text= wn_topic,
    language='en',
    sort="publish-time",
    sort_direction="desc",
    min_sentiment=-0.8,
    max_sentiment=0.8,
    offset=offset)