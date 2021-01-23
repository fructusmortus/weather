import requests
import json
import conf

class Weather_api_client():
    api_key = ''
    lat = ''
    lon = ''
    url = ''
    weather_data = {}
    def __init__(self, api_key, lat, lon, url):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.url = url % (lat, lon, api_key)
        self.get_weather()

    def get_weather(self):
        response = requests.get(self.url)
        self.weather_data = json.loads(response.text)



config = conf.con
new_weather = Weather_api_client(config['api_key'], config['lat'], config['lon'], config['url'])
data_response = new_weather.get_weather()
print(data)