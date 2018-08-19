import tweepy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

# Authenticate
consumer_key = 'HBpNPyvFAuEpo1R4ZY5KJ22kG'
consumer_secret = '4xUdHbmzIHEu3rdYxWIqtLLSwQCnA6Alsfc8uuWpmU6AoIEYrV'

access_token = '904728549235466240-QAQIENEbRgj80CqBq1ikw6rFJJpffVH'
access_token_secret = 'taR3A8beqyBajpmYihr9p3436mJco54TcrDbxK3cuwaDy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Retrieve Tweets
public_tweets = api.search('Bitcoin')

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

def get_label(value):
	if analysis.sentiment[0] > 0:
		return 'Positive'
	else:
		return 'Negative'

f = open('tweets.csv', 'w')
for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	f.write('%s,%s\n' % (tweet.text.encode('utf-8'), get_label(analysis)))

f.close()
    # print(tweet.text)
    
    # #Step 4 Perform Sentiment Analysis on Tweets
    # analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
    # print("")