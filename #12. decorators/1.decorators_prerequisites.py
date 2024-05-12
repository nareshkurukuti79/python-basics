################################  Decorators PreRequisities ##############################

# Example 1 functions with different names

def name1(name):
    print(name)


name1("John")
name2 = name1
name2("Jane")
print(id(name1("john")))
print(id(name2("Jane")))

# higher order functions


def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def operation(result, x):
    output = result(x)

    return output


number_inc = operation(increment, 50)
number_dec = operation(decrement, 10)

print(number_inc)
print(number_dec)

# A function return another function


def operation():

    def increment():
        print("The number has been added")

    return increment


number_inc = operation()
number_inc()

operation()()  # -->>>>> increment()
