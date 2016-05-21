# happiest_state.py
# finds the state with the highest average sentiment score given a twitter JSON file
# calculates sentiment_score using AFINN-111 , a compiled list of words and corresponding sentiment score
# written for Coursera Data Manipulation at Scale course
# 2016-04-03 LC


import sys
import json


def happiest_state_finder(afinnfile, input_file):

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    all_tweets = []

    for line in input_file:
        all_tweets.append(json.loads(line))


    state_happiness = {}


    for tweet in all_tweets:
        sentiment_score = 0

        # to avoid None values
        if 'place' in tweet and tweet['place'] is not None and tweet['place']['country_code'] == 'US':
            if tweet['place']['full_name'] is not None:

                locations = [full_name.strip() for full_name in tweet['place']['full_name'].split(',')]



                for location in locations:

                    if location in states:

                        if 'text' in tweet and 'lang' in tweet:
                            if tweet["lang"]=='en':
                                tweet_text = tweet['text']
                                words = tweet_text.split()

                                for word in words:
                                    lowercase_word = word.lower()
                                    if lowercase_word in scores:
                                        sentiment_score += scores[lowercase_word]

                        if location in state_happiness:
                            score = state_happiness[location][0]
                            count = state_happiness[location][1]
                            score += sentiment_score
                            count += 1
                            state_happiness[location] = [score,count]

                        else:
                            state_happiness[location] = [sentiment_score, 1]

    happiest_state_value = 0

    for key, value in state_happiness.items():
        avg_sentiment_score = value[0] / float(value[1])

        if avg_sentiment_score > happiest_state_value:
            happiest_state_value = avg_sentiment_score
            happiest_state = key


    print happiest_state # + " %.3f" % happiest_state_value

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    happiest_state_finder(sent_file, tweet_file)
    sent_file.close()
    tweet_file.close()

if __name__ == '__main__':
    main()

