# import asyncio
# from twscrape import API, gather
# from twscrape.logger import set_log_level

# async def scrape():
#     api = API()
#     await api.pool.add_account("kit_kitapi", "13manaboy", "kit.tweetapi@gmail.com", "Kenzoku<3")
#     await api.pool.login_all()
#     user_id = 840052593690890240
#     scraper_list = await gather(api.user_tweets(user_id, limit=1, kv={"product": "Latest"}))
#     return scraper_list[:5]

# import tweepy

# # Replace these with your own credentials
# consumer_key = 'oMCXIHE86OlxpSgVF5VNDUkWz'
# consumer_secret = 'iWyIUIIX7uwK3ntuVwgECHDYkCff7Aafh0LOfPb1ZMRd5kQcHw'
# access_token = '783157230342246400-zrjAbjPAawOPtBeXyxlmfFfAKPkJ8ip'
# access_token_secret = '2c2MHL7WlaGDoKVQvzZ1NeR4Pho2TsTVFTnwkwgnGrkYY'
# bearer_token = 'AAAAAAAAAAAAAAAAAAAAALtnuAEAAAAAnRYY6zVDjQFQk4BNjGdH1cpX4O8%3DGaeawdPmj2i1qbuFgYGgdIF1jKIRz8Oz0XrhoQVbjYOOpGYDRv'

# # Authenticate to Twitter
# client = tweepy.Client(bearer_token=bearer_token)


# # Authenticate to Twitter
# auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
# api = tweepy.API(auth)

# # Example: Get the latest 10 tweets from a user's timeline
# username = 'granblue_en'
# user = client.get_user(username=username)
# user_id = user.data.id

# # Fetch the tweets from the user timeline
# tweets = client.get_users_tweets(user_id=user_id, max_results=5)

# for tweet in tweets.data:
#     print(f"User ID {user_id} said {tweet.text}")

# # Example: Search for tweets containing a specific hashtag
# # hashtag = '#example'

# for tweet in tweepy.Cursor(api.search_tweets, lang="en").items(5):
#     try:
#         print(f"{tweet.user.name} said {tweet.text}")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

