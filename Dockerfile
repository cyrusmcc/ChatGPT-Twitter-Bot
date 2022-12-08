FROM python:3.11

ADD .env .
ADD prompts.txt .
ADD tweets.txt .
ADD twitterscript.py .

RUN pip install tweepy datetime apscheduler openai python-dotenv

CMD ["python3", "./twitterscript.py"]