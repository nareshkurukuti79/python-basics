################################ zip functions #############################
# In Python, the zip() function is used to combine elements from two or more iterables (e.g., lists, tuples) into tuples. It returns an iterator of tuples where the i-th tuple contains the i-th element

# syntax
# zip(iterable1, iterable2, ...)

# Example1 Two lists in zip()
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

# Using zip() to combine the lists into tuples
zipped_data = zip(names, ages)

# Converting the result to a list (optional)
zipped_list = list(zipped_data)

print("\n output of two list in zip()")
print(zipped_list)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]


# Example2 Three lists in zip()
names = ['Alice', 'Bob', 'Charlie', 'Naresh']
ages = [25, 30, 22]
scores = [95, 88, 75]

zipped_data = zip(names, ages, scores)
zipped_list = list(zipped_data)

print("\n output of three list in zip()")
print(zipped_list)
# Output: [('Alice', 25, 95), ('Bob', 30, 88), ('Charlie', 22, 75)]


# Example3 unzipping the values using the zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

unzipped_coordinates, unzipped_values = zip(*result_list)


# unziiped iterables are converted to a tuple
# You can also use the * unpacking operator to unzip a zipped iterable:
print("unzipped coordinates: ", unzipped_coordinates)
print("unzipped values: ", unzipped_values)
