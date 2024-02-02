import requests


def find_country(city):
    url = 'https://countriesnow.space/api/v0.1/countries/population/cities'
    data = {
        "city": city
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return(response.json()["data"]["country"])
    else:
        return "?"

