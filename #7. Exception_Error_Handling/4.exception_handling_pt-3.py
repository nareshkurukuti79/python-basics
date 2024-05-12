############### Exception Handling Part 3 ############

# Example1 try...except...else...finally
try:
    note = open("someFile.txt")
    age = int((input("Age: ")))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("No Exceptions here")
finally:
    note.close()
