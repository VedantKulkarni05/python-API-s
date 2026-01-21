import requests


def get_user_info():
    print("User Information Lookup")

    user_id = input("Enter user ID (1-10): ")

    if not user_id.isdigit():
        print("User ID must be a number")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nUser #{user_id} Info")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    print("Post Search")

    user_id = input("Enter user ID to see their posts (1-10): ")

    if not user_id.isdigit():
        print("User ID must be a number")
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\nPosts by User #{user_id}")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    print("Cryptocurrency Price Checker")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data["quotes"]["USD"]["price"]
        change_24h = data["quotes"]["USD"]["percent_change_24h"]

        print(f"\n{data['name']} ({data['symbol']})")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


def fetch_city_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        print("City not found. Please check spelling.")
        return

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )
    weather = requests.get(weather_url).json()["current_weather"]

    print(f"\nWeather in {city}")
    print(f"Temperature: {weather['temperature']} °C")
    print(f"Wind Speed: {weather['windspeed']} km/h")


def fetch_todos(completed, usr_id):
    if not str(usr_id).isdigit():
        print("User ID should be a number")
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
            f"ID: {todo['id']} | User: {todo['userId']} | "
            f"{todo['title']} | Completed: {todo['completed']}"
        )


def main():
    while True:
        print("\nSelect an option:")
        print("1. Get user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Get city weather")
        print("5. Search todos")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            city = input("Enter city name: ")
            fetch_city_weather(city)
        elif choice == "5":
            completed = input("Completed? (true/false): ").lower() == "true"
            user_id = input("Enter user ID: ")
            fetch_todos(completed, user_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
