from credenciales import *
import tweepy
# https://tweepy.readthedocs.io/en/v3.5.0/

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# For loop to iterate over tweets with #ocean, limit to 10
lista = ["usuarios-tuiter"]
for l in lista:
    user_data = api.get_user(l) 
    print "%s - %s" % (l, user_data['created_at'])
