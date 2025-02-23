# Weather App

## Demo
![Weather App Demo](weather-app/Weather-App-demo.gif)

Description

This is a weather application that fetches weather data from OpenWeather API using a Flask backend and a React frontend. Users can enter a city name and get real-time weather updates, including a 5-day forecast with data every 3 hours.

Technologies Used

Frontend: React (Create React App)

Backend: Flask (Python)

API: OpenWeather API

Styling: CSS

Features

Current weather display

5-day forecast with 3-hour intervals

Dynamic weather icons

Interactive UI with dropdown info section

Responsive design

Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/weather-app.git
cd weather-app

2. Backend Setup (Flask)

cd backend
pip install -r requirements.txt
python backend.py

3. Frontend Setup (React)

cd ../frontend
npm install
npm start

4. Running the App in Development Mode

Runs the app in the development mode.
Open http://localhost:3000 to view it in your browser.

The page will reload when you make changes.
You may also see any lint errors in the console.

File Structure

weather-app/
├── backend/       # Flask API
│   ├── backend.py # Main backend server
│   ├── test.py    # Initial weather logic
│   ├── requirements.txt
│   └── ...
├── frontend/      # React Frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── App.js
│   ├── index.js
│   └── ...
├── demo.gif       # App demo
└── README.md

How to Use

Open the app in the browser.

Enter a city name and click "Get Weather".

View current weather and switch between different days.

Click on a forecast button to see detailed 3-hour updates.

Deployment

To deploy this app, you can use:

Frontend: Vercel, Netlify

Backend: Heroku, AWS, Render

Troubleshooting

Ensure all dependencies are installed (pip install -r requirements.txt and npm install).

Check if the OpenWeather API key is correctly set up.

Make sure the backend is running before launching the frontend.

Acknowledgments

Built by Emile Eid

PM Accelerator info is included in the app dropdown

Feel free to contribute and improve this project!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

