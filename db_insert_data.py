from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from api_not_available import ApiNotAvailableException
from db_creation import Country, City, News, Weather
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import time
import pycountry

with open('country-capitals.json') as capitals:
    data_capitals = json.load(capitals)
    formatted_capitals = [cap['CapitalName'] for cap in data_capitals if cap['CapitalName'] != "N/A"]


class InsertData:

    @staticmethod
    def insert_data_news_api():
        engine = create_engine("postgresql://postgres:123QWEasd@localhost:5432/api_data_test")
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        countries = [country.alpha_2 for country in list(pycountry.countries)]
        identifier_c = 0
        identifier_n = 0
        for c in countries[0:10]:
            identifier_c += 1
            country = Country()
            country.id = identifier_c
            country.name = c
            session.add(country)
            time.sleep(1)
            try:
                whole_news = NewsApiClient(c)
            except ApiNotAvailableException:
                whole_news = LentaParser()
            top_news = whole_news.get_top_news()
            identifier_n += 2
            news = News()
            news.id = identifier_n
            news.country_id = country.id
            for content in top_news:
                news.title = content['title']
                news.body = content['body']
            session.add(news)
        session.commit()
        session.close()

    @staticmethod
    def insert_data_weather_api():
        engine = create_engine("postgresql://postgres:123QWEasd@localhost:5432/api_data_test")
        session_maker = sessionmaker(bind=engine)
        session = session_maker()
        identifier_c = 0
        identifier_n = 0
        for c in formatted_capitals[0:10]:
            identifier_c += 1
            city = City()
            city.id = identifier_c
            city.name = c
            session.add(city)
            time.sleep(1)
            try:
                new_weather = WeatherApiClient(c)
            except ApiNotAvailableException:
                new_weather = WeatherbitApiClient(c)
            identifier_n += 2
            weather = Weather()
            weather.id = identifier_n
            weather.city_id = city.id
            weather.weather_info = new_weather.get_weather_description()
            weather.temp_in_c = new_weather.get_temperature()[0]
            weather.wind_speed_kmph = new_weather.get_wind()[0]
            session.add(weather)
        session.commit()
        session.close()
