from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from flask import Flask
from flask import request
from GetValidator import RunRequestSchema
from flask_restful import Api
from flask import jsonify
from api_not_available import ApiNotAvailableException
from allcities import cities
import pycountry

app = Flask(__name__)

api = Api(app)

run_request_schema = RunRequestSchema()


@app.route('/current_data', methods=['GET'])
def current_data():
    errors = run_request_schema.validate(request.args)
    if errors:
        raise ValueError(("An error occurred with input: {}".format(errors)))
    city = request.args.get('city')
    filtered_city_set = cities.filter(name=city, population='>100000')
    largest_city = next(iter(filtered_city_set))
    if largest_city.dict['country_code'] in [country.alpha_2 for country in list(pycountry.countries)]:
        country = largest_city.dict['country_code']
        try:
            new_weather = WeatherApiClient(city)
        except ApiNotAvailableException:
            new_weather = WeatherbitApiClient(city)
        try:
            news = NewsApiClient(country)
        except ApiNotAvailableException:
            news = LentaParser()
        wind_info = new_weather.get_wind()
        weather_info = new_weather.get_weather_description()
        temperature_info = new_weather.get_temperature()
        data = {
            "city": city,
            "country": country,
            "hot_news": news.get_top_news(),
            "local_weather": {"wind_info": wind_info,
                              "weather_info": weather_info,
                              "temperature_info": temperature_info
                              }
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
