import os
from operator import imod

import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWIL_ACCOUNT_SID")
auth_token = os.environ.get("TWIL_AUTH_TOKEN")

params = {
    "lat": 38.969017,
    "lon": -0.185157,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= params)
response.raise_for_status()

weather_data = response.json()

carry_umbrella = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        carry_umbrella = True

if carry_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid="MGc62d804c058bb2eddf19bc7e7c783ffc",
        body="It's going to rain today. Remember to bring an ☔️",
        to=os.environ.get("PHONE_NUMBER")
    )
    print(message.status)