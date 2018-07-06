from twython import Twython, TwythonStreamer
import urllib.request
import time
import random
# from sense_hat import SenseHat
from .auth import (
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret
            )
# sense = SenseHat()
# sense.clear()
# sense.low_light = True
USER = 'realDonaldTrump'
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            username = data['user']['screen_name']
            #twitter.create_friendship(screen_name=username)
stream = MyStreamer(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )
try:
    id_str = []
    while True:
        twitter = Twython(consumer_key,consumer_secret, access_token, access_token_secret)
        search_results = twitter.search(count=1, q=SCREEN_NAME)
        for tweet in search_results['statuses']:
            if id_str == tweet['id_str']:
                # twitter.update_status(status="56ED81DC8CBBE4C86304BAD829BF77D4")
                print('Skipping tweet')
                break
         
            url = tweet['entities']['media'][0]['media_url']
            print(url)
            if url:
                urllib.request.urlretrieve(url, "00000002.jpg")
            if tweet['user']["screen_name"] == SCREEN_NAME:
                msg = tweet["text"]
                # sense.show_message(msg, scroll_speed = 0.05, text_colour=[255, 0, 0], back_colour=[0,0,255])
                # for i in range(0,8):
                    # for j in range(0,8):
                        # time.sleep(0.01)
                        # sense.set_pixel(i,j,(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                photo = open('00000002.jpg', 'rb')
                image = twitter.upload_media(media=photo)
                twitter.update_status(status="56ED81DC8CBBE4C86304BAD829BF77D4 This pi can tweet pictures!", media_ids=[image['media_id']])
                id_str = tweet['id_str']
        time.sleep(10.0)
except Exception as e:
    print(e)
    pass
finally:
    sense.clear()
