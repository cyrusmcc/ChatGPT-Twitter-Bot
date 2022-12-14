# ChatGPT-Twitter-Bot
 A basic bot which posts tweets generated from ChatGPT prompts utilizing [revChatGPT](https://github.com/acheong08/ChatGPT), a third party ChatGPT API. OpenAI is actively trying to circumvent bot activity on ChatGPT which is resulting in a lot of instability with this API. This bot may break or cease to function often. Once an official API is available for ChatGPT this repository will be updated to utilize it. 

## ChatGPT auth

This project is utilzing a third party ChatGPT API which requires workarounds for OpenAI's Cloudflare protections. You will need Firefox/Chrome intalled.When executing this application a browser will open and you will need to login to OpenAI with your account information.


If you do not have an OpenAI account already, you will need to register one here [OpenAI](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBTYlpad0VuSDQyQ1c3d3Zoa2ZuZ0pqNktPQnBJTDJTOKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEh3WWN4Ylp0YzRaUTg4SlotSGJINDhRVlpRX2RnMUp1o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q)


## Obtain twitter keys

You can access your Twitter API keys through the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard). If you haven't used this platform before you will need to create a project once you've registered an account. 

Once you've registered a project, navigate to the Twitter Developers dashboard homepage <br>
Look for your project under the Apps section and click the key icon on your project <br>
Generate your Consumer(API) key and secret <br>
Copy these values and use them to populate the TWITTER_API_KEY and TWITTER_API_KEY_SECRET entries in your .env file <br>


Under the Authentication Tokens section, generate an Access Token and Secret <br>
Copy these values and use them to populate the TWITTER_ACCESS_TOKEN and TWITTER_ACCESS_TOKEN_SECRET entires in your .env file.


## How to use

This script will use prompts generated in **prompts.py** to generate tweets which will be posted to your twitter account in random intervals between 2-6 hours of length. Prompts are composed of a prompt template, a topic, a list of attributes, a wildcard, and a list of constraints. Example values can be found in prompts.json and additional properties can be added here. 

### Example of a prompt created from the above fields
Without values
> Describe {topic} from a unique perspective or angle. {attributes}. {wildcard}. {constraints}.

With values
>  Describe chatgpt from a unique perspective or angle. Use an informal tone, use relaxed punctuation. Mention a specific company. Write your response as a tweet with at most 280 characters.

### The resulting tweet
![image](https://user-images.githubusercontent.com/61042997/208254767-da32936d-a736-449a-abff-71fc94f4fd59.png)


Add as many prompts or additional input fields as you like to this file and execute the program. An output log will be kept in **tweets.txt**

### Execute the program
> python3 twitterbot.py


## Creating a docker container
> NOTE: Cloudflare protections have made the Dockerfile unusable at the moment, I will need to do some testing with the new revChatGPT workarounds to get this to work. 

A docker file is provided if you wish to run your bot in a docker container. To create a docker image from the directory which contains this twitter bot

### Execute in a terminal
> docker build -t chatgpt-twitter-bot .

This will create a docker image which can then be used to instantiate a docker container.

### Run a docker container
> docker run -t --name=chatgpt-twitter-bot-container -p replace-with-your-local-ip:8080:80 chatgpt-twitter-bot
