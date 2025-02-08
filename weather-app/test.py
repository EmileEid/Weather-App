import requests

#openweathermap api key
api_key = '7ab913b9dd0a1ad7ceffa0e402f0e81b'

#user enters a city
user_input = input("Enter City: ")

#fetch api data for user input
forcast = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?q={user_input}&units=imperial&appid={api_key}"
).json()

#https://api.openweathermap.org/data/2.5/forecast?q=St. Louis&units=imperial&appid=06bdab518281978935a4c23f7daddb5a
#Class for weather data object
class weather_data:
    def __init__(self, date, time, weather, temp, feels_like, humidity, wind_s, wind_d):
        self.date = date
        self.time = time
        self.weather = weather
        self.temp = temp
        self.feels_like = feels_like
        self.humidity = humidity
        self.wind_s = wind_s
        self.wind_d = wind_d

#Function to take in forcast data and separate the hourly forcasts by day.
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
        weather_obj = weather_data(date, time, weather, temp, feels_like, humidity, wind_s, wind_d)

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

# function to display hourly data by day
def display(daily_data):
    for date, forecasts in daily_data.items():
        print(f"Date: {date}")
        print("-" * 40)
        
        for weather in forecasts:
            print(f"Time: {weather['time']}")
            print(f"Weather: {weather['weather']}")
            print(f"Temperature: {weather['temp']}°F")
            print(f"Feels Like: {weather['feels_like']}°F")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind: {weather['wind_s']} mph {weather['wind_d']}")
            print("-" * 40)
        print("\n")



#error handling
if forcast['cod'] == '404':
    print("No City Found")

else:
    #main function
    daily_data = preprocess_data(forcast)

    display(daily_data)
    