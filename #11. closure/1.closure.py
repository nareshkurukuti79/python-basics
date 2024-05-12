######################### Closure ########################

# Nested Functions
# Nonlocal variables

# Example1 a Nested function
def person(address):

    def john():
        print(address)

    john()


person("USA")

# Example2 nonlocal variable modification


def outer():
    number = 85

    def inner():
        nonlocal number
        number = 95
        print("Inner Function:", number)

    inner()


outer()

# Example3 defining a closure


def person(address):
    def john():
        print(address)

    return john


john_address = person("USA")
# print(john_address)
john_address()

# Example4 deleting the original/enclosing scope


def person(address):
    def john():
        print(address)

    return john


john_address = person("USA")

del person

john_address()


######################## When to use closure #####################
def numbers(n):

    def multiply_by(x):
        return x * n

    return multiply_by


three = numbers(3)
fout = numbers(4)
five = numbers(5)

print("output")
print(three)
print(type(three))
print(three(10))
print(fout(40))
print(five(50))

print(three.__closure__)
print(three.__closure__[0].cell_contents)
print(fout.__closure__[0].cell_contents)
