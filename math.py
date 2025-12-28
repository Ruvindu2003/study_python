import math 
import random 
import json
import datetime

print(math.sqrt(16))

name=["Alice", "Bob", "Charlie", "Diana"]
numbers=[0,1,2,3,4,5,6,7,8,9]
random_name=random.choice(name)
print(random_name)

numberss=random.choice(numbers)
print(numberss)


name_dict={"name":"Buddima","age":22,"city":"Colombo"}
name_json=json.dumps(name_dict)
print(name_json)

print(datetime.datetime.now())