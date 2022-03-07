from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import Stream

import APICredentialsManager


class TwitterClient:
    def __init__(self, twitter_user=None):
        self.auth = authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


def authenticate_twitter_app():
    tokens = APICredentialsManager.get_credentials()
    auth = OAuthHandler(tokens[2], tokens[3])
    auth.set_access_token(tokens[0], tokens[1])
    return auth
