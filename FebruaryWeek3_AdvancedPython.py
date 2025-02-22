## February Week 3: Advanced Python
# https://youtube.com/playlist?list=PL30AETbxgR-eczfB1DsAyr4L3_oyDIWAA&si=5rycPWkkK2rT4Cst

# Alt + Shift + E : run highlighted line
# Ctrl + Shift + F10: run current file
# Shift + F6: refactor variable name
# Ctrl + K: Commit

## Return vs Yield in Ptyhon!

def return_example():
    numbers = []
    for i in range(1, 6):
        numbers.append(i)
    return numbers

# No return: <class 'NoneType'>
# Several returns: Tuple
print(type(return_example()))
print(return_example())


# Yield: produce intermediate values when a function runs
# generator functions: generator objects - iterable
def yield_example():
    numbers = []
    for i in range(1, 6):
        yield i
    print('Finished!')

print(type(yield_example()))
print(yield_example())
# <class 'generator'>
# <generator object yield_example at 0x000001ABD50AB370>

for i in yield_example():
    print(i)

# Key differences between Yield and Return
# 1. Stop vs. Interrupt
#   Return: function stops when Return statement is reached
#   Yield: 'interrupt' a function without loosing local variables
# 2. Code after yield/return statements
#   Return: code after return statement is not accessible
#   Yield: code after yield is accessible
# 3. Output
#   Return: only one output [everything collated into tuple]
#   Yield: interim results
# Other
#   Functions that have a yield statement are called generators
#   Generator functions return iterable generator objects

def count_up_to(n):
    count = 1
    while count <= n:
        yield count     # Produces the value and pauses
        count += 1

gen = count_up_to(5)    # Creates a generator object

# iterate over the generator
for num in gen:
    print(num)


## JSON in Python : Javascript object notation

import json

cur_dict = {
    'name': 'John Doe',
    'age': 30,
    'is_student': False,
    'hobbies': ['swimming', 'biking'],
    'phone_number': None,
    'address': {'city': 'New York', 'zip': '10001'}
}

print(cur_dict)
print(type(cur_dict))

cur_json = json.dumps(cur_dict)
print(cur_json)
print(type(cur_json))

json_data = '{"name": "John Doe", "age": 30, "is_student": false,\
            "hobbies": ["swimming", "biking"], "phone_number": null, \
            "address": {"city": "New York", "zip": "10001"}}'
print(json_data)
print(type(json_data))

new_dict = json.loads(json_data)
print(new_dict)
print(type(new_dict))

# accessing individual pieces
print(new_dict['address']['city'])

# writing JSON to file
with open('dataFeb19.json', 'w') as json_file:
    json.dump(cur_dict, json_file)
print('Saving completed')

# convert it back to json
with open('dataFeb19.json', 'r') as now_json_file:
    cur_data = json.load(now_json_file)
    print(cur_data)

## Context Manegers, with Statement
# Why use Context Managers?
file = open("hello.txt", 'w')
file.write("Hello, World!")
file.close()
print(file.closed)

file = open("helloV2.txt", 'w')
file.write("Hello, World!")
file.write(str(10/0))
file.close()
print(file.closed)
file.close()

# The "with" statement
with open("helloV3.txt", "w") as file:
    file.write("Hello, World! (Context Manager)")
    file.write(str(10/0))
print(file.closed)

# built-in context manager