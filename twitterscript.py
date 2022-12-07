# Import the necessary libraries
import tweepy # for accessing the Twitter API
from datetime import datetime # for getting the current date and time
from apscheduler.schedulers.blocking import BlockingSchedulerimport # for adding delays
import openai # for using the OpenAI API
from dotenv import load_dotenv # for loading environment variables
load_dotenv() # load environment variables
import os # for accessing environment variables
import random

# Add your OpenAI API key here
#openai.organization = ""
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Add your Twitter API keys here
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = ""

# Authenticate the API keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

def get_random_prompt():
    with open("prompts.txt", "r") as f:
        prompts = f.readlines()
        prompt = random.choice(prompts)
        return prompt

def generate_text(prompt, max_tokens=70):
    text = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens, # 1 token = 4 characters, so 70 tokens = 280 characters (the max length of a tweet)
        temperature=0.4, # temperature is a measure of randomness
        top_p=1, # top_p is the probability of choosing the next word
        frequency_penalty=0, # frequency_penalty is the probability of repeating a word
        presence_penalty=0 # presence_penalty is the probability of repeating a word
    )
    return text

# Function that posts a tweet
def post_tweet():
    print("Posting tweet...")
    prompt = get_random_prompt()
    api.update_status(generate_text(prompt))

# Schedule the function to run every 2-6 hours
sched = BlockingScheduler()
sched.add_job(post_tweet, 'interval', hours=4, jitter=7200)
sched.start()