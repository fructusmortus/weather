import requests
import json

class WeatherApiClient():
    url = ''
    query = ''
    weather_data = {}
    def __init__(self, url, query):
        self.query = query
        self.url = url + query 

    def get_weather(self):
        response = requests.get(self.url)
        self.weather_data = json.loads(response.text)
        return self.weather_data