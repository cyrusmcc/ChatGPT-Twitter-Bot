# Openai-Twitter-Bot
 A basic python script which generates & posts tweets from Openai prompts.

## Obtain an OpenAPI API key
> OpenAPI consumes tokens to generate each tweet, you must posess token credits or add a payment option to your OpenAPI account to utilize these features. At current OpenAPI prices for davinci model, a dollar will generate ~700 tweets.

Visit [OpenAPI Account Keys](https://beta.openai.com/account/api-keys) to obtain a secret Key

Copy this key and use it to populate OPENAI_API_KEY in your .env file

## Obtain twitter keys

You can access your Twitter API keys through the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard). If you haven't used this platform before you will need to create a project once you've registered an account. 

Once you've registered a project, navigate to the Twitter Developers dashboard homepage <br>
Look for your project under the Apps section and click the key icon on your project <br>
Generate your Consumer(API) key and secret <br>
Copy these values and use them to populate the TWITTER_API_KEY and TWITTER_API_KEY_SECRET entries in your .env file <br>


Under the Authentication Tokens section, generate an Access Token and Secret <br>
Copy these values and use them to populate the TWITTER_ACCESS_TOKEN and TWITTER_ACCESS_TOKEN_SECRET entires in your .env file.


## How to use

This script will use prompts placed in **prompts.txt** to generate tweets which will be posted to your twitter account in random intervals between 2-6 hours of length.

### Example of a prompt to place inside prompts.txt
> Give me a tweet idea with hashtags which asks a witty question`

Add as many prompts as you like this this file and execute the program. An output log will be kept in **tweets.txt**

### Execute the program
> python3 twitterbot.py


## Creating a docker container
A docker file is provided if you wish to run your bot in a docker container. To create a docker image from the directory which contains this twitter bot

### Execute in a terminal
> docker build -t openapi-twitter-bot .

This will create a docker image which can then be used to instantiate a docker container.

### Run a docker container
> docker run -t --name=openapi-twitter-bot-container -p replace-with-your-local-ip:8080:80 openapi-twitter-bot
