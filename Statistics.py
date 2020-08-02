from TweetCleaner import *
from SentimentAnalyzer import *
import ast
import operator

def countSentiments(file_name):
    positive = 0
    negative = 0
    neutral = 0

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            sentiment = ast.literal_eval(row[13])
            if sentiment['compound'] > 0.05:
                positive += 1
            elif sentiment['compound'] < -0.05:
                negative += 1
            else:
                neutral += 1

        return (positive, negative, neutral)

def countMentions(file_name):
    trumpCounter = 0
    clintonCounter = 0
    bothCounter = 0

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:     
            if row[11] == "True" and row[12] == "True":
                bothCounter += 1
            elif row[11] == "True":
                trumpCounter += 1
            else:
                clintonCounter += 1

        return (bothCounter, trumpCounter, clintonCounter)

mentions = (0, 0, 0)
clintonSentiments = (0, 0, 0)
trumpSentiments = (0, 0, 0) 

for i in range(8, 32):
    date = str(i)

    mentions = tuple(map(operator.add, mentions, countMentions("clinton" + date + "october1.csv")))
    clintonSentiments = tuple(map(operator.add, clintonSentiments, countSentiments("clinton" + date + "october1.csv")))

    mentions = tuple(map(operator.add, mentions, countMentions("trump" + date + "october1.csv")))
    trumpSentiments = tuple(map(operator.add, trumpSentiments, countMentions("trump" + date + "october1.csv")))
    
    

for i in range(1, 9):
    date = str(i)

    mentions = tuple(map(operator.add, mentions, countMentions("clinton" + date + "november1.csv")))
    clintonSentiments = tuple(map(operator.add, clintonSentiments, countSentiments("clinton" + date + "november1.csv")))

    mentions = tuple(map(operator.add, mentions, countMentions("trump" + date + "november1.csv")))
    trumpSentiments = tuple(map(operator.add, trumpSentiments, countMentions("trump" + date + "november1.csv")))


print(mentions)
print(trumpSentiments)
print(clintonSentiments)
