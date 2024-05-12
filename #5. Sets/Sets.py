####################### Sets #####################
# Sets are mutable
# Sets are unordered
# Sets are not allowed duplicate values


first_set = {11, 33, 44, 687, 989, 33}
print("output")

# Example2
mixed = {5.19, "Set", ("London", "Paris")}
print(mixed)

# Example3
numbers = {1, 2, 3, 4, 5, 6, 4, 5, 2, 1}
print(numbers)

# Example4 - creating a set from a tuple
colors = set(("blue", "green", "red", "green"))
print(colors)

# Example5 - creating a set from list
colors = set(["blue", "red", "green", "blue"])
print(colors)

# Example6 - creating a set from a dict
colors = set({
    "blue": 1,
    "red": 2,
    "green": 3
})
print(colors)

# Example7 - a set cannot have a mutuable data type as an item

# colors = {"red", "blue", [1, 2, 3]}  # TypeError

print(colors)

# Example8 - creating an empty set
names = {}
print(names)
print(type(names))

numbers = set()
print(numbers)
print(type(numbers))

######################## Modifying Sets ###########################
# Creating a Set
mixed_info = {"Python", "Dog"}
print(mixed_info)

# add()
mixed_info.add(31)
print(mixed_info)

# update()
mixed_info.update([12, "Jar", "Sand"])
print(mixed_info)

# update()
mixed_info.update(["Bird", "Island"], ("Cat", "Island"), {"Rabbit", "Island"})

print(mixed_info)

###################### Removing Set Itesms #########################
# discard()
numbers = {1, 2, 3, 4, 5, 6}

numbers.discard(4)
print(numbers)

# discard() -> item does not exist
numbers = {1, 2, 3, 4, 5, 6}
numbers.discard(11)

print(numbers)

# remove()
numbers = {1, 2, 3, 4, 5, 6}
# numbers.remove(11)  # KeyError

print(numbers)

# pop()
numbers = {1, 2, 3, 4, 5, 6}
numbers.pop()  # poping from start

print(numbers)

# clear()
numbers = {1, 2, 3, 4, 5, 6}
numbers.clear()

print(numbers)

################### Set Operations #############################
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union operator |
print(A | B)

# union() method
print(A.union(B))

# instersection operator &
print(A & B)

# instersection method
print(A.intersection(B))

# difference operator
print(A - B)

# difference method()
print(A.difference(B))

# set symmetric difference operator
print(A ^ B)

# set symmetric_difference()
print(A.symmetric_difference(B))


##################### More Set Methods #######################
# Example1
numbers = {101, 202, 303, 404, 505, 606}
other_numbers = numbers
print(numbers)
print(other_numbers)

numbers.remove(303)
print(numbers)
print(other_numbers)

numbers.discard(202)
print(numbers)
print(other_numbers)

# Example2
some_numbers = numbers.copy()
print(numbers)
print(some_numbers)


some_numbers.add(909)
print(numbers)
print(some_numbers)

print(id(numbers))
print(id(some_numbers))
print(id(other_numbers))

# isdisjoint() with sets
A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}
D = {10, 20, 30, 7}

print('Are A and B disjoint?', A.isdisjoint(B))  # True
print('Are A and C disjoint?', A.isdisjoint(C))  # False
print('Are B and C disjoint?', B.isdisjoint(C))  # False
print('Are A and D disjoint?', A.isdisjoint(D))  # True
print('Are B and D disjoint?', B.isdisjoint(D))  # False
print('Are C and D disjoint?', C.isdisjoint(D))  # True

# isdisjoint() with other iterables
A = {'a', 'b', 'c', 'd'}
B = ['b', 'e', 'f']
C = '5de4'
D = {1: 'a', 2: 'b'}
E = {'a': 1, 'b': 2}
F = ("Z", "g", "s")
print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))
print('Are A and D disjoint?', A.isdisjoint(D))
print('Are A and E disjoint?', A.isdisjoint(E))
print('Are A and F disjoint?', A.isdisjoint(F))

# issubset()
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B))
print(A.issubset(C))
print(B.issubset(A))
print(C.issubset(B))

# issuperset()
print(A.issuperset(B))
print(A.issuperset(C))
print(B.issuperset(A))
print(B.issuperset(C))

# Membership Test
numbers = {1, 2, 3, 4}
print(1 in numbers)
print(5 in numbers)

# iterating through a set
for num in numbers:
    print(num)
    print("number", num)

####################### Frozen Set ###########################
# Creating a fronzenset
# fronzenset is immutable

numbers = frozenset([1, 2, 3, 4, 5, 6])
some_num = frozenset([3, 4, 5, 6])
print(numbers)
print(type(numbers))

print(numbers.isdisjoint(some_num))
print(numbers.difference(some_num))

# frozenset()
vowels = ("a", "e", "i", "o", "u")
frozen_vowels = frozenset(vowels)
print(frozen_vowels)

print("Empty frozenset", frozenset())

####################### Set Comprehension ########################
numbers1 = {number ** 2 for number in range(10)}
print(numbers1)

numbers2 = {number ** 3 for number in range(5)}
print(numbers2)
