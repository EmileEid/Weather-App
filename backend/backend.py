
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the React frontend
api_key = '7ab913b9dd0a1ad7ceffa0e402f0e81b'

# WeatherData class for storing weather attributes
class WeatherData:
    def __init__(self, date, time, weather, temp, feels_like, humidity, wind_s, wind_d):
        self.date = date
        self.time = time
        self.weather = weather
        self.temp = temp
        self.feels_like = feels_like
        self.humidity = humidity
        self.wind_s = wind_s
        self.wind_d = wind_d

def preprocess_data(forecast):
    data = forecast.get('list', [])
    daily_data = {}

    for entry in data:
        dt_txt = entry['dt_txt']
        date, time = dt_txt.split()

        weather = entry['weather'][0]['main']
        temp = entry['main']['temp']
        feels_like = entry['main']['feels_like']
        humidity = entry['main']['humidity']
        wind_s = entry['wind']['speed']
        wd = entry['wind']['deg']

        # Determine wind direction
        wind_d = get_wind_direction(wd)

        # Create WeatherData object
        weather_obj = WeatherData(date, time, weather, temp, feels_like, humidity, wind_s, wind_d)

        # Add data to daily_data dictionary
        if date not in daily_data:
            daily_data[date] = []
        daily_data[date].append(weather_obj.__dict__)  # Convert WeatherData object to a dictionary

    return daily_data

def get_wind_direction(wd):
    if wd >= 0 and wd <= 22.5 or wd > 337.5 and wd <= 360:
        return 'N'
    elif wd > 22.5 and wd <= 67.5:
        return 'NE'
    elif wd > 67.5 and wd <= 112.5:
        return 'E'
    elif wd > 112.5 and wd <= 157.5:
        return 'SE'
    elif wd > 157.5 and wd <= 202.5:
        return 'S'
    elif wd > 202.5 and wd <= 247.5:
        return 'SW'
    elif wd > 247.5 and wd <= 292.5:
        return 'W'
    elif wd > 292.5 and wd <= 337.5:
        return 'NW'
    return 'N'  # Default to 'N' if something goes wrong

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    try:
        # Fetch weather data from OpenWeatherMap API
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid={api_key}"
        )
        if response.status_code != 200:
            return jsonify({'error': 'Could not fetch weather data'}), 500

        forecast = response.json()
        daily_data = preprocess_data(forecast)  # Preprocess the data
        return jsonify(daily_data)  # Return preprocessed data as JSON

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
