# Task 1:
# Print only repositories written in Python.
import requests
username = input("Enter the username you want to search for: ").strip()
url = (f'https://api.github.com/users/{username}')
try:
    response = requests.get(url, timeout = 10)
    if response.status_code == 200:
        fetch = requests.get(url + '/repos', timeout=10)
        data = fetch.json()
        for repo in data:
            if repo.get('language') == 'Python':
                print("Repository Name: ", repo['name'])
                print("Language: ", repo['language'])
                print("URL: ", repo['html_url'])
                print()
    else: print('Failed to fetch data!!')
except requests.exceptions.RequestException as error:
    print("Request Failed!!")

# Task 2:
# Find the repository with the most stars

try:
    if response.status_code == 200:
        if fetch.status_code == 200:
            repos = fetch.json()
            if repos:
                most_starred = max(repos, key=lambda repo: repo["stargazers_count"])

                print("Repository:", most_starred["name"])
                print("Stars:", most_starred["stargazers_count"])
                print("URL:", most_starred["html_url"])
            else:
                print("No public repositories found.")
        else:
            print("Failed to fetch repositories:", fetch.status_code)
    else:
        print("Failed to fetch profile:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Failed to request:", error)

# Task 3:
# Write a script that asks for a GitHub username and prints the 5 most recently updated repositories, including their names and update dates.

if response.status_code == 200:
    new_url = (url + '/repos')
    parameter = {'per_page': 5, 'sort': 'updated', 'page':1}
    sort = requests.get(new_url, params=parameter, timeout=10)
    if sort.status_code == 200:
        repos = sort.json()
        if repos:
            for repo in repos:
                print("Repository:", repo["name"])
                print("Last Updated:", repo["updated_at"])
                print("URL:", repo["html_url"])
                print()
    else: print('Failed to fetch data!!')
else: print('Failed to request data!!')