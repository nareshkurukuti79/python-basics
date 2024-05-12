########################## Unpacking Operator ###################

# * => unpacking operator
numbers = [1, 2, 3]
print(numbers)

print(1, 2, 3)
print(*numbers)

# example2

values = list(range(15))
print(values)
print(*values)

values = [*range(20)]
print(*values)

# example3

print("output of example3")
print(*{*"python"})

# example4
citites = ["Rome", "Athens", "Istanbul", "Tokyo", "Jakarta"]
names = ["Olivia", "Amelia", "Oliver", "Charlotte", "Liam"]

info = [*citites, *names]
print(info)

# example5
dict_one = {
    "name": "Jasper",
    "city": "Tokyo"
}

dict_two = {
    "full name": "Dick van Dyke",
    "address": "USA"
}

dict_three = {
    "name": "William",
    "job": "Developer"
}
combined = {**dict_one, **dict_two, "Country": "France", **dict_three}
print("combined")
print(combined)
