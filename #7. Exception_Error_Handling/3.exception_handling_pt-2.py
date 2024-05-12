############## Exception Handling Part 2 ###############

# Example1 get a ZeroDivisionError

try:
    age = int(input("Age: "))
    x = 10/age
except ValueError:
    print("Please enter a valid age")
else:
    print("No Errors here")

# Example2 Resolving a ZeroDivisionError

try:
    age = int(input("Age: "))
    x = 10/age
except ValueError:
    print("Please enter a valid age")
except ZeroDivisionError:
    print("please enter a valid age")
else:
    print("No Errors Here")

# Example3 Creating a tuple of errors
try:
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("Please Enter a Valid age")
else:
    print("No Errors Here")
