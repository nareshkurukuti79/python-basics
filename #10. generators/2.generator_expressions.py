############## Generator Expressions ######################


# creating generator expression

numbers = [1, 2, 11, 9, 5, 2, 0, 12]

# squaring each item using generator expressions
sqrt_nums_GE = (x**2 for x in numbers)
print(sqrt_nums_GE)

print(next(sqrt_nums_GE))
print(next(sqrt_nums_GE))
print(next(sqrt_nums_GE))

# generator expression as function argument
print(sum(x * 2 for x in numbers))
print(max(x**2 for x in numbers))

print(min(x for x in numbers))

##################### Generator Expresssions Advantages #######################
"""
1. Memory Efficient
2. Ease of Implementation
3. Representing Infinite Stream
4. Pipelining Generators
"""


def number_power(max_num):
    n = 0
    while n <= max_num:
        yield 2 ** n
        n += 1


result = number_power(2)
print(next(result))
print(next(result))
print(next(result))


# Representing Infinite Stream
def even_nums(n):
    n = 0
    while True:
        yield n

        n += 2


even_nums = even_nums(10)
print("Output of Inifinite Stream")
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))
print(next(even_nums))


# Pipelining Generators
# Fib Num Series ->>> 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci_numbers(nums):
    x, y = 0, 1

    for _ in range(nums):
        x, y = y, x+y

        yield x


fib_nums = fibonacci_numbers(10)
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
print(next(fib_nums))
