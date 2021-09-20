import requests
import json


FORMAT = 0
# JSON Is easy to use and transport because of its flat structure then you can reconstitute it into whatever you need when you get it e.g a python dictionary
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# # <Response [200]>
# # returns response code
# # 100 wait
# # 200 OK
# # 300 Not AUTHORISED
# # 400 You screwed up
# # 500 I (the server) screwed up

# print(response.status_code)
# if response.status_code == 404:
#     raise Exception('The resource does not exist')
# elif response.status_code == 401:
#     raise Exception('You are not authorised')
# elif response.status_code == 200:
#     print('Eiioooo')

# since we cant write a case by case scenario for each failed response python requests has a raise_for_status() function that raises an error if we dont get a 200 
# it returns a response with details of the error for example
# >>> requests.exceptions.HTTPError: 404 Client Error
# response.raise_for_status()
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json


# data = response.json()
# print(type(data))
# print(data)
# # It returns a dictionary >>> {'iss_position': {'latitude': '46.3108', 'longitude': '-148.2789'}, 'timestamp': 1621505762, 'message': 'success'}
# dataone = response.json()['iss_position']
# print(dataone)
# # # >>> {'latitude': '44.5785', 'longitude': '-143.8188'}
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']

print(f'ISS Longitude is:{longitude}')
# # >>>-139.5399
print(f'ISS Latitude is:{latitude}')
# 
# TODO Api Parameters
# Sunrise-sunset regions
MY_LAT=-1.292066
MY_LNG = 36.821945

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMAT
}
# please note that parameter keys must match those provided in the api documentation
# responsetwo = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
# print(responsetwo)
# responsetwo.raise_for_status()
# datathree=responsetwo.json()
# sunrise = datathree['results']['sunrise'].split('T')[1].split(':')
# sunset = datathree['results']['sunset'].split('T')[1].split(':')

# print(sunrise)
# print(sunset)




