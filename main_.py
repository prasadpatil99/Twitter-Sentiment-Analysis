# Importing Libraries
import tweepy
from textblob import TextBlob

# Keys and Tokens
consumer_key = 'WgjRmUXX8BoThbDrDnfQbOEGV'
consumer_secret = 'wPGxE2J5KL5u0D3geZFawIAk2TuZSG37ov0DRk04E6xpwZqSuH'
access_token ='1121720100959084544-SPNB1CFfypRfi329u4hitaAPVx7raq'
access_token_secret = 'lVrZMC7QZ2FQCSaYwpgvFJDwJcX09jLeFq9dknccLL7vF'

# Authenticating Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Searching For a Subject
public_tweets = api.search('Artificial Intelligence')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
