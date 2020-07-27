import csv
import re

def read_csv(file_name):
    tweets = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            tweets.append(row)

        return tweets

def remove_links(tweets):
    regex = r"(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*"
    for tweet in tweets:
        tweet[4] = re.sub(regex, "", tweet[4])

    return tweets

def tweets_to_csv(tweets, file_name):
    with open(file_name, mode='w', newline="") as tweets_file:
        tweets_writer = csv.writer(tweets_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for tweet in tweets:
            tweets_writer.writerow(tweet)

def tweet_classifier(tweets):
    trump_keywords = ['trump', 'donald', 'republican']
    clinton_keywords = ['clinton', 'hillary', 'democrat']

    for tweet in tweets:
        trump = False
        clinton = False

        text = tweet[4]
        text = text.lower()
        for word in trump_keywords:
            if word in text:
                trump = True
        
        for word in clinton_keywords:
            if word in text:
                clinton = True
        
        tweet.append(trump)
        tweet.append(clinton)
    
    return tweets
