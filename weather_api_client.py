import requests
import conf


class WeatherApiClient:

    def __init__(self, city):
        self.config = conf.con
        self.city = conf.con
        # self.weather_data = requests.get(config['url'] + "current?access_key=" + config['api_key'] + "&query=" + city)
        self.weather_data = {}

    def get_data(self):
        response = requests.get(f"{self.config['url']}current?access_key={self.config['api_key']}&query={self.city}")
        if not response.json()['request']:
            return False
        else:
            self.weather_data = response.json()
            print(self.weather_data)
            return True

    def get_wind(self):
        wind_info = {
            "wind_speed": self.weather_data['current']['wind_speed'],
            "wind_degree": self.weather_data['current']['wind_degree'],
            "wind_dir": self.weather_data['current']['wind_dir'],
        }
        return wind_info

    def get_moisture(self):
        moisture_info = {
            "precip": self.weather_data['current']['precip'],
            "humidity": self.weather_data['current']['humidity'],
            "cloudcover": self.weather_data['current']['cloudcover'],
        }
        return moisture_info

    def get_main_weather_params(self):
        other_info = {
            "temperature": self.weather_data['current']['temperature'],
            "feelslike": self.weather_data['current']['feelslike'],
            "weather_descriptions": self.weather_data['current']['weather_descriptions'][0],
            "uv_index": self.weather_data['current']['uv_index'],
            "visibility": self.weather_data['current']['visibility'],
        }
        return other_info
