import datetime
import requests
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sqlalchemy
import pgconnection


class InsertData:

    BASE_URL = "http://127.0.0.1:5000/main?city=Ottawa&country=ca"

    def __init__(self):
        self.data_response = {}
        self.send_request()

    def send_request(self):
        response = requests.get(InsertData.BASE_URL)
        self.data_response = response.json()
        return self.data_response

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