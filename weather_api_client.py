import requests
import json
import conf


class WeatherApiClient:

    weather_data = {}

    def __init__(self, city):
        config = conf.con
        # self.weather_data = requests.get(config['url'] + "current?access_key=" + config['api_key'] + "&query=" + city)
        response = requests.get(f"{config['url']}current?access_key={config['api_key']}&query={city}")
        self.weather_data = json.loads(response.text)
        print(self.weather_data)

    def get_weather(self):
        return self.weather_data

    def get_wind(self):
        wind_info = {
            "wind_speed": self.weather_data['current']['wind_speed'],
            "wind_degree": self.weather_data['current']['wind_degree'],
            "wind_dir": self.weather_data['current']['wind_dir'],
        }
        return wind_info