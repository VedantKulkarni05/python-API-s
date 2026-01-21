import requests
import os
from datetime import datetime, timedelta, timezone


def fetch_weather(city):
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        print("API key missing")
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.HTTPError as e:
        print(f"API error: {e}")
    except requests.RequestException:
        print("Network error")
    return None


def display_weather():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty")
        return

    data = fetch_weather(city)
    if not data:
        print("Weather data unavailable")
        return

    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]

    # Local time conversion
    tz_offset = data.get("timezone", 0)
    local_time = datetime.now(timezone.utc) + timedelta(seconds=tz_offset)
    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"], tz=timezone.utc
    ) + timedelta(seconds=tz_offset)
    sunset = datetime.fromtimestamp(data["sys"]["sunset"], tz=timezone.utc) + timedelta(
        seconds=tz_offset
    )

    print("=" * 50)
    print(f"Weather Report for {data['name']}, {data['sys']['country']}")
    print(f"Local Time: {local_time.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    print(f"Condition    : {weather['main']} - {weather['description'].title()}")
    print(f"Temperature  : {main['temp']}°C (Feels like {main['feels_like']}°C)")
    print(f"Humidity     : {main['humidity']}%")
    print(f"Wind         : {wind['speed']} m/s (Direction {wind['deg']}°)")
    print(f"Cloudiness   : {data['clouds']['all']}%")
    print(f"Visibility   : {data.get('visibility', 0) / 1000:.1f} km")
    print(f"Sunrise      : {sunrise.strftime('%H:%M')}")
    print(f"Sunset       : {sunset.strftime('%H:%M')}")
    print("=" * 50)


if __name__ == "__main__":
    display_weather()
