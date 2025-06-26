import requests

r = requests.get('https://api.github.com/events')

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

# with open("test.txt", "a") as file:
#     file.write("\n"+str(r.status_code))
#     file.write("\n"+str(r.headers['content-type']))
#     file.write("\n"+str(r.encoding))
#     file.write("\n"+r.text)
