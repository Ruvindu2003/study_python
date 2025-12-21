import requests


response = requests.get('https://api.github.com')
print(response.status_code)



first_name = "John"
last_name = "Doe"


dash="-" * 10
print(first_name +" " + last_name)
print(dash)