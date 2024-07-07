# import asyncio
# from twscrape import API, gather
# from twscrape.logger import set_log_level

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

