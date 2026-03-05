import os
from datetime import datetime
import requests
from dotenv import load_dotenv
load_dotenv()

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Push-ups Graph",
    "unit" : "Count",
    "type" : "int",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
put_params = {
    "quantity": "10"
}

# response = requests.put(url=put_endpoint, json=put_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)