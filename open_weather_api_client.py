import requests
import json
import conf


class OpenWeatherApiClient:

    weather_data = {}

    def __init__(self, city):
        config = conf.con_ow_data
        # self.weather_data = requests.get(config['url'] + "current?access_key=" + config['api_key'] + "&query=" + city)
        response = requests.get(f"{config['url']}data/2.5/find?q={city}&appid={config['api_key']}")
        self.weather_data = json.loads(response.text)
        print(self.weather_data)

    def get_weather(self):
        weather_descr = {
            "weather_descr": self.weather_data['list'][0]['weather'][0]['description']
        }
        return weather_descr

    def get_wind(self):
        wind_info = {
            "wind_speed": self.weather_data['list'][0]['wind']['speed'],
            "wind_degree": self.weather_data['list'][0]['wind']['deg']
        }
        return wind_info

    def get_main(self):
        main_info = {
            "temp": self.weather_data['list'][0]['main']['temp'],
            "feels_like": self.weather_data['list'][0]['main']['feels_like'],
            "pressure": self.weather_data['list'][0]['main']['pressure'],
            "humidity": self.weather_data['list'][0]['main']['humidity']
        }
        return main_info
