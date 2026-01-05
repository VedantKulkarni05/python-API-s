import requests
from datetime import datetime

city_cache = {}

def fetch_city_coords(city_name):
    city = city_name.lower().strip()

    if city in city_cache:
        return city_cache[city]

    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()

        if not data.get("results"):
            print("City not found")
            return None

        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]

        city_cache[city] = (lat, lon)
        return lat, lon

    except requests.RequestException:
        print("Failed to fetch city location")
        return None


def fetch_weather(city_name):
    coords = fetch_city_coords(city_name)
    if not coords:
        return None

    lat, lon = coords

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException:
        print("Failed to fetch weather data")
        return None


def show_weather(city_name):
    data = fetch_weather(city_name)
    if not data:
        return

    info = data["current_weather"]

    code_map = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        95: "Thunderstorm"
    }

    condition = code_map.get(info.get("weathercode"), "Unknown")

    print("\n" + "=" * 45)
    print(f" Weather in {city_name.title()}")
    print("=" * 45)
    print(f" Temperature     : {info['temperature']} °C")
    print(f" Wind Speed      : {info['windspeed']} km/h")
    print(f" Wind Direction  : {info['winddirection']}")
    print(f" Condition       : {condition}")
    print("=" * 45)


crypto_map = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp"
}


def fetch_crypto(coin):
    coin_key = coin.lower().strip()
    coin_id = crypto_map.get(coin_key, coin_key)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException:
        print(f"Failed to fetch {coin_key}")
        return None


def compare_cryptos(coin_list):
    print("\n" + "=" * 80)
    print(f"{'Crypto':<12}{'Symbol':<8}{'Price ($)':>15}{'24h Change':>15}{'Market Cap ($)':>20}")
    print("=" * 80)

    for coin in coin_list:
        data = fetch_crypto(coin)
        if not data:
            continue

        usd = data["quotes"]["USD"]

        print(
            f"{data['name']:<12}"
            f"{data['symbol']:<8}"
            f"{usd['price']:>15,.2f}"
            f"{usd['percent_change_24h']:>14.2f}%"
            f"{usd['market_cap']:>20,.0f}"
        )

    print("=" * 80)


def run_app():
    print("\n Real-Time Weather & Crypto Dashboard")

    while True:
        print("\n1. Check Weather")
        print("2. Compare Crypto Prices")
        print("3. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            city = input("Enter city name: ")
            show_weather(city)

        elif choice == "2":
            print(f"Available: {', '.join(crypto_map.keys())}")
            coins = input("Enter crypto names (comma separated): ")
            coin_list = [c.strip() for c in coins.split(",")]
            compare_cryptos(coin_list)

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    run_app()
