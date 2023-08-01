from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

def fetch_weather_data():
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Helper function to get the weather data for a specific date
def get_weather_data(date):
    data = fetch_weather_data()
    if data is not None:
        for item in data["list"]:
            if item["dt_txt"].startswith(date):
                return item["main"]["temp"]
    return None

# Helper function to get the wind speed for a specific date
def get_wind_speed(date):
    data = fetch_weather_data()
    if data is not None:
        for item in data["list"]:
            if item["dt_txt"].startswith(date):
                return item["wind"]["speed"]
    return None

# Helper function to get the pressure for a specific date
def get_pressure(date):
    data = fetch_weather_data()
    if data is not None:
        for item in data["list"]:
            if item["dt_txt"].startswith(date):
                return item["main"]["pressure"]
    return None

@app.route("/", methods=["GET", "POST"])
def main():
    result = None

    if request.method == "POST":
        option = int(request.form.get("option"))
        date = request.form.get("date")

        if option == 1:
            temp = get_weather_data(date)
            if temp is not None:
                result = f"The temperature on {date} is {temp}°C."
            else:
                result = "Data not available for the given date."

        elif option == 2:
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                result = f"The wind speed on {date} is {wind_speed} m/s."
            else:
                result = "Data not available for the given date."

        elif option == 3:
            pressure = get_pressure(date)
            if pressure is not None:
                result = f"The pressure on {date} is {pressure} hPa."
            else:
                result = "Data not available for the given date."

        elif option == 0:
            result = "Program terminated."

        return jsonify({"result": result})

    return render_template("index.html")


# Run the Flask app
if __name__ == "__main__":
    app.run()
