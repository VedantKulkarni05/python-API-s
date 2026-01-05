import requests
# url = "https://jsonplaceholder.typicode.com/posts/1"

# exe1
# url = "https://jsonplaceholder.typicode.com/posts/5"

# exe2
# url = "https://jsonplaceholder.typicode.com/posts/users"

# exe3
url = "https://jsonplaceholder.typicode.com/posts/999"

response = requests.get(url)

print(f"url:{url}")
print(f"status code {response.status_code}")

print(f"response data ")
print(response.json())




