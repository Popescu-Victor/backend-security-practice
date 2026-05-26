import worldnewsapi
import dotenv
from wnapi_to_telegram import send_news



wn_token = dotenv.get_key(".env", "WNAPI")
search_topic = input("What topic are you interested in? ")



# Initial SDK configuration
newsapi_configuration = worldnewsapi.Configuration(api_key={'apiKey': wn_token})

try:
	newsapi_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(newsapi_configuration))

	max_results = 25   # replace with your maximum
	offset = 0
	all_results = []

	while len(all_results) < 3:

		request_count = min(100, max_results - len(all_results)) # request 100 or the remaining number of articles

		response = newsapi_instance.search_news(
			text=search_topic,
			language='en',
			sort="publish-time",
			sort_direction="desc",
			min_sentiment=-0.6,
			max_sentiment=0.6,
			offset=offset,
			number=request_count)

		print("Retrieved " + str(len(response.news)) + " articles. Offset: " + str(offset) + "/" + str(max_results) +
			  ". Total available: " + str(response.available) + ".")

		if len(response.news) == 0:
			break

		all_results.extend(response.news)
		offset += 100



except worldnewsapi.ApiException as e:
	print("Exception when calling NewsApi->search_news: %s\n" % e)

async def main():
	await send_news(all_results[0].title + "\n\n" + all_results[0].url)

if __name__ == "__main__":
	import asyncio
	asyncio.run(main())