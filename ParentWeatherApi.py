class ParentWeatherApi:

    def __init__(self, city, config):
        self.config = config
        self.city = city
        self.weather_data = {}
