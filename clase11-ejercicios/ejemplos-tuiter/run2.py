from credenciales import *
import tweepy
import codecs

# https://tweepy.readthedocs.io/en/v3.5.0/

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# For loop to iterate over tweets with #ocean, limit to 10
lista = ['CarlosC62169047', 'djosuejj', 'pedrojsalinas', 'fernandogdo1']
for l in lista:
    archivo = codecs.open('%s.csv' %l, 'w', encoding='utf-8')
    archivo.write('%s|%s|%s|%s|%s|%s\n'%('name','screen_name','followers_count','friends_count', 'listed_count', 'favourites_count'))
    informacion = api.followers(l)
    for x in informacion['users']:
    	datos = {'followers_count': x['followers_count'], 'listed_count': x['listed_count'], 'friends_count': x['friends_count'],
    	'screen_name': x['screen_name'], 'favourites_count': x['favourites_count'], 'name': x['name'], 'created_at': x['created_at'] }
    	archivo.write('{name}|{screen_name}|{followers_count}|{friends_count}|{listed_count}|{favourites_count}|\n'.format(** datos))
    archivo.close()
    







