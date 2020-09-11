import tweepy
import logging
import os

logger = logging.getLogger()

class API():
    def __init__(self):
        if os.getenv("DEVELOPMENT") == "True":
            self.consumer_key = os.getenv("TESTING_CONSUMER_KEY")
            self.consumer_secret = os.getenv("TESTING_CONSUMER_SECRET")
            self.access_token = os.getenv("TESTING_ACCESS_TOKEN")
            self.access_token_secret = os.getenv("TESTING_ACCESS_TOKEN_SECRET")
            self.delete_all = True
            self.unfollow_all = True
        else:
            self.consumer_key = os.getenv("SURFROBOT_CONSUMER_KEY")
            self.consumer_secret = os.getenv("SURFROBOT_CONSUMER_SECRET")
            self.access_token = os.getenv("SURFROBOT_ACCESS_TOKEN")
            self.access_token_secret = os.getenv("SURFROBOT_ACCESS_TOKEN_SECRET")
            self.delete_all = False
            self.unfollow_all = False

    def create_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
        logger.info("API created")
        return api

