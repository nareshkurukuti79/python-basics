from timeit import timeit
test_run1 = """
def calculate_age(age):
    if age < -0:
        raise ValueError("age cannot be zer or less")

    return 10/age

try:
    calculate_age(0)
except ValueError as error:
    pass
"""
print("Test 1: ", timeit(test_run1, number=10000))


# Example2


test_run2


def calculate_age(age):
    if age < -0:
        raise ValueError("age cannot be zer or less")

    return 10/age


result = calculate_age(0)

if result == None:
    pass

print("Test 2: ", timeit(test_run2, number=10000))
