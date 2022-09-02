from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp']),weather['humidity'],weather['wind']

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_hot():
  url = "https://tenapi.cn/resou/"
  res = requests.get(url).json()
  hot0 = res['data']['list'][0]
  hot1 = res['data']['list'][1]
  hot2 = res['data']['list'][2]
  hot3 = res['data']['list'][3]
  hot4 = res['data']['list'][4]
  hot5 = res['data']['list'][5]
  hot6 = res['data']['list'][6]
  hot7 = res['data']['list'][7]
  hot8 = res['data']['list'][8]
  hot9 = res['data']['list'][9]
  return hot0['name'],
         hot1['name'],
         hot2['name'],
         hot3['name'],
         hot4['name'],
         hot5['name'],
         hot6['name'],
         hot7['name'],
         hot8['name'],
         hot9['name']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, humidity, wind = get_weather()
data = {"weather":{"value":wea, "color":get_random_color()},
        "temperature":{"value":temperature, "color":get_random_color()},
        "humidity":{"value":humidity, "color":get_random_color()},
        "wind":{"value":wind, "color":get_random_color()},
        "love_days":{"value":get_count(), "color":get_random_color()},
        "birthday_left":{"value":get_birthday(), "color":get_random_color()},
        "words":{"value":get_words(), "color":get_random_color()}},
        "hot":{"value":get_hot(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
