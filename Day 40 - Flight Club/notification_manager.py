import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.my_email = os.environ.get("GMAIL_ID")
        self.password = os.environ.get("GMAIL_PASSWORD")

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message_body, email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs=email,
                                msg=f"Subject:Flight Deals\n\n{message_body}"
                                )