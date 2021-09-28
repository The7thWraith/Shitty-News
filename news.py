import pyautogui
import requests
import time
import random
from gtts import gTTS
import os
import playsound
from newsapi import NewsApiClient


# By The7thWraith
# Really shitty design, I made this at 11:30 on a school night I don't care
# I tried to do TTS but python did a bruh
# It uses RSS feeds because bad

pyautogui.prompt("Shitty News, by The7thWraith")

# c8033c0484f94194887351de963077d3

newsapi = NewsApiClient(api_key='c8033c0484f94194887351de963077d3')

f = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=c8033c0484f94194887351de963077d3')

print(f.text)

'''
subject = pyautogui.prompt("Topic - This is not optional")
sites = pyautogui.prompt("Sources - Leave blank for no sorting")


everything = newsapi.get_top_headlines(q='Trump', language='en', category='business', country='us')
print(everything)
'''

