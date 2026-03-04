import os
from datetime import date, timedelta
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
av_api = os.environ.get("AV_API_KEY")
params = {
    "apikey": av_api,
    "symbol": STOCK
}
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
r = requests.get(url, params)
data = r.json()

today = date.today() - timedelta(days=2)
yesterday = today - timedelta(days=1)

today_close = data["Time Series (Daily)"][str(today)]["4. close"]
yesterday_close = data["Time Series (Daily)"][str(yesterday)]["4. close"]

dif = (float(yesterday_close) - float(today_close))/float(yesterday_close) * 100
dif.__round__(2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
message = ""
def get_news():
    global message
    params = {
        "apiKey": os.environ.get("NEWS_API"),
        "language": "en",
        "pageSize": 3,
        "page": 1
    }
    url = "https://newsapi.org/v2/everything?q=tesla&from=2026-02-04&sortBy=publishedAt&"
    response = requests.get(url, params)
    data = response.json()
    article1 = data["articles"][0]["title"] + "\n" + data["articles"][0]["description"]
    article2 = data["articles"][1]["title"] + "\n" + data["articles"][1]["description"]
    article3 = data["articles"][2]["title"] + "\n" + data["articles"][2]["description"]

    message = article1 + "\n" + article2 + "\n" + article3


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_message():
    account_sid = os.environ.get("TWILIO_ACC")
    auth_token = os.environ.get("TWILIO_API")
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        from_='+13254686852',
        body=message,
        to=os.environ.get("PHONE_NUMBER")
    )

if dif >= 5 or dif <= -5:
    get_news()
    if dif >= 5:
        message = f"TSLA: 🔻{dif}\n" + message
    else:
        message = f"TSLA: 🔺{dif}\n" + message
    send_message()


