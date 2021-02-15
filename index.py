from weather_api_client import WeatherApiClient
from news_api_client import NewsApiClient
from weatherbit_api_client import WeatherbitApiClient
from LentaParser import LentaParser
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask_restful import Resource, Api
from flask import jsonify

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
        new_weather = WeatherApiClient(city)
        status_weather = new_weather.get_weather_data()
        if status_weather:
            wind_info = new_weather.get_wind()
            weather_info = new_weather.get_weather_description()
            temperature_info = new_weather.get_temperature()
        else:
            new_weather = WeatherbitApiClient(city)
            status_weather = new_weather.get_weather_data()
            if status_weather:
                wind_info = new_weather.get_wind()
                weather_info = new_weather.get_weather_description()
                temperature_info = new_weather.get_temperature()
            else:
                return render_template('error.html')
        news = NewsApiClient(country)
        status_news = news.get_data()
        if status_news:
            top_news = news.get_top_news()
        else:
            news = LentaParser()
            top_news = news.get_news()
        data = {
            "city": city,
            "country": country,
            "hot_news": top_news,
            "local_weather": {"wind_info": wind_info,
                              "weather_info": weather_info,
                              "temperature_info": temperature_info
                              }
        }
        return jsonify(data)

@app.route('/wind-info')
def wind():
    city = request.args.get('city')
    if city:
        new_weather = WeatherApiClient(city)
        wind_info = new_weather.get_wind()
        print(wind_info)
        return render_template('wind-info.html', wind=wind_info)
    else:
        return redirect("/", code=302)


@app.route('/moisture-info')
def moisture():
    city = request.args.get('city')
    if city:
        new_weather = WeatherApiClient(city)
        moisture_info = new_weather.get_moisture()
        return render_template('moisture-info.html', moisture=moisture_info)
    else:
        return redirect("/", code=302)


if __name__ == '__main__':
    app.run(debug=True)
