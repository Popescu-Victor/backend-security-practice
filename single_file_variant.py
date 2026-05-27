from google import genai
import dotenv
from typing import Final
from telegram.ext import ApplicationBuilder, MessageHandler, filters


api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
TOKEN: Final = dotenv.get_key(dotenv.find_dotenv(), "TOKEN")
context = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_CONTEXT")




def call_api(message):
    message = f"{context}\n\nUser: {message}"
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=message
    )
    return response.text

async def handle(update, ctx):
    message = update.message.text
    response = call_api(message)
    await ctx.bot.send_message(chat_id=update.message.chat.id, text=response)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle))
app.run_polling()
