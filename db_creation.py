from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2

import pgconnection


def main():
    queries = ({"Description": "Create database",
                "Database": "postgres",
                "SQL": """CREATE DATABASE apidata"""},

               {"Description": "Create city table ",
                "Database": "apidata",
                "SQL": """CREATE TABLE city(cityid serial PRIMARY KEY, name varchar(256) NOT NULL)"""},

               {"Description": "Create weather table ",
                "Database": "apidata",
                "SQL": """CREATE TABLE weather(weatherid serial PRIMARY KEY, 
                                       cityid smallint REFERENCES city(cityid) NOT NULL, 
                                       weather_info varchar(256) NOT NULL, 
                                       temp_in_celsius DECIMAL(3,1) NOT NULL, 
                                       wind_speed_kmph smallint NOT NULL, dateadded date)"""},

                {"Description": "Create country table ",
                 "Database": "apidata",
                 "SQL": """CREATE TABLE country(countryid serial PRIMARY KEY, name varchar(256) NOT NULL)"""},

                {"Description": "Create news table ",
                 "Database": "apidata",
                 "SQL": """CREATE TABLE news(newsid serial PRIMARY KEY, 
                                                       countryid smallint REFERENCES country(countryid) NOT NULL, 
                                                       title varchar(1024) NOT NULL, 
                                                       body text NOT NULL, 
                                                       dateadded date)"""})

    try:

        for query in queries:
            conn = pgconnection.get_connection(query["Database"])
            print(conn)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = conn.cursor()

            cursor.execute(query["SQL"])

            print("Executed {}".format(query["Description"]))

            cursor.close()
            conn.close()

    except psycopg2.ProgrammingError as e:

        print(e)


main()
