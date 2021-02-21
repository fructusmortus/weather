from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from api_not_available import ApiNotAvailableException
import datetime
from flask import request
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlalchemy
import pgconnection
import pycountry



class InsertData:

    def __init__(self):
        self.gathered_apis_data = {}

    def gather_data_news_api(self):
        countries = (country.alpha_2 for country in list(pycountry.countries))
        for country in countries:
            try:
                news = NewsApiClient(country)
            except ApiNotAvailableException:
                news = LentaParser()

    def gather_apis_data(self):
        return self.gathered_apis_data

    def insert_data(self):
        try:
            conn = pgconnection.get_connection("apidata")
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()
            for item in self.data_response():

                cursor.execute("""INSERT INTO city(name)
                                  VALUE (%(name)s);""", item["city"])
                print("City inserted")

                cursor.execute("""INSERT INTO weather(cityid, weather_info, temp_in_celsius, wind_speed_kmph, dateadded)
                                  VALUES (%(cityid)s, %(weather_info)s, %(temp_in_celsius)s, %(wind_speed_kmph)s, %(dateadded)s);""", item)

            cursor.close()
            conn.close()

        except psycopg2.Error as e:

            print(type(e))

            print(e)
