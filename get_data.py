import requests
from datetime import datetime, timedelta

today = datetime.now()
print("Today's date:", today.strftime("%Y-%m-%d"))

weekago = today - timedelta(days=7)
print("Date one week ago:", weekago.strftime("%Y-%m-%d"))

url=f'https://api.open-meteo.com/v1/forecast?latitude=48.5&longitude=2.21&hourly=temperature_2m&start_date={weekago.strftime("%Y-%m-%d")}&end_date={today.strftime("%Y-%m-%d")}'
response=requests.get(url)
data=response.json()
print(data)
