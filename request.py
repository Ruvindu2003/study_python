import requests

latiude = 48.85
longitude = 2.35
url = f"https://api.open-meteo.com/v1/forecast?latitude={latiude}&longitude={longitude}&current_weather=true"
response = requests.get(url)
data = response.json()
print(data)

person = {
    "name": "Ruvindu",
    "age": 22,
}

print(person["name"])
person["age"] = 23
print(person)