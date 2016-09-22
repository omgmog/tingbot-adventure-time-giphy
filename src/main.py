import tingbot
from tingbot import *
import json, urllib

screen.fill(color='black')
img = 'empty.png'

@left_button.press
def random():
    global img
    # Query Giphy API for random gif tagged with "adventure time"
    url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=adventure+time'
    data = json.load(urllib.urlopen(url))
    img = data['data']['image_url']

@every(seconds=1.0/30)
def loop():
    screen.fill(color='black')
    screen.image(img)

@webhook('randomatgif')
def on_webhook(data):
    global img
    # Hey we got a new random "adventure time" gif, use it!
    img = data
    
tingbot.run()