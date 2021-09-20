import requests

# HTTP Requests 
# requests.get()
# requests.post()
# requests.put()
# requests.delete()

USERNAME = "zawawa"
TOKEN = "8jkjv8klo986g9905ds"

user_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# use a unique username

# response = requests.post(url=user_endpoint,json=user_params)
# print(response)
# print(response.text)


headers = {
    "X-USER-TOKEN":TOKEN
}
# GRAPH
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id":"graph6",
    "name":"Boyfriend-Free",
    "unit":"Days",
    "type":"int",
    "color":"ajisai",

}
pixel_data = {
    "date": "20210908",
    "quantity": "2.1"
}

# Adding dates
from datetime import datetime
today = datetime.now()
# print(today)

yesterday = datetime(2021, 9, 7)
print(yesterday.strftime("%Y-%m-%d"))
update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/'graph6'/{yesterday}"


graph_response = requests.post(graph_endpoint,json=graph_params, headers=headers)
print(graph_response)
print(graph_response.text)




# PUT REQUESTS



