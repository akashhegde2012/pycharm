import tweepy
import time
auth = tweepy.OAuthHandler('2HIKf5bsozok5wmQbFYlsBGr6', 'OWJrzaUujRhaiUr5uF6JELpIJDxBrUFHdaTcv4Kpu4QpQKUEbM')
auth.set_access_token('1190116292520361985-BFLBenNHauzU1rUcmuJyVsOEc8LDAK','DKSmOT9fflRMcK7jpyBeGm2tCDed8ZFoKxaDHPjetsx55')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
api=tweepy.API(auth)
user=api.me()

def limit_handeler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError :
        time.sleep(1000)

search_string='Narendra Modi'
numbersOfTweets=2

for tweet in tweepy.Cursor(api.search,search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break





#
# # generous bot
# for follower in limit_handeler(tweepy.Cursor(api.followers).items()):
#     if follower.name=='Manish V':
#         follower.follow()