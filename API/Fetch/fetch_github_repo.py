# Task:
# Fetch Repository name, Programming language, Number of stars, Repository URL

import requests

username = input("Enter the username you want to search: ").strip()

url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("Username:", data["login"])
        print("Total Repos:", data["public_repos"])

        repos_url = f"https://api.github.com/users/{username}/repos"
        fetch = requests.get(
            repos_url,
            params={"per_page": 100},
            timeout=10
        )

        if fetch.status_code == 200:
            repos = fetch.json()

            if repos:
                for project in repos:
                    print("Name:", project["name"])
                    print(
                        "Programming Language:",
                        project.get("language") or "Not specified"
                    )
                    print("Stars:", project["stargazers_count"])
                    print("URL:", project["html_url"])
                    print()
            else:
                print("No public repositories found.")

        else:
            print("Failed to fetch repositories:", fetch.status_code)

    elif response.status_code == 404:
        print("GitHub user not found.")

    else:
        print("Failed to fetch profile:", response.status_code)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
