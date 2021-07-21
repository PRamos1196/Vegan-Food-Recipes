from flask import Flask, render_template, request
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from collections import Counter
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import time
import tweepy as tw
import sys
import os
import random

dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)

consumer_key=os.environ['oauth_consumer_key']
consumer_secret=os.environ['oauth_consumer_secret']
access_token=os.environ['oauth_token']
access_token_secret=os.environ['oauth_token_secret']
spoon_api = os.environ["SPOON_API"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth, wait_on_rate_limit=True)


# declaring home page
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

# defining home page
def homepage():
    food_and_hashtag=[
        ['broccoli and chickpea rice salad','#chickpeasalad'],
        ['easy homemade rice and beans','#riceandbeans'],
        ['broccolini quinoa pilaf','#broccolini'],
        ['moroccan chickpea and lentil stew','#moroccan stew'],
        ['instant pot quinoa grain bow','#quinoa'],
        ['gulasch','#gulasch'],
        ['quinoa salad with barberries nut','#quinoa']
    ]
    
    randlist = random.choice(food_and_hashtag)
    # Define get_food_information() function to gather food data from spoonacular api, contians image of the food, title, and ID
    def get_food_information():
        food_link = f"https://api.spoonacular.com/recipes/complexSearch?query={randlist[0]}&apiKey={spoon_api}&number=1"
        food_data = requests.get(food_link)
        return food_data.json()
    
    
    food_detail_dictionary = get_food_information()
    food_id = food_detail_dictionary['results'][0]['id']
    response = f"https://api.spoonacular.com/recipes/{food_id}/information?apiKey={spoon_api}"
        
    # Define gather_ingredients() function to gather ingredients from suppossed food item, and use a list to store those ingredients
    # with there designated measurments and amounts
    def gather_ingredients():
        ingredients = requests.get(response)
        ingredients_extract = ingredients.json()
        ingredients_extended = ingredients_extract['extendedIngredients']
        list_of_ingredients = []
        for data in ingredients_extended:
            list_of_ingredients.append(data['originalString'])
        return list_of_ingredients
        
    def get_link_to_recipe_page():
        link = requests.get(response)
        link_extract = link.json()
        link_extended = link_extract['spoonacularSourceUrl']
        return link_extended
    
    def get_preptime():
        prep = requests.get(response).json()
        prep_time = prep['readyInMinutes']
        return prep_time
        
    
    food_prep_time = get_preptime()
    food_title = food_detail_dictionary['results'][0]['title']
    food_ingredients = gather_ingredients()
    food_link = get_link_to_recipe_page()
    food_photo = food_detail_dictionary['results'][0]['image']
    
    # Define tweet_list() function to gather tweets about said food item and ingredients, gathers:
    # author: screen name
    # post: Text post
    # date: month, day, year
    # and stores this information inside a list of tuples
    def tweet_list():
        tweets = []
        for tweet in Cursor(auth_api.search,q=randlist[1],count=10, lang='en',since='2018-09-26').items(10):
            author = tweet.user.screen_name
            tweet_post = tweet.text
            url = f"https://twitter.com/{tweet.user.screen_name}/status/{str(tweet.id)}"
            date_of_post = str(tweet.created_at)
            tweet_itself = author , tweet_post , date_of_post, url
            tweets.append(tweet_itself)
        return tweets
    random_tweet = random.choice(tweet_list())
    
    return render_template("index.html",food_prep_time = food_prep_time ,food_link = food_link ,food_photo = food_photo, food_id = food_id, food_title = food_title, len = len(food_ingredients), food_ingredients = food_ingredients, random_tweet = random_tweet)

if __name__ == "__main__":
 app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)