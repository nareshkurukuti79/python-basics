######### Recursive Functions ############

import sys
# Example1


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 6
print("The factorial of ", num, "is", factorial(num))

print(sys.getrecursionlimit())


# def recrusor():
#     recrusor()


# recrusor()
