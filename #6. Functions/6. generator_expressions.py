############################ Generator Expressions #######################

# syntax

# generator_expression = (expression for item in iterable if condition)


# list comprehension

from sys import getsizeof
numbers = [x*2 for x in range(15)]
print(numbers)
print(type(numbers))

# generator object
numbers = (x*2 for x in range(15))
print(numbers)
print(type(numbers))

for y in numbers:
    print(y)

# getting the size of a generator object
numbers = (x*2 for x in range(10))

print("Genearator Object:", getsizeof(numbers))

# getting the size of a list comprehension
numbers_list = [x*2 for x in range(10)]
print("LCE:", getsizeof(numbers_list))
