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
data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_close = float(yesterday_data["4. close"])
day_before_yesterday_close = float(day_before_yesterday_data["4. close"])

dif = (yesterday_close - day_before_yesterday_close)
up_down = None
if dif > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

dif_percent = round(dif / yesterday_close) * 100
print(dif_percent)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
formatted_articles = []
def get_news():
    global formatted_articles
    params = {
        "apiKey": os.environ.get("NEWS_API"),
        "qInTitle": COMPANY_NAME,
        "language": "en",
    }
    url = "https://newsapi.org/v2/everything"
    response = requests.get(url, params)
    articles = response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles =[f"{STOCK}: {up_down}{dif_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_message():
    account_sid = os.environ.get("TWILIO_ACC")
    auth_token = os.environ.get("TWILIO_API")
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        msg = client.messages.create(
            from_='+13254686852',
            body=article,
            to=os.environ.get("PHONE_NUMBER")
        )

if abs(dif_percent) > 5:
    get_news()
    send_message()


