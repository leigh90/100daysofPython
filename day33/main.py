import requests
import smtplib
import os

my_email=os.environ['MYEMAIL']
my_password=os.environ['MYPASSWORD']
to_email=os.environ['TO_EMAIL']

# send email
def alert():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f'Look up, love'
        )

# TODO Get my position and 
# MY_LAT=-1.292066
MY_LAT=-51.5033
# MY_LNG = 36.821945
MY_LNG = -38.2481
FORMAT = 0

# TODO Get position of ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_position = response.json()
print(iss_position)
iss_latitude = float(iss_position["iss_position"]["latitude"])
iss_longitude = float(iss_position["iss_position"]["longitude"])
# print(iss_latitude)
# print(iss_longitude)

# TODO Check if iss is in my range 
if iss_longitude == MY_LNG and iss_latitude == MY_LAT:
    alert()
else:
    for i in range(-5,6):
        possible_lat = MY_LAT + i
        possible_lng = MY_LNG + 1
        if iss_longitude == possible_lng and iss_latitude == possible_lat:
            alert()
# or 
if MY_LAT -10 <= iss_latitude <= MY_LAT +10 and MY_LNG-10 <= iss_longitude <= MY_LNG+10:
    alert()




