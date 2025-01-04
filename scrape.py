import requests

url = 'https://tonari-it.com' 
r = requests.get(url)

print(r.text[:4000])