import requests
import os
from datetime import datetime

api_key = '285c52bdd298d32615b1f4cf4e6531cc0000'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)

with open('wether_report.txt', 'wb') as t:
    t.write(api_link.content)
