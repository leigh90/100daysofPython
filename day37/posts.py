import requests
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
    "id":"graph2",
    "name":"Boyfriend-Free",
    "unit":"Days",
    "type":"int",
    "color":"ajisai",

}

graph_response = requests.post(graph_endpoint,json=graph_params, headers=headers)
print(graph_response)
print(graph_response.text)