# credentials to login to twitter api
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# credentials to login to unsplash api
YOUR_ACCESS_KEY = ""
SECRET_KEY = ""

ID = ''
PER_PAGE = ''
PAGE = ''
URL = 'https://api.unsplash.com/collections/' + ID + '/photos/?page=' + PAGE + '&per_page=' + PER_PAGE + '&client_id=' + YOUR_ACCESS_KEY