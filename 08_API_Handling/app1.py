import requests as req

def main():
    # url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    # res = req.get(url)

    web_url = "https://www.codewithharry.com"
    res = req.get(web_url)

    try:
        with open("index.html", "a") as file:
            # file.write(str(res))
            # file.write("\n\n")
            file.write(res.text)
    except Exception as e:
        print("Error: ",e)




if __name__ == "__main__":
    main()