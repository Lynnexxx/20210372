#!/usr/bin/env python
# coding: utf-8

import os
import requests



def get_weather():
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    lat = os.environ.get('LAT')
    lon = os.environ.get('LON')
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
    response = requests.get(url)


    if response.status_code == 200:
        weather_data = response.json()
        print(f"The current weather in ({lat}, {lon}) is {weather_data['weather'][0]['description']}")
    else:
        print(f"Failed to retrieve weather data: {response.status_code} {response.text}")

    return response.json() 

get_weather()

