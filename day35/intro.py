import requests
# API keys are used to authenticate api users
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "2b3d82d4ee6d89e96d22b3b2ed08ecfc"

# response = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=-4.043477&lon=39.668205&exclude=current,minutely,daily,alerts&appid=2b3d82d4ee6d89e96d22b3b2ed08ecfc")
# print(response)

# data = response.json()['hourly']
# print(data)

weather_params = {
    "lat": -4.043477,
    "lon": 39.668205,
    "exclude": ["current","minutely","daily,alerts"],
    "appid": API_KEY
}

# better
response = requests.get(OWM_endpoint,params=weather_params)
print(response)
response.raise_for_status()

data = response.json()['hourly']
print(data)