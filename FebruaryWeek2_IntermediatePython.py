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

z = lambda a, b, c: a + b + c
print(z(a=1, b=2, c=3))
print(z(1, 2, 3))

get_odd_numbers = lambda x: x % 2 != 0
print(list(filter(get_odd_numbers, numNum)))

greet_lambda = lambda: print('Hello Word')
greet_lambda()

# 1. can be invoked immediately, unlike functions
(lambda x, y: x**y)(5, 3)

# 2. frequently used with map, reduce, filter
from functools import reduce
num = list(range(7))
print(num)
print(list(map(lambda a: a*a, num)))
print(reduce(lambda a, b: a + b, num))
print(list(filter(lambda a: a % 2 == 0, num)))

# 3. can be nested
nested_lambda = lambda a, b: a + b(a)
print(nested_lambda(10, lambda a: a*2))

## Python reduce function
# reduces sequence of elements into single value
# by repeatedly applying a specified function
# reduce(function, iterable [, initializer])
from functools import reduce
num = list(range(6))
def get_sum(x, y):
    # print(f'{x} + {y}')
    return x + y
print(reduce(get_sum, num))
print(reduce(get_sum, num, 15))

# reduce with lambda functions
nums = list(range(0, 13, 2))
print(reduce(lambda x, y: x if x > y else y, nums))     # find max
print(reduce(lambda x, y: x if x < y else y, nums))     # find min



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

## Python collections: list, tuples, sets, dicts
# create empty list, tuples, sets, dicts
# create non-empty list, tuples, sets, dicts
# accessing data: indexing
# changing entries: item assignment
# adding and removing entries
# sorting

# creating empty collections
list1, list2 = [], list()
print(f'{type(list1)} vs {type(list2)}')

tuple1, tuple2 = (), tuple()
print(f'{type(tuple1)} vs {type(tuple2)}')

set1, set2 = {*()}, set()
print(f'{type(set1)} vs {type(set1)}')

dict1, dict2 = {}, dict()
print(f'{type(dict1)} vs {type(dict2)}')

# creating non-empty collections
# casting: set removes duplicates | True same as 1, hence removed
list3 = [1, 2, 2, True, 'a', 'a', 'c']
tuple3 = (1, 2, 2, True, 'a', 'a', 'c')
set3 = {1, 2, 2, True, 'a', 'a', 'c'}

print(f'{list3}\n {list(list3)}\n {list(tuple3)}\n {list(set3)}')
print(f'{tuple3}\n {tuple(list3)}\n {tuple(tuple3)}\n {tuple(set3)}')
print(f'{set3}\n {set(list3)}\n {set(tuple3)}\n {set(set3)}')

dict3 = {1: 'apple', 2: 'cherry', 3: 'strawberry'}
# SyntaxError dict4 = dict([1: 'apple', 2: 'cherry', 3: 'strawberry'])
# Error dict4 = dict((1: 'apple', 2: 'cherry', 3: 'strawberry'))
dict5 = dict({1: 'apple', 2: 'cherry', 3: 'strawberry'})
print(f'{dict3}\n {dict5}')

# accessing data: indexing
# set are unordered, so indexing not possible
print(f'{list3[3]}\n {list3[-1]}\n {list3[0:2]}')
print(f'{tuple3[3]}\n {tuple3[-1]}\n {tuple3[0:2]}')
print(f'{dict3[1]}\n {dict3.keys()}\n {dict3.values()}\n {dict3.items()}')

# changing entries
# Tuple are immutable, sets are unordered
print(list3)
list3[1] = 15
print(list3)

print(dict3)
dict3[1] = 'banana'     # change key
print(dict3)

dict3[4] = dict3.pop(2)     # change entry
print(dict3)

# adding and removing values
# tuple immutable
print(list3)
list3.append('d')
print(list3)

list3.pop(0)    # pop/remove item at index 0
print(list3)

print(set3)
set3.add(12)
print(set3)

set3.pop()      # always removes a random value, unordered so no index use
print(set3)

print(dict3)
dict3.update({4: 'banana'})
print(dict3)

dict3.pop(1)    # remove item at key 1
print(dict3)

# sorting
list4 = [1, 2, 2, 1, 8, 3, 7]
print(list4)
print(list4.sort())     # sort makes changes to original, no return value
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
print(sorted(list4))    # sorted returns a copy, returned sorted copy

tuple4 = tuple(list4)
print(tuple4)
print(sorted(tuple4))   # only possible with sorted, returns sorted list

set4 = set(list4)
print(set4)
print(sorted(set4))     # unordered, returns sorted list

print(dict3)
print(sorted(dict3))
print(sorted(dict3.items()))

## Classes and Objects, Inheritance
# class: blueprint for creating objects
# defines attributes (variables) and methods (functions)
# object: instance of a class
# Inheritance: child class inherits methods and attributes from parent class
# Outstanding concepts: Encapsulation, Polymorphism


class Student:
    def __init__(self, first, last, major):
        self.first_name = first
        self.last_name = last
        self.major = major

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.major}"

    def change_major(self, new_major):
        self.major = new_major
        print(f'Major of {self.first_name} {self.last_name} changed to "{self.major}"')


student_1 = Student('John', 'Deere', 'Computer Science')
print(student_1)
student_1.change_major('Mechanical Engineering')
print(student_1)


class ExchangeStudent(Student):
    def __init__(self, first_name, last_name, major, home_university):
        super().__init__(first_name, last_name, major)
        self.home_university = home_university

    # overrides the __str__ method in parent class
    def __str__(self):
        return f"{super().__str__()} | Home University: {self.home_university}"


exchange_student = ExchangeStudent('Evan', 'Hill', 'Biology', 'Concordia University')
print(exchange_student)

## Python Decorators
# decorator: function that modifies the behaviour of another function without changing structure
# used to wrap another function to add functionality before or after the function call
# a function can take another function | a function can return another function

def decorator_2(outside_func_2):
    def wrapper_2(*args, **kwargs):
        print('Wrapper function 2 executed')
        return outside_func_2(*args, *kwargs)
    # return wrapper_2()
    return wrapper_2

def decorator_1(outside_func_1):
    def wrapper_1():
        print('Wrapper function 1 executed')
        return outside_func_1()
    # return wrapper_1()
    return wrapper_1

def regular_1():
    print('Regular function 1 executed')

# decorator_1(regular_1)
regular_decorated_1 = decorator_1(regular_1)
regular_decorated_1()
#
@decorator_1
@decorator_2
def regular_2():
    print('Regular function 2 executed')

# regular_decorated_2 = decorator_2(decorator_1(regular_1))
# regular_decorated_2()
regular_2()

# using decorators with arguments
@ decorator_2
def regular_3(arg):
    print(f"Regular function executed with arg: {arg}")

regular_3('test')


def greet_decorator(func):
    def wrapper(name):
        print('Starting the function')
        func(name)
        print('Function executed')
    return wrapper

@greet_decorator
def greet(name):
    print(f'Hello {name}')

greet('Semenyo')

# presserving metadata
# wrapper fn overwrites name and docstring of original function
from functools import wraps

def smart_decorator(func):
    @wraps(func)    # preserves metadata
    def wrapper(*args, **kwargs):
        """Docstring for wrapper function"""
        print('Calling function ...')
        return func(*args, **kwargs)
    return wrapper

@smart_decorator
def add(a, b):
    """Adds two numbers"""
    return a + b

print(add.__name__)
print(add.__doc__)