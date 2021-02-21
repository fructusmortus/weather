import requests
from conf import con
from ParentWeatherApi import ParentWeatherApi
from api_not_available import ApiNotAvailableException


class WeatherApiClient(ParentWeatherApi):
    BASE_URL = "{}current?access_key={}&query={}"

    def _send_request(self):
        response = requests.get(self.BASE_URL.format(con['url'], con['api_key'], self.city))
        if 'success' in response.json():
            error_message = response.json()['error']['info']
            raise ApiNotAvailableException(f"{error_message} occurred in WeatherApiClient")
        else:
            self.weather_data = response.json()

    def get_wind(self):
        return self.weather_data['current']['wind_speed'], "km/h"

    def get_weather_description(self):
        return self.weather_data['current']['weather_descriptions'][0]

    def get_temperature(self):
        return self.weather_data['current']['temperature'], "celsius"
