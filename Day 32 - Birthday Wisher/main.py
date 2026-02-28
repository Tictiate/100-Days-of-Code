import datetime as dt
import pandas
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day
original_data = pandas.read_csv("birthdays.csv")
data = original_data.to_dict(orient="records")

def send_email(name, email):
    receiver_name = name
    receiver_email = email
    letter = random.randint(1,3)

    with open(f"letter_templates/letter_{letter}.txt") as file:
        message = file.readlines()
        message[0] = message[0].split()
        message[0][1] = f" {name},\n"
        message[0] = message[0][0] + message[0][1]
        message = "".join(message)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=receiver_email,
                            msg=f"Subject:{message}"
        )

for record in data:
     if record["month"] == month and record["day"] == day:
         send_email(record["name"], record["email"])