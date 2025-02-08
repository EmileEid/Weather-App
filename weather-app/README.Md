Weather App for PM Accelerator Internship Technical Assessment.

I created a weather app that pulls data from openweather using an API

## Demo
![Weather App Demo](Weather-App-demo.gif)



test.py is the file I started with, laying out the logic for my back end. When run it will also display forecast data every 3 hours for the next 5 days. To run git initit pip needs to be installed so you can install and import requests allowing you to use the API.

I have learned Web Development on my own, so I used this opportunity to deepen my knowledge. I spent the last couple of days learning how to use Node.js and Meta's React framework for front-end app development. I took the logic from test.py and developed backend.py, which uses Flask to create a backend server that my front end can communicate with. Flask needs to be installed and imported for this to work. I then applied what I learned over the last few days to develop the front end using React. My name is displayed on the app as it says "Weather App by Emile Eid", and I also included an info button that, when pressed, opens a dropdown providing a description of PM Accelerator.

The app should prompt the user to enter a city and then press the get weather button. Once that button is pressed it retrieves the data from the API and displays the most recent day's forecast in the middle of the page. There are buttons on the bottom of the page that show the forecast for the next 5 days. Those buttons can be clicked on to display the forecast for every 3 hours on that day.

I decided to implement 2 of the above and beyond steps which were to display a 5-day forecast and use icons to enhance weather data.

Check out my demo video for more information!
