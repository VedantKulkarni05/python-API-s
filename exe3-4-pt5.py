import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

# Exercise 3: POST request
response = requests.post(url, json={"title": "My Post", "body": "Content"})

data = response.json()

print("Response:")
print(data)

# Exercise 4: Save to JSON file
with open("results.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved to results.json")
