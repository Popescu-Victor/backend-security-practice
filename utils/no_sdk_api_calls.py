import httpx
import dotenv
import asyncio
from wnapi_to_telegram import send_news

wn_token = dotenv.get_key(".env", "WNAPI")
search_topic = input("What topic are you interested in? ")

BASE_URL = "https://api.worldnewsapi.com/search-news"

async def fetch_news():
    all_results = []
    offset = 0
    max_results = 25

    async with httpx.AsyncClient() as client:
        while len(all_results) < 3:
            request_count = min(100, max_results - len(all_results))

            response = await client.get(
                BASE_URL,
                params={
                    "text": search_topic,
                    "language": "en",
                    "sort": "publish-time",
                    "sort-direction": "desc",
                    "min-sentiment": -0.6,
                    "max-sentiment": 0.6,
                    "offset": offset,
                    "number": request_count,
                },
                headers={"x-api-key": wn_token}
            )

            response.raise_for_status()
            data = response.json()
            articles = data.get("news", [])

            print(f"Retrieved {len(articles)} articles. Offset: {offset}/{max_results}.")

            if not articles:
                break

            all_results.extend(articles)
            offset += 100

    return all_results


async def main():
    all_results = await fetch_news()
    article = all_results[0]
    await send_news(article["title"] + "\n\n" + article["text"])

if __name__ == "__main__":
    asyncio.run(main())