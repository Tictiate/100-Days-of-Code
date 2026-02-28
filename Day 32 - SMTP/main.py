import smtplib
import datetime as dt
import random
my_email = "ishaangandhi2006@gmail.com"
password = "ican ttell yout hepa"

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 5:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
        )