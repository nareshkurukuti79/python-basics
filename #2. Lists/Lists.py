# SimpleList

numbers = [1, 2, 3, 5]
names = ["John", "Naresh", "Emily"]
print(names)

# A list of lists
likes = [["tv", "gaming"], ["pizza", "pasta"]]
print(likes)

# A list of lists of lists

mixed = [[2, True], "Cat", "Dog", [["Wind", "Water"], ["Earth", "file"]]]
print(mixed)

# A list of identical items
animal = ["cat"]*10
print(animal)

# List merging/concatenation
even_nums = [2, 4, 6, 8, 10]
odd_nums = [1, 3, 5, 7]
cities = ["kabul", "New York", "London"]
boolean = [True, False]

mixed_lists = even_nums + odd_nums + cities + boolean
print(mixed_lists)


########## List Methods & Accessing List Items ######################

collection = [28, "M", 32, "H", "Parrot", "Sea Biscuits"]

print(collection[0])
print(collection[1])
print(collection[2])
print(collection[3])

# List range

print(collection[0:2])
print(collection[0:4])
print(collection[:5])
print(collection[2:])
print(collection[:])  # It will return original list


# You can get the items by step

print(collection[::2])  # You can every alternative item from the List
print(collection[::3])  # You can every third item from the list

# You can get items by step and index

print(collection[2::2])  # It will return from the index 2 and step 2
# The first value (2) represents the starting index of the slice.
print(collection[2:5:2])
# The second value (5) represents the ending index of the slice
# The third value (2) represents the step or stride


################# List Unpacking #######################
numbers = [99, 88, 77]
num1, num2, num3 = numbers
print(num1)
print(num2)
print(num3)

numbers = [23, 49, 85, 1, 2, 3, 4, 5]
num1, num2, *other_num = numbers
print(num1)
print(num2)
print(other_num)

num1, *other_num, num2 = numbers
print(num1)
print(other_num)
print(num2)

num1, num2, *other_num, num3, num4 = numbers
print(num1)
print(num2)
print(other_num)
print(num3)
print(num4)

################ Looping Over Lists #############################
# Example1
letters = ["a", "aa", "bb", "b"]
for letter in letters:
    print(letter)

# Example2
for letter in enumerate(letters):
    print(letter)

# Example3
items = (0, "a")
index, letter = items
print(index, letter)

# Example3
for index, item in enumerate(letters):
    print(index, item)


################# Lists Modifying ################################
# append()
names = ["Jhon", "Mark", "Emily"]

names.append("Naresh")
print(names)

# insert()
fruits = ["Apple", "Orange", "Banana"]

fruits.insert(1, "Lemon")
fruits.insert(0, "Peach")
print(fruits)

# pop()
numbers = [1, 55, 64, 124, 654]

numbers.pop(-1)
print(numbers)

# remove()
fruits = ["Apple", "Orange", "Banana"]
fruits.remove("Banana")

print(fruits)

# del statement
numbers = [1, 55, 64, 124, 654]

del numbers[0]
del numbers[1:2]

# clear()
fruits = ["Apple", "Orange", "banana"]
fruits.clear()
print(fruits)

# reverse()
numbers = [1, 55, 64, 124, 654]
numbers.reverse()
print(numbers)

# join()
names = ["Naresh", "Kurukuti", "Mine"]
print("".join(names))
print(" ".join(names))
print(", ".join(names))


# Finding list items
fruits = ["Apple", "Orange", "Banana"]

print(fruits.index("Orange"))
print(fruits.index("Mango"))

# To check item exist or not in the list
fruits = ["Apple", "Orange", "Banana"]

if "Mango" in fruits:
    print(fruits.index("Mango"))

# To get the count of items in the list
fruits = ["Apple", "Orange", "Banana"]

print(fruits.count("Mango"))
print(fruits.count("Orange"))

# Sorting List
numbers = [1, 34, 4, 5, 45, 2, 0, 545, 45, 64, 65]

numbers.sort()  # Ascending order
print(numbers)
numbers.sort(reverse=True)  # Descending order
print(numbers)

# sorted()
numbers = [1, 34, 4, 5, 45, 2, 0, 545, 45, 64, 65]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# sort() based on price

products = [
    ("Cup", 5),
    ("TShirt", 14),
    ("Hat", 100),
    ("Watch", 30),
    ("UV Lamp", 27)
]


def sort_products(product):
    return product[1]


products.sort(key=sort_products)
print(products)

###################### List Comprehension #######################
# basic syntax of an LC(List Comprehension)
# [expression for item in list]

numbers = [23, 54, 89, 15, 99]
fruits = ["Apple", "Orange", "Banana"]

numbers2 = [num for num in numbers]
print(numbers2)

numbers3 = [num*2 for num in numbers]
print(numbers3)

numbers4 = [(num/2)*5 for num in numbers]
print(numbers3)


products = [
    ("Cup", 5),
    ("TShirt", 14),
    ("Hat", 100),
    ("Watch", 30),
    ("UV Lamp", 27)
]
products_new = [item for item in products]
print(products_new)
product_items = [item[0] for item in products]
print(product_items)
product_prices = [item[1] for item in products]
print(product_prices)

# List Comprehension with single condition
products = [
    ("Cup", 5),
    ("TShirt", 14),
    ("Hat", 100),
    ("Watch", 30),
    ("UV Lamp", 27)
]

items = [item[1] for item in products if items[1] >= 20]
print(items)

# LC with two condition
products = [
    ("Cup", 5),
    ("TShirt", 14),
    ("Hat", 100),
    ("Watch", 30),
    ("UV Lamp", 27)
]

modified_numbers = [num if num > 100 else num/2 for num in numbers]
print(modified_numbers)


# Swapping List items
number = [2, 4, 6]

numbers[0], numbers[1], numbers[2] = numbers[2], numbers[1], numbers[0]
print(numbers)
