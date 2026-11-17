from enum import auto

from django.shortcuts import render
import requests 

# Create your views here.
from django.http import HttpResponse
def get_weather(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city,
        "count":1,
        "format": "json"
    }
    geo_response = requests.get(geo_url, params=geo_params,timeout=10)
    geo_response.raise_for_status()
    geo_data = geo_response.json()
    if not geo_data.get("results"):
        return None 
    location = geo_data["results"][0]
    latitude = location["latitude"]
    longitude = location["longitude"]
    city_name = location["name"]
    country = location.get("country","")

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily":("weather_code,"
        "temperature_2m_max,"
        "temperature_2m_min,"
        "precipitation_sum,"
        "wind_speed_10m_max,"),
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m,"
        ),
        "timezone":"auto",
        "forecast_days": 5,

    }
    weather_response = requests.get(weather_url,params=weather_params,timeout=10)
    weather_response.raise_for_status()
    weather_data = weather_response.json()
    current = weather_data["current"]
    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Slight Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        81: "Moderate Rain Showers",
        82: "Violent Rain Showers",
        95: "Thunderstorm",
        96: "Thunderstorm with Hail",
        99: "Heavy Thunderstorm with Hail"
    }
    weather_code = current["weather_code"]
    is_day = current["is_day"]
    condition = weather_codes.get(weather_code,"Unknown_weather")
    daily = weather_data["daily"]
    forecast = []
    for i in range(5):
            forecast.append({
                "date":daily["time"][i],
                "max_temp": daily["temperature_2m_max"][i],
                "min_temp":daily["temperature_2m_min"][i],
                "rain":daily["precipitation_sum"][i],
                "wind":daily["wind_speed_10m_max"][i],
                "condition":weather_codes.get(daily["weather_code"][i],"unknown")
    
            })
    # select the weather icon
    if weather_code == 0:
        icon = "☀️" if is_day else "🌙"
    elif weather_code == 1:
        icon = "🌤️" if is_day else "☁️"
    elif weather_code in [3, 45, 48]:
        icon = "☁️" if is_day else "🌫️"
    elif weather_code in [51, 53, 55, 56, 57]:
        icon = "🌦️"

    elif weather_code in [61, 63, 65, 66, 67, 80, 81, 82]:
        icon = "🌧️"

    elif weather_code in [71, 73, 75, 77, 85, 86]:
        icon = "❄️"

    elif weather_code in [95, 96, 99]:
        icon = "⛈️"

    else:
        icon = "🌡️"
    # select the dynamic background 
    if weather_code in [95,96,99]:
        background_class = "stormy"
    elif weather_code in  [51, 53, 55, 56, 57,
                          61, 63, 65, 66, 67,
                          80, 81, 82]:
        background_class = "rainy"
    elif weather_code in [71, 73, 75, 77, 85, 86]:
        background_class = "snowy"
    elif weather_code in [45,48]:
        background_class = "foggy"
    elif weather_code in [2,3]:
        background_class = "cloudy"
    else:
        background_class = "clear"
    # add day/night information 
    day_status = "Day" if is_day else "Night"



            
    return {
        "city": city_name,
        "country": country,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "feels_like": current["apparent_temperature"],
        "wind_speed": current["wind_speed_10m"],
        "precipitation": current["precipitation"],
        "condition": condition,
        "weather_code":weather_code,
        "background_class": background_class,
        "day_status":day_status,
        "icon":icon,
        "is_day": current["is_day"],
        "latitude": latitude,
        "longitude": longitude,
        "time": current["time"],
        "forecast": forecast,

    }



def home(request):
    city = request.GET.get("city","").strip()
    weather=None 
    error = ""
    if city:
        try:
            weather = get_weather(city)
            if weather is None :
                error = "city not found please try leter."
        except requests.exceptions.Timeout:
            error = "Weather service timed out. Try again."
        except requests.exceptions.RequestException:
            error = "Unable to connect to weather service."
        except (KeyError,ValueError,TypeError):
            error = "Invalid weather data received."
    context = {
        "website_name": "My Weather Website",
        "city": city,
        "weather": weather,
        "error": error,

    }
    return render(request,"weather/home.html",context)



        

        






