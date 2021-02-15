import requests
import conf
from ParentWeatherApi import ParentWeatherApi
from api_not_available import ApiNotAvailableException


class WeatherApiClient():
    BASE_URL = "{}current?access_key={}&query={}"

    def __init__(self, city):
        self.weather_data = {}
        self.city = city
        self.send_request()

    def send_request(self):
        response = requests.get(self.BASE_URL.format(conf.con['url'], conf.con['api_key'], self.city))
        if 'success' in response.json():
            error_message = response.json()['error']['info']
            print(ApiNotAvailableException(f"{error_message} occurred in WeatherApiClient"))
            return None
        else:
            self.weather_data = response.json()
            return self.weather_data

    def get_weather_data(self):
        return self.weather_data

    def get_wind(self):
        return self.weather_data['current']['wind_speed'], "km/h"

    def get_weather_description(self):
        return self.weather_data['current']['weather_descriptions'][0]

    def get_temperature(self):
        return self.weather_data['current']['temperature'], "celsius"
