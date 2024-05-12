################ Introduction to Decorators ################
# __call__() ->>>> callable

# Example 1 a decorator

# decorator
def operation(func):

    def increment():
        print("\n")
        print("before the func")

        # the exectuion of the decrement function
        func()

        print("\n")
        print("after the func")

    return increment

# decorated


def decrement():
    print("\n")
    print("The number has been decremented")


decorated_function = operation(decrement)
decorated_function()

# the syntactic sugar of a decorator


def operation(func):

    def increment():
        print("\n")
        print("before the func")

        # the exectuion of the decrement function
        func()

        print("\n")
        print("after the func")

    return increment


@operation
def decrement():
    print("\n")
    print("The number has been decremented")


decorated_function = operation(decrement)
print("output from the syntactic method")


decrement()

# Note: @operation == decrement = operation(decrement)


# Decorating Functions with Parameters and also using decorator
def operation(func):

    def inner(x, y):
        print("\n")
        print(f"{x} / {y} =")

        if y == 0:
            print("\n")
            print("cannot divide by zero")
            return

        return func(x, y)

    return inner


@operation
def divide(x, y):
    print(x/y)


print("\n")
divide(2, 5)
print("\n")
divide(4, 4)
print("\n")
divide(40, 0)


# (*args)
def multiply(func):

    def digits(*args):

        func(*args)

    return digits


@multiply
def operation(x, y, z):
    print(x * y * z)


operation(10, 20, 30)

# *args


def do_arithemtic(func):

    def number(*numbers):

        func(*numbers)

    return number


@do_arithemtic
def operation(x, y, z, a, b, c):
    print((a/b) + z + (x+y)/c)


operation(100, 200, 300, 400, 500, 600)


# (**kwargs)
def do_arithmetic(func):
    def number(**kwargs):
        func(**kwargs)
    return number


@do_arithmetic
def operation(x, y, z, a, b, c, m, n, o):
    print(((a/b) * m + z * n + (x/o+y)/c+m*n+o)/(o-n))


operation(x=100, y=200, z=300, a=100, b=400, c=500, m=700, n=800, o=900)


# Chaining Decorator

def info_name(func):

    def full_name(*args):

        func(*args)

    return full_name


def info_last_name(func):

    def full_name(*args):

        func(*args)

    return full_name


@info_name
@info_last_name
def info(name, lastname):
    print(f"my full name is {name} {lastname}")


info("Naresh", "Kurukuti")
