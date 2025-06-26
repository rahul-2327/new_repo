import requests

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)
# "https://httpbin.org/get?key1=value1&key2=value2"

print(r.json())