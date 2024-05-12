######################### Arrays #########################
from array import array
# typecode important in arrays
# syntax array(typecode, iterables)
numbers = array('i', [1, 2, 3])  # i is typecode
numbers.append(4)
print(numbers)

# numbers[0] = 2.3 #TypeError
