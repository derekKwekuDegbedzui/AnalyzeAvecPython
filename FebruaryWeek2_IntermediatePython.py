## February Week 2
# https://youtube.com/playlist?list=PL30AETbxgR-cbPtjzN9Sz4WIcl1oBUCcC&si=LyO9_3l__gwAxN0V

# Alt + Shift + E : run highlighted line
# Ctrl + Shift + F10: run current file
# Shift + F6: refactor variable name

# Parameters, arguments, positive and keyword arguments


def get_user_age(name, year_of_birth, current_year=2025):
    return f"{name} is {current_year - year_of_birth} years old."


# parameters: in function definition: name, year_of_birth, etc
# arguments: values passed in the function call
print(get_user_age('Semenyo', 2010))


# SyntaxError: keyword arguments before position arguments


## Optional arugments: *args, **kwargs
# *args: variable length non-keyworded arguments
# ** kwargs: variable length keyworded arguments

# *args: pass unspecified number of positional arguments
def args_example(*args):
    print(type(args))

args_example()  # class tuple

def addition_1(a, b):
    print(a + b)

addition_1(3, 4)
# addition_1(3, 4, 7, 8)     # TypeError expect 2 position arg, got 4

def addition_2(*args):
    cur_sum = 0
    for arg in args:
        cur_sum += arg
    print(cur_sum)

addition_2(3, 4, 7, 8)

# **kwargs: pass unspecified number of keyword arguments

def kwargs_example(**kwargs):
    print(type(kwargs))

kwargs_example()

def kwargs_example_2(**kwargs):
    print(kwargs.values())

kwargs_example_2(keyword_1='a', keyword_2='b')
kwargs_example_2(keyword_1='a', keyword_2='b', keyword_3='c', keyword_4='d')


## Python "Map" function
# Applies a function (built-in, self defined) to all items in an iterable
# Used for transforming without writing explicit loops
# map (function, iterable, ...)

nums = (1, 2, 3, 4, 5, 6)   # can use list, tuple, set
# longer approach: for loop, converted to list comprehension
result = [num * num for num in nums]

# Using map with self defined functions
def square(n):
    return n*n

nums_squred = map(square, nums)
print(list(nums_squred))

# Using map with in-built functions
nums = [-2, -5, 2, 6, 10]
abs_values = list(map(abs, nums))
print(abs_values)

words = ['How', 'are', 'you', 'doing']
word_len = list(map(len, words))
print(word_len)

# Using map with multiple iterables
nums1, nums2 = [1, 2, 3], [4, 5, 6]
print(list(map(lambda x, y: x + y, nums1, nums2)))

nums = (1, 2, 3, 4, 5, 6)
results = list(map(lambda n: n * n, nums))
print(result)


## Python Filter function
# Used to filter elements from an iterable based on truthy
# Truthy values: pos, neg, True > returns true when converted to Boolean | False, 0, None
def get_even_numbers(number):
    return number % 2 == 0

nums_set = {1, 2, 3, 4, 5, 6}
print(set(filter(get_even_numbers, nums_set)))

cur_out = filter(lambda num: num % 2 == 0, nums_set)
print(set(cur_out))

cur_list = [1, 'a', 0, False, True, '0', None, 12, 'Hello']
result = filter(None, cur_list)
print(list(result))


## Lambda

square_it = lambda n: n**2
print(square_it(12))

numNum = [1, 2, 4, 5, 8, 11]
print(list(map(square_it, numNum)))

get_odd_numbers = lambda x: x % 2 != 0
print(list(filter(get_odd_numbers, numNum)))


## Using 'Else' with 'For' Loops
# else block is executed if for loop completes without encoutering a break statement
target = 6
cur_num = [0, 1, 2, 3, 4, 5, 7, 8]
#cur_num.insert(target, target)
for num in cur_num:
    if num == target:
        print(f'Found {target}')
        break   # if break is executed, the else block is skipped
else:
    print(f'{target} not found in the list')

## Zip and Unzip
# zip() combines multiple iterables into single iterables of tuples
# zip(*) reverses the process, to produce individual list or iterables

first_names = ['Albert', 'Bernard', 'Cindy', 'Dandrel']
last_names = ['Amt', 'Bob', 'Cam']
ages = [20, 25, 30]

for i in range(len(last_names)):
    print(f'{first_names[i]} {last_names[i]} is {ages[i]} years old')

for first_name, last_name, age in zip(first_names, last_names, ages):
    print(f'{first_name} {last_name} is {age} years old')

# creating dict
keys = ['name', 'age', 'city']
values = ['Albert', 20, 'Sana ne']
directory = dict(zip(keys, values))
print(directory)

# zip unequal multiple sized iterables
print(list(zip(first_names, last_names)))

# handling unequal lengths
from itertools import zip_longest
print(list(zip_longest(first_names, last_names, fillvalue='N/A')))


# using unzip
full_dir = [
    ('Albert', 'Amt', 23),
    ('Belly', 'Bob', 28),
    ('Cindy', 'Cam', 31),
    ('Debby', 'Dood', 36)
]

first_names, last_names, ages = list(zip(*full_dir))
print(f'{first_names}\n {last_names}\n {ages}')
