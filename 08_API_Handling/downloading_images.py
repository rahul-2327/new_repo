import requests as req
from PIL import Image
from io import BytesIO


url = "https://cdn.wallpaperhub.app/cloudcache/b/d/7/6/4/b/bd764bb25d49a05105060185774ba14cd2c846f7.jpg"

res = req.get(url)
i = Image.open(BytesIO(res.content))

file = open("img.jpg", "wb")
i.save(file)

file.close()

