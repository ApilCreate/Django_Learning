import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(response) # 200 
# print(response.json()['items'])
for data in response.json()['items']:
    if data["is_answered"] == True:
        print(data['title'])
        print(data['link'])
        print()