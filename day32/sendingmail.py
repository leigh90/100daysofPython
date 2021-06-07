# SMTP - Simple Mail Transfer Protocol
# smtplib - Python's email library
import smtplib
my_email = "ashdev755@gmail.com"
password = "3WNcmC42voSU"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="ashdev97@yahoo.com", 
    msg="Subject:Subject Line\n\nThis is the body of the email"
    )
connection.close()

# OR

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="ashdev97@yahoo.com", 
        msg="Subject:Subject Line\n\nThis is the body of the email"
    )
# this will open and clse the connection without you having to do it manually using .close()

# DateTime Module
import datetime as dt

now = dt.datetime.now()
print(now)
print(now.year)
year = now.year
day = now.today
# time = now.
if year == 2021:
    print("Still wearing face masks")

month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1993,month=7, day=27)
print(date_of_birth.weekday())