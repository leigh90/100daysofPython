import requests
from twilio.rest import Client
import os

# todo API keys are used to authenticate api users
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "2b3d82d4ee6d89e96d22b3b2ed08ecfc"
# response = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=-4.043477&lon=39.668205&exclude=current,minutely,daily,alerts&appid=2b3d82d4ee6d89e96d22b3b2ed08ecfc")
# print(response)

# data = response.json()['hourly']
# print(data)

weather_params = {
    "lat": 1.2921,
    "lon": 36.8219,
    "exclude": ["current","minutely","daily,alerts"],
    "appid": API_KEY
}

# better
response = requests.get(OWM_endpoint,params=weather_params)
print(response)
response.raise_for_status()
# data = response.json()['hourly'][0]['weather'][0]
# print(data)
# Print bring an umbrella if its going to rain.
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella')
    #todo Send SMS Using Twilio
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    FROME = os.environ['TWILIO_FROM_NUMBER']
    TOE = os.environ['TWILIO_TO_NUMBER']

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Its going to ⛈ love, bring an ☔ ",
                        from_=FROME,
                        to=TOE
                    )

    print(message.sid)
    print(message.status)

# Send this as alert as an SMS
