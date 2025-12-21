import requests


response = requests.get('https://api.github.com')
print(response.status_code)



first_name = "John"
last_name = "Doe"


dash="-" * 10
print(first_name +" " + last_name)
print(dash)

print(len(first_name) + len(last_name))


name ="RUVINDU"
name.lower()
print(name.lower())
print(name.upper())

sententce = "The quick brown fox jumps over the lazy dog"
print(sententce.title())