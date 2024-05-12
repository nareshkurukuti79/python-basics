##################### Raising Exceptions ##################

# Example1 Raising an exception

def calculate_age(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")
    return 10/age

# Raising an exception and handling it


def calculate_age(age):
    if age <= 0:
        raise ValueError("age cannot be zero or less")
    return 10/age


try:
    calculate_age(0)
except ValueError as error:
    print(error)
