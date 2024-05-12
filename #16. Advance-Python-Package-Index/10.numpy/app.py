######################### NumPy ###############################

# pipenv install numpy

import numpy as np


# creating a simply array
array = np.array([2, 4, 1])

# creating a multidimensional array
array_mul = np.array([1, 2, 3, 4], [5, 6, 7, 8])
print(array_mul)
print(array_mul.shape)

# NumPy Helper Methods
# zeros()
array_zeros = np.zeros((4, 6))  # 4, 6 dimensions of the array
print(array_zeros.shape)

# ones()
array_ones = np.ones((4, 6), dtype=int)
print(array_ones)

# full()
array_full = np.ones((4, 6), 11,  dtype=int)
print(array_full)

# random.random()
array_rand = np.random.random((4, 6))
print(array_rand)

# accessing the number a the first row and first col
print(array[0, 0])

# uising a comparison operator
print(array > 0.5)

# boolean indexing
print(array[array > 0.3])

# array computational functions
# sum()
array = np.array([1, 2, 3, 4, 5, 2.1, 3.9, 5.5, 11.8, 15.7, 13.3])
print(np.sum(array))

# floor()
array = np.array([1, 2, 3, 4, 5, 2.1, 3.9, 5.5, 11.8, 15.7, 13.3])
print(np.floor(array))

# ceil()
array = np.array([1, 2, 3, 4, 5, 2.1, 3.9, 5.5, 11.8, 15.7, 13.3])
print(np.ceil(array))

# round()
array = np.array([1, 2, 3, 4, 5, 2.1, 3.9, 5.5, 11.8, 15.7, 13.3])
print(np.round())

# Arithmetic Operation Between Numbers and Arrays
first_array = np.array([111, 333, 555])
second_array = np.array([222, 444, 666])

print(first_array + second_array)
print(first_array + 1)

# unit conversion (Length)
feet = np.array([1, 3, 4, 5, 6])
cm = feet * 30.48
inch = feet * 12
meter = feet * 0.3048
print(cm)
