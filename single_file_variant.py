from google import genai
import dotenv
from typing import Final
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes


api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TELEGRAM_TOKEN")




def call_api(message):
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=message
    )
    return response.text

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text
    print(f"User said: {message_text}")  
    handle_response(message_text) 