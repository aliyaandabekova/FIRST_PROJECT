import requests

response = requests.get('https://api.github.com/repos/aliyaandabekova/FIRST_PROJECT/commits').json()

for r in response:
    print(r['sha'],r['commit']['author']['name'])