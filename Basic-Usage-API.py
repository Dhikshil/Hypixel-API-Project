import requests
import json
from pprint import pprint

name = "speedy_spider555"
#use namemc.com to get uuid and uuid-dashed

#use https://developer.hypixel.net/dashboard to get api key
API_KEY = "ef6332e4-72fe-4c77-be4d-b6c324cc943f"

name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={name}"

url = f"https://api.hypixel.net/key?key={API_KEY}"

#get user details
def get_info(call):
    r = requests.get(call)
    return r.json()

pprint(get_info(url))
