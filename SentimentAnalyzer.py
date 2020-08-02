from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from TweetCleaner import read_csv

def sentimentAnalyzer(tweets):
    analyser = SentimentIntensityAnalyzer()
    for tweet in tweets:
        sentiment = analyser.polarity_scores(tweet[4])
        tweet.append(sentiment)

    return tweets

