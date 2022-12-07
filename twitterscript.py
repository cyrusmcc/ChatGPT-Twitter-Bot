# Import the necessary libraries
import tweepy # for accessing the Twitter API
import schedule # for scheduling the tweets
import time # for adding delays
import openai # for using the OpenAI API
from dotenv import load_dotenv # for loading environment variables
load_dotenv() # load environment variables
import os # for accessing environment variables
import random

# Add your OpenAI API key here
#openai.organization = ""
openai.api_key = os.getenv("OPENAI_API_KEY")

# Add your Twitter API keys here
consumer_key = os.get
consumer_secret = ""
access_token = ""
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
    prompt = get_random_prompt()
    api.update_status(generate_text(prompt))

# Use the 'schedule' library to run the 'post_tweet' function
# every 2-5 hours
schedule.every(random.randint(120, 300)).minutes.do(post_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
