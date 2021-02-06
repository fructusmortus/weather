from weather_api_client import WeatherApiClient
# from open_weather_api_client import OpenWeatherApiClient
from weatherbit_api_client import WeatherbitApiClient
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
    if city:
        new_weather = WeatherApiClient(city)
        status = new_weather.get_data()
        if status:
            wind_info = new_weather.get_wind()
            moisture_info = new_weather.get_moisture()
            main_weather_params = new_weather.get_main_weather_params()
            return render_template('index.html',
                                   wind=wind_info,
                                   moisture=moisture_info,
                                   main_weather_params=main_weather_params,
                                   city=city)
        else:
            # new_weather = OpenWeatherApiClient(city)
            new_weather = WeatherbitApiClient(city)
            status = new_weather.get_data()
            print("status", status)
            if status:
                weather_descr = new_weather.get_weather()
                wind_info = new_weather.get_wind()
                main_info = new_weather.get_main()
                return render_template('index.html',
                                       weather_descr=weather_descr,
                                       wind_info=wind_info,
                                       main_info=main_info,
                                       city=city)
            else:
                return render_template('error.html', city=city)


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
