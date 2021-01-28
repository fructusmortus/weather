from weather_api_client import WeatherApiClient
from open_weather_api_client import OpenWeatherApiClient
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')


@app.route('/main')
def main():
    city = request.args.get('city')
    new_weather = WeatherApiClient(city)
    data_response = new_weather.get_weather()
    return render_template('index.html', text=data_response, city=city)


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
    app.run()