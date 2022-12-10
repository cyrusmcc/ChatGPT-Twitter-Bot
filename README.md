# Openai-Twitter-Bot
 A basic python script which generates & posts tweets from Openai prompts.

## Obtain an OpenAPI Auth
> ChatGPT is currently free to utilize but this may change in the future.

If you do not have an OpenAI account already, you will need to register one here [OpenAI](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBTYlpad0VuSDQyQ1c3d3Zoa2ZuZ0pqNktPQnBJTDJTOKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEh3WWN4Ylp0YzRaUTg4SlotSGJINDhRVlpRX2RnMUp1o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q)

Use your account email and password into to populate the  OPENAI_EMAIL and OPENAI_PASSWORD fields in your .env file

## Obtain twitter keys

You can access your Twitter API keys through the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard). If you haven't used this platform before you will need to create a project once you've registered an account. 

Once you've registered a project, navigate to the Twitter Developers dashboard homepage <br>
Look for your project under the Apps section and click the key icon on your project <br>
Generate your Consumer(API) key and secret <br>
Copy these values and use them to populate the TWITTER_API_KEY and TWITTER_API_KEY_SECRET entries in your .env file <br>


Under the Authentication Tokens section, generate an Access Token and Secret <br>
Copy these values and use them to populate the TWITTER_ACCESS_TOKEN and TWITTER_ACCESS_TOKEN_SECRET entires in your .env file.


## How to use

This script will use prompts generated in **prompts.py** to generate tweets which will be posted to your twitter account in random intervals between 2-6 hours of length. Prompts are composed of a *prompt_start* value which provides a proposition, a *topic*, a *wildcard*, an *attribute*, and a *constraint*. You will need to provide values in these fields to utilze the bot.


### Example of a prompt created from the above fields
>  give me a tweet asking a question about WebGL using multiple relevant hashtags using lower case letters in less than 280 characters

### The resulting tweet
> Are there any good tutorials for learning #webgl from scratch? Looking to dive in and create some cool 3D graphics. #gamedev #javascript #3d

Add as many prompts or additional input fields as you like to this file and execute the program. An output log will be kept in **tweets.txt**

### Execute the program
> python3 twitterbot.py


## Creating a docker container
A docker file is provided if you wish to run your bot in a docker container. To create a docker image from the directory which contains this twitter bot

### Execute in a terminal
> docker build -t openapi-twitter-bot .

This will create a docker image which can then be used to instantiate a docker container.

### Run a docker container
> docker run -t --name=openapi-twitter-bot-container -p replace-with-your-local-ip:8080:80 openapi-twitter-bot
