import threading

import pandas

from Twitter import *

import pandas as pd
import numpy as np
import tweepy


class Processor(threading.Thread):
    def __init__(self, analysis_window):
        super().__init__()
        self.analysisWindow = analysis_window

    def set_progress(self, msg):
        self.analysisWindow.processing_text.set(msg)

    def run(self):
        try:
            self.process()
        except IndexError as e:
            print(e)
        self.analysisWindow.processing_done()

    def process(self):
        self.set_progress("Authenticating client...")
        twitter_client = TwitterClient()

        api = twitter_client.get_twitter_client_api()

        self.set_progress("Getting tweets...")

        # tweets = api.user_timeline(screen_name=self.analysisWindow.username[1:], count=self.analysisWindow.tweet_count)

        tweets = []

        double_break = False

        for pages in tweepy.Cursor(api.user_timeline, count=200, screen_name=self.analysisWindow.username[1:]).pages():
            self.set_progress(f"Tweets: {len(tweets)}")
            for tweet in pages:
                tweets.append(tweet)
                if len(tweets) >= self.analysisWindow.tweet_count:
                    double_break = True
                    break
            if double_break:
                break

        self.set_progress("Processing tweets...")
        self.df = self.tweets_to_data_frame(tweets)

        # l = [tweet.favorite_count for tweet in tweets]
        # r = [tweet.retweet_count for tweet in tweets]
        # _id = [tweet.id for tweet in tweets]
        # txt = [tweet.text for tweet in tweets]

        self.set_progress("Done")

    def tweets_to_data_frame(self, in_tweets: list) -> pandas.DataFrame:
        tweets = []

        if not self.analysisWindow.use_retweets:
            for tweet in in_tweets:
                if not hasattr(tweet, "retweeted_status"):
                    tweets.append(tweet)
        else:
            tweets = in_tweets

        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])

        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['is_retweet'] = np.array([hasattr(tweet, "retweeted_status") for tweet in tweets])

        df['x'] = np.array(self.analysisWindow.axis[0].get_list(df))
        df['y'] = np.array(self.analysisWindow.axis[1].get_list(df))

        return df
