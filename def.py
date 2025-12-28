

def isWether(temperage):

    if temperage>30:
        return "It's a hot day"
    else:
        return "It's not a hot day"

print(isWether(35)) #isWether(59) 


def greate(name,last_name):
    return f"Hello, {name} {last_name}!"


print(greate(name="Buddima",last_name="dharani"))



def calculate_price(price):
    tax=0.2
    discount=10
    final_price=price+tax-discount
    print("final price is:",final_price)

print(calculate_price(100))



