import datetime
import tweepy

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
# auth.set_access_token(key, secret)

# Create API object
api = tweepy.API(auth)

# Handle of the account whose tweets you want to like
handle = 'sangilikamesh'
user = api.get_user(screen_name=handle)
userid = user.id
print(userid)
# Time range for tweets (in this case, last 24 hours)
time_range = datetime.datetime.now() - datetime.timedelta(days=1)

# Get user timeline
trends = api.get_place_trends(23424848)
#India http://where.yahooapis.com/v1/place/23424848

for trend in trends:
    print(trend)
