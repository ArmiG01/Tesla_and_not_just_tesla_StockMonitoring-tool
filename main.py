import datetime
import requests
from twilio.rest import Client
import time

account_sid = "ACda90cfd3a07ca8c3da52f25401c436b9"
auth_token = "87002d6a53b4e02127d53836dfc7356d"
client = Client(account_sid, auth_token)
data = datetime.datetime.now()
datad = data.strftime("%d")
datam = data.strftime("%m")
datay = data = data.strftime("%y")
COMPANY_NAME = "Tesla Inc"
api = "9c4d556cb5514e8691e41323666ee88c"
PARMS = {
    "apiKey": api,
    "from": f"{datay}-{datam}-{float(datad) - 2}",
    "to": f"{datay}-{datam}-{float(datad) - 1}",
    "q": COMPANY_NAME
}
req = requests.get("http://newsapi.org/v2/everything?", params=PARMS)
newz = req.json()['articles']
neededt = [newz[new]["title"] for new in range(3) if newz[new]]
neededd = [newz[new]["description"] for new in range(3) if newz[new]]
neededurl = [newz[new]["url"] for new in range(3) if newz[new]]

stock = requests.get(
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&floaterval=60min&apikey=V5CS4Q0L7VUPZ2NL").json()
stockyz = stock["Time Series (Daily)"]
first = stockyz[f"20{datay}-{datam}-{int(datad) - 2}"]['2. high']
second = stockyz[f"20{datay}-{datam}-{int(datad) - 1}"]['2. high']
if (float(second) - float(first)) / float(first) * 100 > 0:
    x = abs((float(second) - float(first)) / float(first) * 100)
    message = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[0]}'
             f'description: {neededd[0]}'
             f'url: {neededurl[0]}',
        from_='+15593990789',
        to='+79017069674'
    )
    print(message.status)
    message1 = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[1]}'
             f'description: {neededd[1]}'
             f'url: {neededurl[1]}',
        from_='+15593990789',
        to='+79017069674'
    )
    print(message1.status)
    message2 = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[2]}'
             f'description: {neededd[2]}'
             f'url: {neededurl[2]}',
        from_='+15593990789',
        to='+79017069674'
    )

    print(message2.status)

else:
    x = abs((float(second) - float(first)) / float(first) * 100)

    message = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[0]}'
             f'description: {neededd[0]}'
             f'url: {neededurl[0]}',
        from_='+15593990789',
        to='+79017069674'
    )
    print(message.status)
    message1 = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[1]}'
             f'description: {neededd[1]}'
             f'url: {neededurl[1]}',
        from_='+15593990789',
        to='+79017069674'
    )
    print(message1.status)
    message2 = client.messages.create(
        body=f'Tesla stock price was increased by ⬆️{round(x, 2)}% '
             f'title: {neededt[2]}'
             f'description: {neededd[2]}'
             f'url: {neededurl[2]}',
        from_='+15593990789',
        to='+79017069674'
    )
    print(message2.status)
