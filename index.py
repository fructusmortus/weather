from weather_api_client import WeatherApiClient
# from open_weather_api_client import OpenWeatherApiClient
from weatherbit_api_client import WeatherbitApiClient
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class Main(Resource):
    def get(self):
        city = query()
        print(query())
        new_weather = WeatherApiClient(city)
        status = new_weather.get_data()
        if status:
            wind_info = new_weather.get_wind()
            moisture_info = new_weather.get_moisture()
            main_weather_params = new_weather.get_main_weather_params()
            return {"weather_report": {
                "wind_info": wind_info,
                "moisture_info": moisture_info,
                "main_weather_params": main_weather_params
            }}
        else:
            # new_weather = OpenWeatherApiClient(city)
            new_weather = WeatherbitApiClient(city)
            status = new_weather.get_data()
            print("status", status)
            if status:
                weather_descr = new_weather.get_weather()
                wind_info = new_weather.get_wind()
                main_info = new_weather.get_main()
                return {"weather_report": {
                    "weather_descr": weather_descr,
                    "wind_info": wind_info,
                    "main_info": main_info
                }
                }


api.add_resource(Main, '/')


@app.route('/query')
def query():
    city = request.args.get('city')
    main = Main()
    return city


if __name__ == '__main__':
    app.run(debug=True)
