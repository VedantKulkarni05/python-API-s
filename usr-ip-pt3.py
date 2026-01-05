import requests


# def get_user_info():
#     print("User Information Lookup ")

#     user_id = input("Enter user ID (1-10): ")

#     url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print(f" User #{user_id} Info ")
#         print(f"Name: {data['name']}")
#         print(f"Email: {data['email']}")
#         print(f"Phone: {data['phone']}")
#         print(f"Website: {data['website']}")
#     else:
#         print(f"\nUser with ID {user_id} not found!")


# def search_posts():
#     print(" Post Search ")

#     user_id = input("Enter user ID to see their posts (1-10): ")

#     url = "https://jsonplaceholder.typicode.com/posts"
#     params = {"userId": user_id}

#     response = requests.get(url, params=params)
#     posts = response.json()

#     if posts:
#         print(f" Posts by User #{user_id} ")
#         for i, post in enumerate(posts, 1):
#             print(f"{i}. {post['title']}")
#     else:
#         print("No posts found for this user.")


# def get_crypto_price():
#     print(" Cryptocurrency Price Checker ")

#     print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
#     coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

#     url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         price_usd = data["quotes"]["USD"]["price"]
#         change_24h = data["quotes"]["USD"]["percent_change_24h"]

#         print(f" {data['name']} ({data['symbol']}) ")
#         print(f"Price: ${price_usd:,.2f}")
#         print(f"24h Change: {change_24h:+.2f}%")
#     else:
#         print(f"\nCoin '{coin_id}' not found!")
#         print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


# def main():
#     while True:
#         print("select an option:")
#         print("1.get user info")
#         print("2. search posts(by user))")
#         print("3. Check crypto price using coinpaprika API")
#         print("4. Exit")

#         choice = input("\nEnter choice (1-4): ")

#         if choice == "1":
#             get_user_info()
#         elif choice == "2":
#             search_posts()
#         elif choice == "3":
#             get_crypto_price()
#         elif choice == "4":
#             print("\nGoodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)


# def fetch_weather():
#     url = "https://api.open-meteo.com/v1/forecast?latitude=19.997&longitude=73.791&current_weather=true"
#     response = requests.get(url)

#     if response.status_code == 200:
#         print("API responding")
#         data = response.json()
#         curr = data["current_weather"]

#         print("weather for static Location (Nashik)")
#         print(f"temp: {curr['temperature']} C")
#         print(f"wind-speed: {curr['windspeed']}km/h")

#     else:
#         print("error in API responding")


# fetch_weather()


def fetch_city_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        print("city not found or enter the correct spelling ")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather = requests.get(weather_url).json()["current_weather"]

    print(f"{city}: {weather['temperature']}C")
    print(f"{city}: {weather['windspeed']}km/h")


City = input("Enter correct city name ")
fetch_city_weather(City)

# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
# Exercise 3: Add input validation (check if user_id is a number)


# exe 2-3
def fetch_todos(completed, usr_id):
    if not str(usr_id).isdigit():
        print("user id should be in digit")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": completed, "userId": int(usr_id)}

    response = requests.get(url, params=params)
    todos = response.json()

    if not todos:
        print("No todos found for this filter")
        return

    for todo in todos:
        print(
            f"ID: {todo['id']} | User: {todo['userId']} | {todo['title']} | Completed: {todo['completed']}"
        )


fetch_todos(False, 1)
fetch_todos(True, 2)
fetch_todos(True, 1)
