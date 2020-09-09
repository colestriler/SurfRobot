import tweepy
import logging
import os

logger = logging.getLogger()

#Temporary
DEV=True

def create_api():
    # Use Test Configs if Running Locally
    if os.getenv("DEVELOPMENT") == "True" and DEV==True:
        consumer_key = os.getenv("TESTING_CONSUMER_KEY")
        consumer_secret = os.getenv("TESTING_CONSUMER_SECRET")
        access_token = os.getenv("TESTING_ACCESS_TOKEN")
        access_token_secret = os.getenv("TESTING_ACCESS_TOKEN_SECRET")
    else:
        consumer_key = os.getenv("SURFROBOT_CONSUMER_KEY")
        consumer_secret = os.getenv("SURFROBOT_CONSUMER_SECRET")
        access_token = os.getenv("SURFROBOT_ACCESS_TOKEN")
        access_token_secret = os.getenv("SURFROBOT_ACCESS_TOKEN_SECRET")



    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api


a = create_api()