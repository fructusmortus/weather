import requests
import conf
from api_not_available import ApiNotAvailableException
from ParentWeatherApi import ParentWeatherApi


class WeatherbitApiClient(ParentWeatherApi):
    BASE_URL = "{}?city={}&key={}"

    def __init__(self, city):
        super().__init__(city)

    def send_request(self):
        response = requests.get(self.BASE_URL.format(conf.con_wb['url'], self.city, conf.con_wb['api_key']))
        try:
            self.weather_data = response.json()
            return self.weather_data
        except ApiNotAvailableException:
            if response.status_code != 200:
                error_message = response.json()['error']
                raise ApiNotAvailableException(f"{error_message} occurred in WeatherbitApiClient")

    def get_weather_data(self):
        return self.weather_data

    def get_wind(self):
        return self.weather_data['data'][0]['wind_spd'], "km/h"

    def get_weather_description(self):
        return self.weather_data['data'][0]['weather']['description']

    def get_temperature(self):
        return self.weather_data['data'][0]['temp'], "celsius"
