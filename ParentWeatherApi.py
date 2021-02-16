from abc import ABC, abstractmethod


class ParentWeatherApi(ABC):

    def __init__(self, city):
        self.weather_data = {}
        self.city = city
        self.send_request()

    @abstractmethod
    def send_request(self):
        pass

    def get_weather_data(self):
        return self.weather_data
