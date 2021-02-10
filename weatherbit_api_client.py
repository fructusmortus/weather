import requests
import conf


class WeatherbitApiClient:

    def __init__(self, city):
        self.config = conf.con_wb
        self.city = city
        self.weather_data = {}
        # self.weather_data = requests.get(config['url'] + "current?access_key=" + config['api_key'] + "&query=" + city)

    def get_data(self):
        response = requests.get(f"{self.config['url']}?city={self.city}&key={self.config['api_key']}")
        if 'data' not in response.json():
            return False
        else:
            self.weather_data = response.json()
            print(self.weather_data)
            return True

    def get_wind(self):
        return self.weather_data['data'][0]['wind_spd'], "km/h"

    def get_weather_description(self):
        return self.weather_data['data'][0]['weather']['description']

    def get_temperature(self):
        return self.weather_data['data'][0]['temp'], "celsius"
