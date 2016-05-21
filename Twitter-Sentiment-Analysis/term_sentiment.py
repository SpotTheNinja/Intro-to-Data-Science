# term_sentiment.py
# uses words with assigned sentiment score and assigns values to non-assigned words
# calculates sentiment_score using AFINN-111 , a compiled list of words and corresponding sentiment score
# written for Coursera Data Manipulation at Scale course
# 2016-04-03 LC

import sys
import json
from urlparse import urlparse

def term_sentiments_score(afinnfile, input_file):

    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    all_tweets = []
    for line in input_file:
        all_tweets.append(json.loads(line))

    term_sentiments = {}
    term_temp = []
    for tweet in all_tweets:
        sentiment_score = 0

        if 'text' in tweet and 'lang' in tweet:
            if tweet["lang"]=='en':
                term_temp[:] = []
                tweet_text = tweet['text']
                words = tweet_text.split()

                for word in words:
                    lowercase_word = word.lower()
                    # for terminal purposes
                    encoded_lw = lowercase_word.encode('utf-8')

                    if lowercase_word in scores:
                        sentiment_score += scores[lowercase_word]

                    # in twitter, skip all the directed responses and URLs
                    elif encoded_lw[0] != '@' and urlparse(encoded_lw)[0] == '':

                        term_temp.append(lowercase_word)

                for terms in term_temp:
                    # key value pair is in the form of term: [sum sentiment_score, count]
                    # sentiment_score sum will be averaged over count afterwards
                    if terms in term_sentiments:
                        score = term_sentiments[terms][0]
                        count = term_sentiments[terms][1]
                        score += sentiment_score
                        count += 1
                        term_sentiments[terms] = [score,count]

                    else:
                        term_sentiments[terms] =[sentiment_score,1]

    for key, value in term_sentiments.items():
        term_score = value[0] / float(value[1])

        print key.encode('utf-8') + " %.3f" % term_score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    term_sentiments_score(sent_file,tweet_file)

    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()

# calculate sentiment score of whole tweet
# take remaining words in tweet and assign them the same score
# add that to their value in the dictionary
# also add the count so probably a list as the value

