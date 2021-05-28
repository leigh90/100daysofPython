import requests
import json

MY_LAT=-1.292066
MY_LNG = 36.821945
FORMAT = 0

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# # <Response [200]>
# # returns response code
# # 100 wait
# # 200 OK
# # 300 Not AUTHORISED
# # 400 You screwed up
# # 500 I (the server) screwed up


# # response.raise_for_status()
# data = response.json()
# # print(data)
# # >>>{'iss_position': {'latitude': '46.3108', 'longitude': '-148.2789'}, 'timestamp': 1621505762, 'message': 'success'}
# dataone = response.json()['iss_position']
# # print(dataone)
# # >>> {'latitude': '44.5785', 'longitude': '-143.8188'}
# datatwo = response.json()['iss_position']['longitude']
# print(datatwo)
# # >>>-139.5399

# TODO Api Parameters
# Sunrise-sunset regions


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": FORMAT
}
# please note that keys must match those provided in the api documentation
responsetwo = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
print(responsetwo)
responsetwo.raise_for_status()
datathree=responsetwo.json()
sunrise = datathree['results']['sunrise'].split('T')[1].split(':')
sunset = datathree['results']['sunset'].split('T')[1].split(':')

print(sunrise)
print(sunset)




