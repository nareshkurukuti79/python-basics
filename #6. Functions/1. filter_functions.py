########################  filter() ##############################
# The filter() function in Python is used to filter elements of an iterable based on a given function. It takes two arguments: the function to test each element and the iterable to be filtered.
# If functions is None, return the items that are true.
# syntax: filter(function, iterable)
# function: A function that tests each element of the iterable. If None, it simply returns the elements of the iterable that are true.
# iterable: The iterable to be filtered.

# To get even numbers by using filter()

numbers = [1, 3, 3, 2, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(is_even, numbers)

even_numbers_list = list(even_numbers)

print("\n output of filter() for the even numbers")
print(even_numbers_list)


# Example2
random_list = [1, 0, "a", False, True, "0"]

filtered_list = filter(None, random_list)

print("\n output of filter when function is None")
print("\n truthly values are")

for value in filtered_list:
    print(value)
