from conf import postgres_con
from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from api_not_available import ApiNotAvailableException
from db_creation import Country, City, News, Weather
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time


class InsertData:
    engine = create_engine(postgres_con['c_str'])

    @staticmethod
    def check_country_id(country_name):
        session = sessionmaker(bind=InsertData.engine)()
        country_object = session.query(Country).filter(Country.name == country_name).first()
        session.close()
        if country_object:
            return country_object.id
        return None

    @staticmethod
    def check_news(country_id):
        session = sessionmaker(bind=InsertData.engine)()
        actual_news = []
        for instance in session.query(News).filter(News.country_id == country_id).order_by(News.date.desc()).limit(3):
            actual_news.append({'title': instance.title, 'body': instance.body})
        session.close()
        return actual_news

    @staticmethod
    def insert_country(country_name):
        session = sessionmaker(bind=InsertData.engine)()
        country = Country()
        country.name = country_name
        session.add(country)
        session.flush()
        country_id = country.id
        session.commit()
        session.close()
        return country_id

    @staticmethod
    def insert_data_news_api(country, country_id):
        session = sessionmaker(bind=InsertData.engine)()
        try:
            whole_news = NewsApiClient(country)
        except ApiNotAvailableException:
            time.sleep(1)
            whole_news = LentaParser()
        top_news = whole_news.get_top_news()
        actual_news = []
        for content in top_news:
            news = News()
            news.country_id = country_id
            news.title = content['title']
            news.body = content['body']
            actual_news.append({'title': news.title, 'body': news.body})
            session.add(news)
        session.commit()
        session.close()
        if actual_news:
            return actual_news
        raise RuntimeError('Error during the data processing')


    @staticmethod
    def check_city_id(city_name):
        session = sessionmaker(bind=InsertData.engine)()
        city_object = session.query(City).filter(City.name == city_name).first()
        session.close()
        if city_object:
            return city_object.id
        return None

    @staticmethod
    def check_weather(city_id):
        session = sessionmaker(bind=InsertData.engine)()
        actual_weather = []
        for instance in session.query(Weather).filter(Weather.city_id == city_id)\
                                              .order_by(Weather.date.desc())\
                                              .limit(1):
            actual_weather.append({
               'temperature_info': [instance.temp_in_c, 'celsius'],
               'weather_info': instance.weather_info,
               'wind_info': [instance.wind_speed_kmph, 'km/h']
            })
        session.close()
        return actual_weather

    @staticmethod
    def insert_city(city_name):
        session = sessionmaker(bind=InsertData.engine)()
        city = City()
        city.name = city_name
        session.add(city)
        session.flush()
        city_id = city.id
        session.commit()
        session.close()
        return city_id

    @staticmethod
    def insert_data_weather_api(city, city_id):
        session = sessionmaker(bind=InsertData.engine)()
        try:
            new_weather = WeatherApiClient(city)
        except ApiNotAvailableException:
            new_weather = WeatherbitApiClient(city)
        weather = Weather()
        weather.city_id = city_id
        weather.weather_info = new_weather.get_weather_description()
        weather.temp_in_c = new_weather.get_temperature()[0]
        weather.wind_speed_kmph = new_weather.get_wind()[0]
        session.add(weather)
        actual_weather = {
            "wind_info": [weather.wind_speed_kmph, 'km/h'],
            "weather_info": weather.weather_info,
            "temperature_info": [weather.temp_in_c, "celsius"]
        }
        session.commit()
        session.close()
        if actual_weather:
            return actual_weather
        raise RuntimeError('Error during the data processing')

    @staticmethod
    def get_cities():
        actual_city = []
        session = sessionmaker(bind=InsertData.engine)()
        city_objects = session.query(City).order_by(City.name).distinct()
        for city in city_objects:
            actual_city.append(city.name)
        return actual_city
