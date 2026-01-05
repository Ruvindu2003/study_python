import requests
from datetime import datetime, timedelta
import pandas as pd



today = datetime.now()
print("Today's date:", today.strftime("%Y-%m-%d"))

weekago = today - timedelta(days=7)
print("Date one week ago:", weekago.strftime("%Y-%m-%d"))

url=f'https://api.open-meteo.com/v1/forecast?latitude=48.5&longitude=2.21&hourly=temperature_2m&start_date={weekago.strftime("%Y-%m-%d")}&end_date={today.strftime("%Y-%m-%d")}'
response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()

temperatures = data['hourly']['temperature_2m']
dates = data['hourly']['time']

# Build a DataFrame with the results
df = pd.DataFrame({
    "date": pd.to_datetime(dates),
    "temperature_C": temperatures
})

# Preview and info
print(df.head())
print(df.dtypes)

# Optional: print per-hour summary
for temp, date in zip(df["temperature_C"].tolist(), df["date"].dt.strftime("%Y-%m-%d %H:%M").tolist()):
    print(f"On {date}, the temperature was {temp}°C")

    df["date "]=pd.to_datetime(df["date"])
    print(df)
