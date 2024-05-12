##### Dictionaries ##########
contacts = {
    "samantha": 830,
    "JoHn": "123"
}

print("ex-1 output")
print(contacts)

# Ex-2
employee_info = {
    "Name": "Will",
    "Lastname": "Oldman",
    "Address": "NYC",
    "Age": 38
}

print("ex-2 output")
print(employee_info)

# create dictionaries using dict()

animal_names = dict(cat="Sebastin", dog="Togo")
print("output dict()")
print(animal_names)


# Ex - 5 accessing dict keys
print(animal_names["cat"])
print(animal_names["dog"])
animal_names["new"] = "animals"

print(animal_names)

# Checking whether a key exists or not

if "Favorite Color" in animal_names:
    print("Favorite Color")

# get() method

employee_info = {
    "Name": "Will",
    "Lastname": "Oldman",
    "Address": "NYC",
    "Age": 38
}

print("output of get()")
print(employee_info.get("Age"))
print(employee_info.get("contact"))  # it will return None


################## Dictonaries Method Part 1 #######################

employee_info = {
    "Name": "Will",
    "Last Name": "Oldman",
    "Address": "New York",
    "Job": {"Salesperson", "Developer"},
    "Age": 34,
    "Hobbies": ("Reading", "Watching", "Walking"),
    1994: "Date of Birth",
    "Married": True,
    "Favorite Songs": ["Un Dia", "Blinding Lights", "Shallow"],
    "Best Friend": {"name": "Gerald"},
    "Special One": None
}

# Clear()
# employee_info.clear()
# print("\n output of clear():")
# print(employee_info)

# copy()
gerald_info = employee_info.copy()
print("\n output of copy()")
print(gerald_info)

# fromkeys()
print("\n output of fromkeys():")
letters = {'a', 'e', 'i', 'o', 'u'}
numbers = [1, 2]

vowels = dict.fromkeys(letters)
print(vowels)

vowels = dict.fromkeys(letters, numbers)
print(vowels)

print({}.fromkeys(employee_info))

########################### Dictonaries Methods Part2 ##################################
# items() - it will return the key & values pairs of tuples

print("output of items()")
print(employee_info.items())

# del
del employee_info['Best Friend']
print("\n output of del")
print(employee_info)

# keys()
print("\n output of keys()")
print(employee_info.keys())


########################### Dictionaries Methods Part3 ########################

# values()
print("\n output of values():")
print(employee_info.values())

# popitem()
print("\n output of popitem()")
print(employee_info.popitem())

# setdeafult()
print("\n output of setdefault():")
print(employee_info.setdefault("Smoking"))

print(employee_info.setdefault("Allergies", "N\A"))

############################ Dictionaries Method Part4 #######################

# pop() - case #1
target_item1 = employee_info.pop("Age")
print("\n output of pop():")
print(target_item1)
print(employee_info)

# pop() - case #2
target_item2 = employee_info.pop("Smoking", "No")
print("\n output of pop():")
print(target_item2)
print(employee_info)

# pop() - case #3

target_item3 = employee_info.pop("Allergies")
print("\n output of pop():")
print(target_item3)
print(employee_info)

# update() - case #1
lost_key = {"Favorite Movie": "The Blood Diamond"}
print("\n output of update():")
employee_info.update(lost_key)
print(employee_info)


# update() - case #2

found_key = {"Favorite Movie": "Titanic"}
print("\n ouptut of update() case #2")
employee_info.update(found_key)
print(employee_info)

# update() - case #3 ->>>> when a tuple is passed

print("\n output of update when tuple is passed")
employee_info.update(Dog_name="Krypto", Bird_name="Precious")
print(employee_info)


######################## Dictionary Comprehension #####################
# Dictionary comprehension
# new_dict = {key_expr: value_expr for item in iterable if condition}
# key_expr: The expression for the dictionary keys.
# value_expr: The expression for the corresponding values.
# iterable: The source of elements (e.g., a list, tuple, or range).
# condition (optional): An optional condition that filters which key-value pairs are included in the new dictionary.

# EX - 1
coordinates = {x: (((x * 5)/2)+12) - (2.4/1.2) * 6 for x in range(5)}
print("\n output of dictionary comprehension")
print(coordinates)


# EX -2
old_price = {"milk": 1.02, "coffee": 2.5, "bread": 1.89}

dollar_to_pount = 0.76
new_price = {item: value *
             dollar_to_pount for (item, value) in old_price.items()}

print(new_price)


# Ex - 3 singl if condition DC
original_dict = {"Jack": 38, "Lincoln": 48, "Theodore": 57, "Johon": 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

# EX - 4 multiple if condions DC
original_dict = {"Jack": 38, "Lincoln": 48, "Theodore": 57, "Johon": 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0 if v > 20}
print(new_dict)

# EX - 5 DC with if else condition
original_dict = {"Jack": 38, "Lincoln": 48, "Theodore": 57, "Johon": 33}

new_dict = {k: "old" if v > 40 else "young" for (
    k, v) in original_dict.items()}
print(new_dict)


# Nested DC with two DC's
new_dict = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}

print(new_dict)

# Nested DC with two DC's in the loop form
new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {k2: k1*k2 for k2 in range(1, 6)}

print(new_dict)

# Nested DC with two DC's in the loop form, completely unfolded
new_dict = {}
for k1 in range(2, 5):
    new_dict[k1] = {}
    for k2 in range(1, 6):
        new_dict[k1][k2] = k1*k2


print(new_dict)

# Iterating Over Dictionaries
random_dict = {
    34: "kjek",
    5: "jkj",
    45: "Hey",
    "is_employed": False

}

print("output")
for key in random_dict:
    print(f"keys => {key} <br> value=> {random_dict[key]}")
