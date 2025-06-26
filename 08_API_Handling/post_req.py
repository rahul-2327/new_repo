import requests as req

res = req.post('https://httpbin.org/post', data={'key': 'value'})

print(f"Status code: {res.status_code}")
print(res.text)