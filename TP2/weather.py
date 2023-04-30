#!/usr/bin/env python
# coding: utf-8


from flask import Flask, request
import json
import os
import requests
from sys import argv

app = Flask(__name__)


@app.route("/",methods =['GET'])

def get_weather_api():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    api_key = argv[1]
    #url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=68dffda753df5b17c71723a01bd17b41'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"The current weather in ({lat}, {lon}) is {weather_data['weather'][0]['description']}")
    else:
        print(f"Failed to retrieve weather data: {response.status_code} {response.text}")

    return response.json() 




if __name__ == '__main__':
    app.run(debug=True, port= 8081)

    get_weather_api()


