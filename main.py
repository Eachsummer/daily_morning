from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import json

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

def get_hota():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][0]
    return hot0['name']


def get_hotb():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][1]
    return hot0['name']


def get_hotc():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][2]
    return hot0['name']


def get_hotd():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][3]
    return hot0['name']
  

def get_hote():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][4]
    return hot0['name']


def get_hotf():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][5]
    return hot0['name']
  

def get_hotg():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][6]
    return hot0['name']


def get_hoth():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][7]
    return hot0['name']
  

def get_hoti():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][8]
    return hot0['name']


def get_hotj():
    url = "https://tenapi.cn/resou/"
    res = requests.get(url).json()
    hot0 = res['list'][9]
    return hot0['name']


def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, humidity, wind = get_weather()
hot1 = get_hota()
hot2 = get_hotb()
hot3 = get_hotc()
hot4 = get_hotd()
hot5 = get_hote()
hot6 = get_hotf()
hot7 = get_hotg()
hot8 = get_hoth()
hot9 = get_hoti()
hot10 = get_hotj()
data = {"weather":{"value":wea, "color":get_random_color()},"temperature":{"value":temperature, "color":get_random_color()},"humidity":{"value":humidity, "color":get_random_color()},"wind":{"value":wind, "color":get_random_color()},"love_days":{"value":get_count(), "color":get_random_color()},"birthday_left":{"value":get_birthday(), "color":get_random_color()},"words":{"value":get_words(), "color":get_random_color()}},"hot":{"value":hot1, "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
