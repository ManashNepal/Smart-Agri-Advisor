import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather_forecast(location : str):
    url = f"http://api.weatherapi.com/v1/forecast.json?q={location}&days=3&key={WEATHER_API_KEY}"

    try:
        response = requests.get(url=url)
        response.raise_for_status()

        data =response.json()
        forecast_list = []

        for day in data["forecast"]["forecastday"]:
            forecast_list.append({
                "date" : day["date"],
                "temp": day["day"]["avgtemp_c"],
                "rain_mm": day["day"]["totalprecip_mm"],
                "condition": day["day"]["condition"]["text"]
        })
            
        return forecast_list
    
    except Exception as e:
        print(f"error: {str(e)}")

