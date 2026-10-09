import json
import requests

url = ('https://api.github.com/users/ApilCreate')

response = requests.get(url, timeout=10)

if response.status_code == 200:
    data = response.json()

    print("Username: ", data["login"])
    print("Location: ", data["location"])
    print("Public repositories:", data["public_repos"])

else:
    print("Failed to fetch user:", response.status_code)


# OR 
# This only works when the user in inside the fetched list
url = ('https://api.github.com/users')

response = requests.get(url, timeout=10)

if response.status_code == 200:
    users = response.json()

    for user in users:
        if user["login"] == "ApilCreate":
            print("UserName: ", user['login'])
            print("Total Repos: ", user['public_repos'])
            print("Bio: ", user['bio'])
            break

    else:
            print("Couldn't find the user")

else:
     print("Status Code error")