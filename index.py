import conf
from weather_api_client import WeatherApiClient 
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/main')
def main():
    config = conf.con
    query = request.args.get('City')
    print(query)
    new_weather = WeatherApiClient(config['url'], query)
    data_response = new_weather.get_weather()
    return render_template('index.html', text=data_response, temp=data_response['current']['temperature'])

if __name__ == '__main__':
    app.run()