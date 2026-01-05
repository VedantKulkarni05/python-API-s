import requests

# for 200 and 404 reposnse

# def check_url(url):
#     response= requests.get(url)

#     print(f"url {url}")
#     print(f"status code {response.status_code}")

#     if response.status_code ==200:
#         print("API requests worked")
#     else:
#         print("error API request didn't work")

# check_url("https://jsonplaceholder.typicode.com/posts/1")
# check_url("https://jsonplaceholder.typicode.com/posts/999")

# exe3: parsing json data

# print("parsing json data")

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# data = response.json()
# print(f"name: {data['name']}")
# print(f"username: {data['username']}")
# print(f"email: {data['email']}")
# print(f"city: {data['address']['city']}")
# print(f"company name : {data['company']['name']}")


# exe:4


def fetch_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    return requests.get(url).json()


def print_posts(posts, limit=3):
    print(f"User 1 has {len(posts)} posts:")
    for i, post in enumerate(posts[:limit], 1):
        print(f"  {i}. {post['title'][:40]}...")


print("List of Items")
posts = fetch_posts(1)
print_posts(posts)


# exe1 :
def get_usr_phno(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    data = response.json()

    print(f"userID:{data['id']} and phNo:{data['phone']}")

    # exe2:


def check_resource(url):
    response = requests.get(url)
    data = response.json()

    print(f"status code {response.status_code}")

    if response.status_code == 200:
        print(f"API requests worked {data.get('id')}")
    else:
        print("error API request didn't work")


# exe3:
def count_commments(post_id):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    response = requests.get(url)
    comments = response.json()

    count = len(comments)
    print(f"Post ID {post_id} has {count} comments")


get_usr_phno(5)
check_resource("https://jsonplaceholder.typicode.com/posts/1")
check_resource("https://jsonplaceholder.typicode.com/posts/999")

count_commments(1)
