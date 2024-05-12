############  Exception Handling Part 1 ###############

import sys

# Example try..except

try:
    age = int(input("Age: "))
except:
    print("Please enter a valid age")

print("No exception")

# Example2 try...except...else
try:
    age = int(input("Age: "))
except ValueError:
    print("Please Enter a Valid age")
else:
    print("No Errors Here")

# Example3 try..except..else
try:
    age = int(input("Age: "))
except ValueError as exp_error:
    print("please enter a valid age")
    print(exp_error)
    print(type(exp_error))
else:
    print("N Error Here")

# Example4 try....except
random_list = ["a", 0, 2]

for entry in random_list:
    try:
        print("The entry is: ", entry)
        r = 1/int(entry)
        break
    except:
        print("oops!", sys.exc_info()[0], "occured")
