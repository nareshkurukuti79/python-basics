######################### Tuples ###############################
# Example1
tuple_example = (1, 3, 4, 5, 'naresh', 'jklj')
print("\n output of tuple")
print(tuple_example)

# Mixed of Tuple
mixed = ({"Name": "Saitama", "Job": "Hero"}, [
         4, 5, 12], (1.23, 2.13, 3.12), {True, "Asia"})
print("\n output of mixed tuple")
print(mixed)

############### Tuples packing and Unpacking ###################
# If we not use brackets() then its consider as tuple

# Tuple packing
to_do = "buy coffeed", "read a book", "finishing homework"

print(to_do)
print(type(to_do))

# Tuple Unpacking
to_do = "buy coffeed", "read a book", "finishing homework"
to_do1, to_do2, to_do3 = to_do

print("\n output of tuple unpacking")
print(to_do1)
print(to_do2)
print(to_do3)

# Tuple with 1 element

name = ("Naresh")  # this is not tuple
print(name)
print(type(name))

name = ("Naresh",)  # this is tuple
print(name)
print(type(name))

########################## Accessing the Tuple Items ####################
# indexing
mixed = (False, 3.14159, "Python", ["Web", "Mobile"], 45)

print(mixed[0])
print(mixed[1])
# print(mixed[5])#IndexError
# print(mixed["a"]# TypeError)


# Negative Indexing
mixed = (False, 3.14159, "Python", ["Web", "Mobile"], 45)

print(mixed[-1])
print(mixed[-2])
print(mixed[-5])

# slicing
print(mixed[0:2])
print(mixed[:4])
print(mixed[3:1])
print(mixed[:])
print(mixed[:-1])

# Changing Tuple Elements
numbers = (4, 2, 3 [5, 6])
numbers[1] = 10  # TypeError because we can't change the values in the tuples

print(numbers)

numbers[3][2] = 11
print(numbers)


# Re-Assignment of Tuple
numbers = (222, 333, 444)

# Repeating a tuple items
print(("Movie",)*5)

# Tuple concatenation

letters = ("p", "y", "t", "h", "o", "n")
mixed = numbers + letters
print(mixed)

# deleting a tuple entirely
letters = ("p", "y", "t", "h", "o", "n")

del letters
print(letters)

######################## Tuple Methods ###############################
# count()
colors = ("green", "blue", "violet", "lawngreen", "green")

print(colors.count("greeen"))
print(colors.count("red"))

# index()
print(colors.index("blue"))


####################### Tuple Operations #############################
# Tuple Memebership test
colors = ("green", "blue", "violet", "lawngreen", "green")

print("green" in colors)

print("red" in colors)

# Iteration over tuples

for color in colors:
    print(color)
