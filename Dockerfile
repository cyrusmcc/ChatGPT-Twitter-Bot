FROM python:3.11

ADD .env .
ADD prompts.py .
ADD tweets.txt .
ADD twitterscript.py ./src/twitterscript.py

RUN pip install tweepy datetime apscheduler openai python-dotenv revChatGPT

CMD ["python3", "./twitterscript.py"]