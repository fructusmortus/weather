from db_insert_data import InsertData
from city_to_country import city_to_country


def cache_data_job():
    cities = InsertData.get_cities()
    countries = (city_to_country(city) for city in cities)
    city_ids = (InsertData.check_city_id(city) for  city in cities)
    country_ids = (InsertData.check_country_id(country) for country in countries)
    for city, city_id in zip(cities, city_ids):
        InsertData.insert_data_weather_api(city, city_id)
    for country, country_id in zip(countries, country_ids):
        InsertData.insert_data_news_api(country, country_id)
