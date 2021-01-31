import requests
import json
import conf
from urllib.error import HTTPError
from urllib3.exceptions import NewConnectionError


class WeatherbitApiClient:

    weather_data = {}

    def __init__(self, city):
        self.config = conf.con_wb
        self.city = city
        # self.weather_data = requests.get(config['url'] + "current?access_key=" + config['api_key'] + "&query=" + city)

    def get_data(self):
        try:
            response = requests.get(f"{self.config['url']}?city={self.city}&key={self.config['api_key']}")
            self.weather_data = json.loads(response.text)
            print(self.weather_data)
            return True
        except HTTPError as err:
            print("HTTP error weatherbit_api_client", err)
            return False
        except NewConnectionError as nce:
            print("No connection tp weatherbit_api_client", nce)
            return False

    def get_weather(self):
        weather_descr = {
            "weather_descr": self.weather_data['data'][0]['weather']['description']
        }
        return weather_descr

    def get_wind(self):
        wind_info = {
            "wind_speed": self.weather_data['data'][0]['wind_spd'],
            "wind_dir": self.weather_data['data'][0]['wind_cdir_full']
        }
        return wind_info

    def get_main(self):
        main_info = {
            "temp": self.weather_data['data'][0]['temp'],
            "feels_like": self.weather_data['data'][0]['app_temp'],
            "pressure": self.weather_data['data'][0]['pres'],
            "humidity": self.weather_data['data'][0]['rh']
        }
        return main_info
