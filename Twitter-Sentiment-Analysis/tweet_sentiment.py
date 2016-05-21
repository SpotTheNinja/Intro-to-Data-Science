# tweet_sentiment.py
# calculates sentiment_score using AFINN-111 , a compiled list of words and corresponding sentiment score
# written for Coursera Data Manipulation at Scale course
# 2016-04-03 LC


import sys
import json

def tweet_sentiment_score(afinnfile, input_file):


    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    all_tweets = []
    for line in input_file:
        all_tweets.append(json.loads(line))

    for tweet in all_tweets:
        sentiment_score = 0

        if 'text' in tweet and 'lang' in tweet:
            if tweet["lang"]=='en':
                tweet_text = tweet['text']
                words = tweet_text.split()

                for word in words:
                    lowercase_word = word.lower()
                    if lowercase_word in scores:
                        sentiment_score += scores[lowercase_word]

        print sentiment_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet_sentiment_score(sent_file, tweet_file)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()

