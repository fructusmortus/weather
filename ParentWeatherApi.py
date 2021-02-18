from abc import ABC, abstractmethod


class ParentWeatherApi(ABC):

    def __init__(self, city):
        self.weather_data = {}
        self.city = city
        self.send_request()

    @abstractmethod
    def send_request(self):
        raise NotImplementedError

    @abstractmethod
    def get_wind(self):
        raise NotImplementedError

    @abstractmethod
    def get_weather_description(self):
        raise NotImplementedError

    @abstractmethod
    def get_temperature(self):
        raise NotImplementedError

