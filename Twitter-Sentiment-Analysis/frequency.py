# frequency.py
# calculates the frequency of a word in a tweet  over all the tweets in a given Twitter JSON file
# note that multiple usages of a word in a single tweet counts as one occurrence
# written for Coursera Data Manipulation at Scale course
# 2016-04-03 LC


import sys
import json
from urlparse import urlparse

def term_frequency(input_file):

    frequency = {} # initialize an empty dictionary
    all_tweets = []

    for line in input_file:
        all_tweets.append(json.loads(line))

    term_temp =[]
    total = 0
    for tweet in all_tweets:

        if 'text' in tweet and tweet["lang"] == 'en':
            term_temp[:] = []
            tweet_text = tweet['text']
            words = tweet_text.split()

            for word in words:
                lowercase_word = word.lower()
                # for terminal purposes
                encoded_lw = lowercase_word.encode('utf-8')

                # in twitter, skip all the directed responses and URLs
                if encoded_lw[0] != '@' and urlparse(encoded_lw)[0] == '':

                    # avoid duplicates in a tweet
                    if lowercase_word not in term_temp:
                        term_temp.append(lowercase_word)

            for term in term_temp:
                if term in frequency:
                    frequency[term] += 1
                else:
                    frequency[term] = 1

                total += 1

    for key,value in frequency.items():
        percent_frequency = value / float(total)
        print key.encode('utf-8') + " %.5f" % percent_frequency





def main():
    tweet_file = open(sys.argv[1])
    term_frequency(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()

