# import requests


# response = requests.get('https://api.github.com')
# print(response.status_code)



# first_name = "John"
# last_name = "Doe"


# dash="-" * 10
# print(first_name +" " + last_name)
# print(dash)

# print(len(first_name) + len(last_name))


# name ="RUVINDU"
# name.lower()
# print(name.lower())
# print(name.upper())

# sententce = "The quick brown fox jumps over the lazy dog"
# print(sententce.title())


# temprage_celsius = 70

# if temprage_celsius > 30:
#     print("It's a hot day")
# elif temprage_celsius > 20:
#     print("It's a warm day")
# else:
#     print("It's a cold day")


for i in range(5):
    print(i)
print("Hello, World!")

customer=[1,"hii",4,5,6]

customer[0]="Buddima"
customer.append("New Value")
print(customer)


MyList=["Ruvindu",25,True,5.9]


person={
    "name":"Ruvindu",
    "age":25,
    "is_student":True
}

print(person["name"])
print(person["age"])
print(person["is_student"])

print(len(person))

person.get("name")
person["age"]=26
person["is_student"]=False


print(person)
person["address"]="New Address"
print(person)