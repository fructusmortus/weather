from weather_api_client import WeatherApiClient
# from open_weather_api_client import OpenWeatherApiClient
from weatherbit_api_client import WeatherbitApiClient
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
    # city = request.args.get('city')
    body = request.get_json(silent=True)
    # print(body)
    city = body['city']
    if city:
        new_weather = WeatherApiClient(city)
        status = new_weather.get_data()
        if status:
            wind_info = new_weather.get_wind()
            moisture_info = new_weather.get_moisture()
            main_weather_params = new_weather.get_main_weather_params()
            data = {"moisture_info": moisture_info,
                    "wind_info": wind_info,
                    "main_weather_params": main_weather_params}
            return jsonify(data)
        else:
            # new_weather = OpenWeatherApiClient(city)
            new_weather = WeatherbitApiClient(city)
            status = new_weather.get_data()
            print("status", status)
            if status:
                weather_descr = new_weather.get_weather()
                wind_info = new_weather.get_wind()
                main_info = new_weather.get_main()
                data = {"weather_descr": weather_descr,
                        "wind_info": wind_info,
                        "main_info": main_info}
                return jsonify(data)
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
    app.run(debug=True)
