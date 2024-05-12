######################## Map Functions ###########################
# map(function, iterable, ...)
# function: The function to apply to each item in the iterable(s).
# iterable, ...: One or more iterable(s) whose elements will be processed by the function.

# Iterable
numbers = (1, 2, 3, 4, 5)

# Function


def calculate_square(n):
    return n*n


result = map(calculate_square, numbers)
print(result)

# converting a map object to set
num_set = set(result)
print(num_set)

# converting a map object to a tuple
num_tuple = tuple(result)
print(num_tuple)

# converting a map object to list
num_list = list(result)
print(num_list)

# Example2
letters = ["a", "b", "c", "d"]

result_map = list(map(lambda x: x, letters))
print(result_map)


# Passing mutliple iteraables to the map method
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [7, 8]

result = map(lambda n1, n2: n1 + n2, numbers1, numbers2)
print(result)
