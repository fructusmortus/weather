import requests
import conf


class WeatherApiClient:

    def __init__(self, city):
        self.config = conf.con
        self.city = city
        self.weather_data = {}

    def get_data(self):
        response = requests.get(f"{self.config['url']}current?access_key={self.config['api_key']}&query={self.city}")
        if response.status_code != 200:
            print(response.status_code)
            return False
        else:
            self.weather_data = response.json()
            print(self.weather_data)
            return True

    def get_wind(self):
        return self.weather_data['current']['wind_speed'], "km/h"

    def get_weather_description(self):
        return self.weather_data['current']['weather_descriptions'][0]

    def get_temperature(self):
        return self.weather_data['current']['temperature'], "celsius"
