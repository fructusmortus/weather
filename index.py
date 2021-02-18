from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from flask import Flask
from flask import request
from flask import render_template
from flask_restful import Api
from flask import jsonify
from api_not_available import ApiNotAvailableException

app = Flask(__name__)

api = Api(app)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/main', methods=['POST', 'GET'])
def main():
    city = request.args.get('city')
    country = request.args.get('country')
    if city and country:
        try:
            new_weather = WeatherApiClient(city)
            news = NewsApiClient(country)
        except ApiNotAvailableException:
            new_weather = WeatherbitApiClient(city)
            news = LentaParser()
        wind_info = new_weather.get_wind()
        weather_info = new_weather.get_weather_description()
        temperature_info = new_weather.get_temperature()
        data = {
            "city": city,
            "country": country,
            "hot_news": news.news_data,
            "local_weather": {"wind_info": wind_info,
                              "weather_info": weather_info,
                              "temperature_info": temperature_info
                              }
        }
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
