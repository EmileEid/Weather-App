from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = '7ab913b9dd0a1ad7ceffa0e402f0e81b'

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
    return 'N'

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
        wind_d = get_wind_direction(entry['wind']['deg'])

        weather_data = {
            'time': time,
            'weather': weather,
            'temp': temp,
            'feels_like': feels_like,
            'humidity': humidity,
            'wind_s': wind_s,
            'wind_d': wind_d
        }

        if date not in daily_data:
            daily_data[date] = []
        daily_data[date].append(weather_data)

    return daily_data

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    try:
        # Make request to OpenWeatherMap API for 5-day forecast
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=imperial&appid={API_KEY}'
        print(f"Requesting: {url}")  # Debug print
        
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error response: {response.text}")  # Debug print
            return jsonify({'error': 'City not found'}), 404

        data = response.json()
        processed_data = preprocess_data(data)
        print(f"Processed data: {processed_data}")  # Debug print
        
        return jsonify(processed_data)

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debug print
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)