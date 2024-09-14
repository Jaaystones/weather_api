from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Lagos"):
    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL").format(API_KEY=api_key, city=city)
    weather_data = requests.get(api_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n---Get Current Weather Conditions---\n")

    city = input("\nPlease enter a city name: ")

    # Handle empty strings and string with only spaces
    if not bool(city.strip()):
        city ="Lagos"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
    
