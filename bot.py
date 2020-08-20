import requests as resquests
import time
import tweepy
import random
import os
import settings

r = resquests.get(settings.URL)
data = r.json()

api = tweepy.API(settings.auth)
posted = 'banned_id.txt'

# back to ./
os.chdir('./')

# creates txt file if not existent
if not os.path.exists('./banned_id.txt'):
    f = open('banned_id.txt', 'w+')

# creates images folder if not existent
if not os.path.exists('images'):
    os.makedirs('images')

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

random_time = [639, 530, 302, 1209, 677, 710, 666, 578]

while True:
    # Select a random json object in data
    selected = random.choice(data)
    print('Selected ID: ' + selected['id'])

    # If the ID of the selected object its already in the text file, it find gets another object
    with open(posted) as f:
        datafile = f.read()
        while selected['id'] in datafile:
            print('ID was already posted, finding new one...')
            selected = random.choice(data)
            print('New selected picture: ' + selected['id'])

    # back to ./images
    os.chdir('./images')

    # Download the selected image
    resp = resquests.get(selected['urls']['regular'])
    if resp.status_code == 200:
        with open(selected['id'] + '.jpg', 'wb') as f:
            f.write(resquests.get(selected['urls']['regular']).content)
            f.close()

    twtImage = selected['id'] + '.jpg'
    hashtag = '#visual #aesthetic'
    status = 'src: ' + selected['user']['username'] + ' ' + selected['user']['links']['html'] + '\n' + hashtag

    # Tweets the img + status
    api.update_with_media(twtImage, status)
    print('New tweet posted!')

    # back to ./
    os.chdir('./')

    # After the tweet has been sucessfully posted, it writes the image ID in a text file
    with open(posted, 'a') as t:
        t.write(str(selected['id'])+'\n')
        t.close

    # Random select a int in the random list to simulate a more human posting routine
    t = random.choice(random_time)
    print('Next tweet in: ' + str(t/60) + ' mins.')
    time.sleep(t)
