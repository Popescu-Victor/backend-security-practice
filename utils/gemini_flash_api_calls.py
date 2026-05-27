from google import genai
import dotenv


api_key = dotenv.get_key(dotenv.find_dotenv(), "GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Did this api call work?"
)

print(response.text)