# Weather-report
Get real-time weather data, wind speed, and pressure for London, US. Simple web interface allows user interaction to fetch hourly forecasts using OpenWeatherMap API

This is a simple Flask web application that allows users to fetch weather data, wind speed, and pressure for a specific date and time before 2019 in London, US, using the OpenWeatherMap API.

## Features

- Get weather data (temperature) for a specific date and time in London, US.
- Get wind speed data for a specific date and time in London, US.
- Get pressure data for a specific date and time in London, US.
- Web-based interface for user interaction.
- Real-time data fetched from the OpenWeatherMap API.

## Requirements

- Python 3.8+
- Flask
- Requests

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/WeatherDataFlaskApp.git
cd WeatherDataFlaskApp
Install the required packages using pip:
bash
Copy code
pip install -r requirements.txt
Usage
Run the Flask app:
bash
Copy code
python weather_app.py
Access the app in your web browser by navigating to http://127.0.0.1:5000/ (or http://localhost:5000/).

Select an option from the dropdown menu:

Option 1: Get weather data (temperature)
Option 2: Get wind speed data
Option 3: Get pressure data
Option 0: Exit
Enter a date and time in the format "YYYY-MM-DD HH:MM:SS" and click "Submit."

The app will display the corresponding weather data, wind speed, or pressure for the specified date and time.

API Key
Please note that this app uses the OpenWeatherMap API to fetch real-time weather data. You need to obtain your API key from OpenWeatherMap (https://openweathermap.org/api) and replace 'YOUR_API_KEY' in the weather_app.py file with your actual API key.

You can modify.
