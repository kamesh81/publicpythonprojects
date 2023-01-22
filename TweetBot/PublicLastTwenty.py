import datetime
import tweepy

# Authenticate to Twitter
# auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
# auth.set_access_token(key, secret)

# Create API object
api = tweepy.API(auth)

# Handle of the account whose tweets you want to like
handle = 'kameshsangili'

user = api.get_user(screen_name = handle)

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
