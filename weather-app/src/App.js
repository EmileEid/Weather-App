import React, { useState, useEffect } from 'react';
import './App.css';  // Import CSS file for styling

const App = () => {
    const [city, setCity] = useState('');
    const [weatherData, setWeatherData] = useState({});  // Changed to an object to match backend nested dictionary
    const [dropdownVisible, setDropdownVisible] = useState(false); // State to manage dropdown visibility
    const [selectedDate, setSelectedDate] = useState(''); // State to manage the selected date for forecast

    useEffect(() => {
        if (Object.keys(weatherData).length > 0) {  // Check if weatherData has keys
            const firstDate = Object.keys(weatherData)[0];
            setSelectedDate(firstDate); // Set the first date as the default selected date
        }
    }, [weatherData]);
    const fetchWeather = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/weather?city=${encodeURIComponent(city)}`);
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            setWeatherData(data); // Set preprocessed data directly
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    };

    const toggleDropdown = () => {
        setDropdownVisible(!dropdownVisible); // Toggle dropdown visibility
    };

    const handleDateChange = (date) => {
        setSelectedDate(date); // Update the selected date when a button is clicked
    };

    const getWeatherDetailsForDay = (forecasts) => {
        let weatherAtNoon = forecasts.find(f => f.time === '12:00:00'); // Find weather at 12:00
        if (!weatherAtNoon) {
            weatherAtNoon = forecasts[forecasts.length - 1]; // If not available, get the most recent weather
        }
        const weatherIcon = getWeatherIcon(weatherAtNoon.weather); // Get the appropriate weather icon
        return {
            temp: weatherAtNoon.temp,
            weather: weatherAtNoon.weather,
            icon: weatherIcon
        };
    };

    const getWeatherIcon = (weather) => {
        if (weather.toLowerCase().includes('clear')) {
            return '☀️'; // Sun icon
        } else if (weather.toLowerCase().includes('cloud')) {
            return '☁️'; // Cloud icon
        } else if (weather.toLowerCase().includes('rain')) {
            return '🌧️'; // Rain icon
        }
        return '❓'; // Default icon if weather is not recognized
    };

    const formatDate = (dateString) => {
        // Return the date string provided by the backend in MM/DD format
        const [year, month, day] = dateString.split('-');  // Split the date string
        return `${month}/${day}`;  // Return in MM/DD format
    };

    const getDayOfWeek = (dateString) => {
        // Create a Date object from the date string, appending "T00:00:00" to prevent timezone issues
        const date = new Date(`${dateString}T00:00:00`);  // Force it to be parsed as local time without timezone shift
        return new Intl.DateTimeFormat('en-US', { weekday: 'short' }).format(date);  // Return day of the week
    };

    return (
        <div className="app">
            <div className="container">
                {/* Info Button */}
                <button className="info-button" onClick={toggleDropdown}>
                    Info
                </button>
                {dropdownVisible && (
                    <div className="dropdown">
                        <p>The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career. From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations. 
                        Our Product Manager Accelerator community are ambitious and committed. Through our program they have learnt, honed and developed new PM and leadership skills, giving them a strong foundation for their future endeavours.</p>
                    </div>
                )}

                {/* Header Section */}
                <header className="top">
                    <h1>Weather App by Emile Eid </h1>
                </header>

                {/* Location Input Section */}
                <div className="location">
                    <input 
                        type="text" 
                        value={city} 
                        onChange={e => setCity(e.target.value)} 
                        placeholder="Enter City" 
                    />
                    <button onClick={fetchWeather}>Get Weather</button>
                </div>

                {/* Weather Display Section */}
                <div className="middle">
                    {weatherData[selectedDate] && (
                        <div className="weather-display">
                            {/* Center-aligned Day, Date, and Current Temp */}
                            <div className="current-weather">
                                <h2>{getDayOfWeek(selectedDate)} {formatDate(selectedDate)}</h2> {/* Display day and date */}
                                <div className="current-temp">
                                    {getWeatherDetailsForDay(weatherData[selectedDate]).temp}°F
                                </div>
                                <div className="current-temp">
                                    {getWeatherDetailsForDay(weatherData[selectedDate]).weather}
                                    {getWeatherDetailsForDay(weatherData[selectedDate]).icon}
                                </div>
                            </div>

                            {/* Hourly Forecast Table */}
                            <div className="forecast-table">
                                <table>
                                    <thead>
                                        <tr>
                                            <th>Time</th>
                                            <th>Temperature (°F)</th>
                                            <th>Feels Like (°F)</th>
                                            <th>Humidity (%)</th>
                                            <th>Wind (mph)</th>
                                            <th>Weather</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {weatherData[selectedDate].map((forecast, index) => (
                                            <tr key={index}>
                                                <td>{forecast.time}</td>
                                                <td>{forecast.temp}°F</td>
                                                <td>{forecast.feels_like}°F</td>
                                                <td>{forecast.humidity}%</td>
                                                <td>{forecast.wind_s} mph {forecast.wind_d}</td>
                                                <td>{forecast.weather} {getWeatherIcon(forecast.weather)}</td>
                                            </tr>
                                        ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    )}
                </div>

                {/* Date Navigation Section */}
                <div className="bottom">
                    {Object.keys(weatherData).map((date) => {
                        const forecasts = weatherData[date];
                        const { temp, icon } = getWeatherDetailsForDay(forecasts);
                        return (
                            <button 
                                key={date} 
                                className="date-button" 
                                onClick={() => handleDateChange(date)}
                            >
                                {getDayOfWeek(date)} {formatDate(date)} {/* Display day and formatted date */}
                                <br />
                                {temp}°F {icon}
                            </button>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

export default App;