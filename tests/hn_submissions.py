import requests

url = f"https://hacker-news.firebaseio.com/v0/item/33814653.json"
r = requests.get(url)

print(r.json())

