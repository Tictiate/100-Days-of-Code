import os
import time
import requests
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e2379b90be0ad1cf36d6e3b12dd33f25/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/e2379b90be0ad1cf36d6e3b12dd33f25/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.emails = []
        self.headers = {
            "Authorization": f"Basic {os.environ['SHEETY_PASSWORD']}"
        }

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)
            time.sleep(1)

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.headers
        )
        print(f"Row {row_id} price updated in Sheety to ₹{new_price}")

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        for user in data["users"]:
            self.emails.append(user["whatIsYourPreferredEmailAddress?"])

        return self.emails