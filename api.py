import requests


def get_quality_air(city):
    base_url = "https://api.waqi.info"
    token = '6a83904c5df3e83213e191b295adf644300bde37'
    r = requests.get(base_url + f"/feed/{city}/?token={token}")
    r = r.json()
    if r["status"] == 'ok':
            aqi = r['data']['aqi']
            return aqi
    else:
            return 1

