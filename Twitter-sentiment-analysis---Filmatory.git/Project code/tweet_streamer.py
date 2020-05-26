import json
import csv
import tweepy
import re

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):

    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)

    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('tweets.csv', 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['tweet_text')

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.full_text.replace('\n',' ').encode('utf-8')])


consumer_key = "OycHbv63os98XA1WqRJbB9lT4"
consumer_secret = "aWt2CjULqrnnKe4gdVkI6yBwqeyzOgoqQwzfOlvJ9LmkZtTO1z"
access_token = "1235206685477793792-xxnYDEZiN6Tv82DRjJNRkM1ByKAPKv"
access_token_secret = "9VE6g8JpdWC7YKRKgH6qBaDEGQEPL4qjWmy4WXww2hdB0"

hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
