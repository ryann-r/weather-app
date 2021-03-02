"""Server for weather app"""

from os import environ
import json
import requests
import sys
from flask import Flask, request, jsonify, render_template, session, redirect, flash
from jinja2 import StrictUndefined


# API: OpenWeather https://openweathermap.org/api

# Build a weather app that displays a 5-day weather forecast.

# Include city name, current weather icon, temp, humidity, wind speed, etc

# Display the recording of both high and low temps of each day
# Display images for sunny/rainy/cloudy/snowy weather conditions
# Refresh every 5 minutes with exact temp & weather conditions

# use font awesome for icons

app = Flask(__name__)

app.secret_key = 'APP_SECRET_KEY'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """View homepage."""

    return render_template('main.html')


@app.route('/api/get_weather')
def get_weather():
    """Returns JSON weather data at given city name from OpenWeather API."""

    if session.get('city'):
        city_name=session['city']

        api_key = environ.get('WEATHER_API_KEY')
        # city_name = 'London'
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, api_key)
        res = requests.get(url)

        weather = res.json()

        return jsonify({'weather': weather})

    else:
        flash("Please search for a city.")
        return redirect('/')

@app.route('/api/search-input', methods=['POST', 'GET'])
def search_input():
    """Returns city searched for, sets to session."""

    
    data = request.get_json()
    city = data.get('city')
    session['city'] = city
    print("CITY IS", city)

    return city



if __name__ == '__main__':
    # connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')