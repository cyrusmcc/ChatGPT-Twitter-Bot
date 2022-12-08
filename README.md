# Openai-Twitter-Bot
 A basic python script which generates & posts tweets from Openai prompts.

## Obtain an OpenAPI API key
> OpenAPI consumes tokens to generate each tweet, you must posess token credits or add a payment option to your OpenAPI account to utilize these features. At current OpenAPI prices for davinci model, a dollar will generate ~700 tweets.

Visit [OpenAPI Account Keys](https://beta.openai.com/account/api-keys) to obtain a secret Key

Copy this key and use it to populate OPENAI_API_KEY in your .env file

## Obtain twitter bearer token
> You will need to obtain a personal bearer token. The Twitter API keys which come from Twitter's developer dashboard for projects & apps will not work

You may get the bearer token for your account(user account) by following the below link: [Twitter API Documentation](developer.twitter.com)

Click on “Try a live request” <br>
Click on three dots on the right-hand side. it will open up a window. <br>
Click on the “Include access token” button and it will show your bear token in your curl command.

Copy this token and use it to populate BEARER_TOKEN in your .env file


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