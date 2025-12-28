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

DISCOUNT = 20  # renamed from 'discount' to avoid shadowing

def calculate_price(price):
    tax_rate = 0.2  # 20% tax
    final_price = price * (1 + tax_rate) - DISCOUNT
    return final_price

print("final price is:", calculate_price(100))
print("global discount is:", DISCOUNT)


def add_numbers(a, b):  # renamed from 'sum' to avoid shadowing built-in
    return a + b

sumcalculation = add_numbers(10, 30)  # moved out of function and fixed spelling
print(sumcalculation)


def multiply_numbers(x, y):  # renamed from 'multiply' to avoid shadowing built-in
    return x * y


result = multiply_numbers(5, 4)  # moved out of function
print(result)


def double(number):
    return number * 2

    result = double(10)  # moved out of function
print(result)

total = double(15) +double(20)
print(total)

if double(7)>10:
    print("Large number")

def sample_function():
        numbers22=[1, 2, 3, 4, 5]
        firstNummber=numbers22[0]
        lastNummber=numbers22[-1]
        print("First number:", firstNummber)
        print("Last number:", lastNummber)

sample_function()  # moved out of function
