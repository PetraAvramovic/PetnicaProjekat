from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analyzer(tweets):
    analyser = SentimentIntensityAnalyzer()
    for tweet in tweets:
        sentiment = analyser.polarity_scores(tweet[4])
        tweet.append(sentiment)

    return tweets