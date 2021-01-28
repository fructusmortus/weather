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
        return self.weather_data

    # def get_wind(self):
    #     wind_info = {
    #         "wind_speed": self.weather_data['current']['wind_speed'],
    #         "wind_degree": self.weather_data['current']['wind_degree'],
    #         "wind_dir": self.weather_data['current']['wind_dir'],
    #     }
    #     return wind_info
    #
    # def get_moisture(self):
    #     moisture_info = {
    #         "precip": self.weather_data['current']['precip'],
    #         "humidity": self.weather_data['current']['humidity'],
    #         "cloudcover": self.weather_data['current']['cloudcover'],
    #     }
    #     return moisture_info
    #
    # def get_main_weather_params(self):
    #     other_info = {
    #         "temperature": self.weather_data['current']['temperature'],
    #         "feelslike": self.weather_data['current']['feelslike'],
    #         "weather_descriptions": self.weather_data['current']['weather_descriptions'][0],
    #         "uv_index": self.weather_data['current']['uv_index'],
    #         "visibility": self.weather_data['current']['visibility'],
    #     }
    #     return other_info
