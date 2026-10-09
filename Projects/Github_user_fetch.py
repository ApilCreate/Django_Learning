import requests

username = input('Enter the username to search for: ').strip()

response = requests.get(f"https://api.github.com/users/{username}")

if response.status_code == 200:
    user = response.json()
    print("Username: ", user['login'])
    print("Name: ", user['name'])
    print("Bio: ", user['bio'])
    print("Repos: ", user['public_repos'])

else:
    print("Status Code Error:", response.status_code)

