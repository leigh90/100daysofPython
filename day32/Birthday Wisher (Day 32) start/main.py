# Put the quotes in a list

# todo create a python list
all_quotes = []
with open("quotes.txt","r") as lines:
    data = lines.readlines()
    print(data)
    print(type(data))
    
    for element in data:
        all_quotes.append(element.strip())
    print(all_quotes)

    
# Get the current day

import datetime as dt
import smtplib
import os
# from ssl import RAND_status
# my_email = "ashdev755@gmail.com"
# emailpassword = "3WNcmC42voSU"
my_email = os.environ['email']
password =os.environ['emailpassword']
import random

now = dt.datetime.now()
today = now.weekday()

print(today)
print(len(all_quotes))

num = random.randint(0,101)
print(num)
random_quote = all_quotes[num]
print(random_quote)
if today == 0:
    with smtplib.SMTP("smtp.gmail.com") as apple:
        apple.starttls()
        apple.login(user=my_email,password=password)
        apple.sendmail(
            from_addr=my_email, 
            to_addrs="ashdev97@yahoo.com", 
            msg=f"Subject:Welcome to Monday\n\n{random_quote}"
        )
# connection is a variable that could easily be apple
    



# Send motivational email quote
