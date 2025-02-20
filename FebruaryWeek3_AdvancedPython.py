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