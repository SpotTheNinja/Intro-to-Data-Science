# top_ten.py
# takes a given twitter JSON file and outputs top ten hashtags by frequency
# written for Coursera Data Manipulation at Scale course
# 2016-04-03 LC
import sys
import json

def top_ten_hashtags(input_file):

    hashtag_dict = {}
    all_tweets = []
    for line in input_file:
        all_tweets.append(json.loads(line))

    for tweet in all_tweets:

        if 'entities' in tweet and tweet['entities']['hashtags']:
            for hashtag in tweet['entities']['hashtags']:

                if hashtag['text'] in hashtag_dict:
                    hashtag_dict[hashtag['text']] += 1
                else:
                    hashtag_dict[hashtag['text']] = 1

    hashtag_list = sorted(((value,key) for (key,value) in hashtag_dict.items()), reverse=True)

    for i in range(0,10):
        print hashtag_list[i][1].encode('utf-8') + " %d" % hashtag_list[i][0]




def main():

    tweet_file = open(sys.argv[1])
    top_ten_hashtags(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()

