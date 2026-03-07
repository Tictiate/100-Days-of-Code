import os
import requests
from dotenv import load_dotenv
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 190
AGE = 20

load_dotenv()

# Prompting AI to get workout information

base_url = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("APP_KEY")
}

query = input("Tell me which exercises you did: ")

params = {
    "query" : query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=f"{base_url}/v1/nutrition/natural/exercise", json=params, headers=headers)
original_data = response.json()
data = original_data["exercises"][0]

print(data)


# Tracking Details into a Google Sheet

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%I:%M %p")
post_endpoint = "https://api.sheety.co/e2379b90be0ad1cf36d6e3b12dd33f25/workoutTracker/workouts"

token = os.environ.get("TOKEN")
headers = {
    "Authorization": f"Bearer {token}"
}

params = {
    "workout":
        {
            "date": date,
            "time": time,
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        }
}

response = requests.post(url=post_endpoint, json=params, headers=headers)
response.raise_for_status()