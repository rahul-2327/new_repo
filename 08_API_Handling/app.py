import requests as req

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = req.get(url)
    data = res.json()
    # print(res)
    # print(type(res))

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]

        return username,country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:

        username,country = fetch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
        print(f"USERNAME type: {type(username)}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()