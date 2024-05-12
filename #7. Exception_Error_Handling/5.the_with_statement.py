########### The with statement #########

# openging a single file

try:
    with open("someFile.txt") as note:
        print("note opened")

    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
except FileNotFoundError:
    print("File Was not found")
else:
    print("No Exceptions Here")


# Opening Multiple Files
try:
    with open("someFile.txt") as note, open("anotherFile.txt") as my_note:
        print("note opened")

    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")
except FileNotFoundError:
    print("File Was not found")
else:
    print("No Exceptions Here")
