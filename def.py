def is_weather(temperature):
    # fixed naming and parameter name
    if temperature > 30:
        return "It's a hot day"
    else:
        return "It's not a hot day"

print(is_weather(35))  # is_weather(59)


def greet(name, last_name):
    return f"Hello, {name} {last_name}!"


print(greet(name="Buddima", last_name="dharani"))

discount=20

def calculate_price(price):
    tax_rate = 0.2  # 20% tax
    discount = 10
    final_price = price * (1 + tax_rate) - discount
    return final_price

print("final price is:", calculate_price(100))
print("global discount is:", discount)


