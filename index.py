from flask import Flask, request, jsonify
from GetValidator import RunRequestSchema
from flask_restful import Api
from city_to_country import city_to_country
from db_insert_data import InsertData

app = Flask(__name__)

api = Api(app)

run_request_schema = RunRequestSchema()


@app.route('/current_data', methods=['GET'])
def current_data():
    errors = run_request_schema.validate(request.args)
    if errors:
        raise ValueError(("An error occurred with input: {}".format(errors)))
    city = request.args.get('city')
    country = city_to_country(city)
    country_id = InsertData.check_country_id(country)
    city_id = InsertData.check_city_id(city)
    if not country_id and not city_id:
        country_id = InsertData.insert_country(country)
        city_id = InsertData.insert_city(city)
        actual_weather = InsertData.insert_data_weather_api(city, city_id)
        actual_news = InsertData.insert_data_news_api(country, country_id)
    else:
        actual_weather = InsertData.check_weather(city_id)
        actual_news = InsertData.check_news(country_id)
        print(actual_news)
    data = {
        "city": city,
        "country": country,
        "hot_news": actual_news,
        "local_weather": actual_weather
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
