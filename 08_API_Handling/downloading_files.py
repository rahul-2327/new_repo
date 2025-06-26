import requests as req

url = ""

res = req.get(url)

file = open("","wb")
file.write(res.content)
file.close()
