from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index") 
def index():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    # Handle empty strings and string with only spaces
    if not bool(city.strip()):
        city ="Lagos"
    
    weather_data = get_current_weather(city)
    #City is not found by API
    if not weather_data['cod'] == 200:
        return render_template(" city_not_found.html")
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        timezone=weather_data["timezone"],
        lat=f"{weather_data['coord']['lat']}",
        lon=f"{weather_data['coord']['lon']}",
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f'{weather_data["main"]["temp"]:.1f}',
        feels_like=f'{weather_data["main"]["feels_like"]:.1f}'
    )




if __name__ == "__main__":
    serve(app, host="localhost", port=5000) 