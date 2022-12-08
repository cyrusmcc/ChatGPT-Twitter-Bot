# Import the necessary libraries
import random  # random time interval
import os  # for accessing environment variables
import tweepy  # for accessing the Twitter API
from datetime import datetime  # for getting the current date and time
from apscheduler.schedulers.blocking import BlockingScheduler # for adding delays
import openai  # for using the OpenAI API
from dotenv import load_dotenv  # for loading environment variables
load_dotenv()  # load environment variables

# Add your OpenAI API key here
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Add your Twitter bearer token here
bearer_token = os.environ.get('BEARER_TOKEN')

# Create the API object
api = tweepy.Client(bearer_token=bearer_token)

output_file = open('tweets.txt', 'a')

def get_random_prompt():
    with open("prompts.txt", "r") as f:
        prompts = f.readlines()
        prompt = random.choice(prompts)
        return prompt


def generate_text(prompt, max_tokens=70):
    result = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        # 1 token = 4 characters, so 70 tokens = 280 characters (the max length of a tweet)
        max_tokens=max_tokens,
        temperature=0.4,  # temperature is a measure of randomness
        top_p=1,  # top_p is the probability of choosing the next word
        frequency_penalty=0,  # frequency_penalty is the probability of repeating a word
        presence_penalty=0  # presence_penalty is the probability of repeating a word
    )

    text = result.choices[0]['text'].replace('\n', 'n').replace('n#', '')
    return text

# Function that posts a tweet
def post_tweet():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("Posting tweet at: ", date_time)
    prompt = get_random_prompt()
    text = generate_text(prompt)
    output_file.write('prompt: ' + prompt + ' tweet: ' + text + 'date_time: ' + date_time)
    api.create_tweet(text=text, user_auth=False)


# Schedule the function to run every 2-6 hours
sched = BlockingScheduler()
sched.add_job(post_tweet, 'interval', hours=4, jitter=7200)
sched.start()
