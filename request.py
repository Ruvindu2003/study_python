import requests


def getweather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]["temperature"]


pari_temp=getweather("48.5", "2.21")
print(pari_temp)
londn_temp=getweather("51.5", "-0.12")
print(londn_temp)
srilanka_temp=getweather("7.87", "80.65")
print(srilanka_temp)


print(f"temperature in Paris is {pari_temp}°C")
print(f"temperature in London is {londn_temp}°C")
print(f"temperature in Sri Lanka is {srilanka_temp}°C")

person = {
    "name": "Ruvindu",
    "age": 22,
}

print(person)

print(person["name"],)
person["age"] = 23
print(person)