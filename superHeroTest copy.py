import requests
import tweepy
import random

CONSUMER_KEY ="###################"
CONSUMER_SECRET = "############################"
ACCESS_KEY = "####################################"
ACCESS_SECRET = "######################################"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET )
api = tweepy.API(auth)

url = "https://superhero-search.p.rapidapi.com/"
randomNumber = random.randint(1,564)
querystring = {"id":randomNumber ,"name": "","fullName": "","publisher": ""}

headers = {
    'x-rapidapi-host': "superhero-search.p.rapidapi.com",
    'x-rapidapi-key': "########################################"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
response.text

name = data["name"]
fullName = data["biography"]["fullName"]
aliases = data["biography"]["aliases"]
firstAppearance = data["biography"]["firstAppearance"]
publisher = data["biography"]["publisher"]
api.update_status("Random Comicbook Character. Character Name: %s Full Name: %s Aliases: %s First Appearance in a comicbook: %s Publisher: %s" % (name,fullName,aliases,firstAppearance,publisher))
