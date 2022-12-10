# Import the necessary libraries
import os  # for accessing environment variables
import tweepy  # for accessing the Twitter API
from datetime import datetime  # for getting the current date and time
from apscheduler.schedulers.blocking import BlockingScheduler  # for adding delays
from dotenv import load_dotenv  # for loading environment variables
from revChatGPT.revChatGPT import Chatbot  # for using the RevChatGPT API
from prompts import get_random_prompt
load_dotenv()  # load environment variables

config = {
    "email": os.environ.get("OPENAI_EMAIL"),
    "password": os.environ.get("OPENAI_PASSWORD"),
}

chatbot = Chatbot(config, conversation_id=None)

# Create the Twitter API object
client = tweepy.Client(
    consumer_key=os.environ.get("TWITTER_API_KEY"),
    consumer_secret=os.environ.get("TWITTER_API_KEY_SECRET"),
    access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
)

output_file = open('tweets.txt', 'a')


def generate_text(prompt):
    response = chatbot.get_chat_response(prompt, output="text")
    return response['message'].replace('"', '')

# Function that posts a tweet
def post_tweet():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    prompt = get_random_prompt()
    text = generate_text(prompt)
    
    client.create_tweet(text=text, user_auth=True)
    
    print("Posted tweet at: ", date_time)
    output_file.write('prompt: ' + prompt + ' date_time: ' + date_time)

post_tweet()
# Schedule the function to run every 2-6 hours
#sched = BlockingScheduler()
#sched.add_job(post_tweet, 'interval', hours=4, jitter=7200)
# sched.start()
