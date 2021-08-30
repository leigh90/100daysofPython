import os
import requests


# TODO make calls to the apis 

# STOCK API Response
STOCK_API_KEY= os.environ['STOCK_API_KEY']
STOCK = "TSLA"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=compact&apikey={STOCK_API_KEY}"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&outputsize=compact&apikey=3H9CTRO4PR44F4I2
# 1. Get today's date 
import datetime
from datetime import date
today = date.today()
yesterday = today - datetime.timedelta(days=1)
print(today)
print(yesterday)

# TODO Check difference in price between market close yesterday and today
# Calculate the price difference in percentage 
# stock_response = requests.get(url=STOCK_ENDPOINT)
# print(stock_response)
# stock_data = stock_response.json()
# # # print(stock_data)
# tesla_today = float(stock_data["Time Series (Daily)"]["2021-08-24"]["4. close"])
# tesla_yesterday = float(stock_data["Time Series (Daily)"]["2021-08-23"]["4. close"])

# # print(sample)
# print(tesla_today)
# print(type(tesla_today))

# print(tesla_yesterday)
# difference = tesla_today - tesla_yesterday
# print(difference)

# # Calculate the percentage increase or decrease
# import math

# percentage_diff =(difference / tesla_yesterday) * 100
# print(percentage_diff)
# print(round(percentage_diff, 2))



# NEWSAPI Response
COMPANY_NAME = "Tesla Inc"
# NEWS_API_KEY = os.environ['NEWS_API_KEY']
# NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2021-08-23&apiKey={NEWS_API_KEY}"
# stock_params = {
#     "lat": 1.2921,
#     "lon": 36.8219,
#     "exclude": ["current","minutely","daily,alerts"],
#     "appid": API_KEY
# }

# news_response = requests.get(url=NEWS_ENDPOINT)
# print(news_response)
# news_data = news_response.json()
# news_articles = news_data['articles']
# title = 0
# for article in news_articles: 
#     title = article["title"]
#     link = article["url"]



# SMS Update
from twilio.rest import Client
import os

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body=f"Tesla Stock is {percentage_diff} \n  Headlines: {title} {link}  ",
#                      from_='+13126265243',
#                      to='+254700116007'
#                  )

# print(message.sid)
# print(message.status)


# The full Soln

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(stock_response.json())
stock_data = stock_response.json()["Time Series (Daily)"]
# data_list = [new_item for item in data]

stock_data_list = [value  for key,value in stock_data.items()]
# print(stock_data_list)
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_data)
print(yesterday_closing_price)

day_before = stock_data_list[1]
day_before_closing_price = day_before['4. close']
print(day_before)
print(day_before_closing_price)


























































## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

