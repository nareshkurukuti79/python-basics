##################### Classes #######################

"""
Object
1 - attributes
2 - behaviour
"""
# Class
"""
A class is a blueprint for creating objects
"""


class Robot:
    pass


# Object

"""
An object(instance) is an instantiation of class.
"""
robot_obj = Robot()
print(robot_obj)
print(type(robot_obj))

# class of str for creating strings
name = "Naresh"
print(type(name))

# class of int for creating integers
x = 25
print(type(x))

# class of float for creating float
z = True
print(type(z))

# class of list for creating lists
my_list = [1, 2, 3]
print(type(my_list))

# class of dict for creating dicts
my_info = {
    "name": "Musilm",
    "last name": "Helalee"
}
print(my_info)

# class of tuple for creating tuples
my_tuple = (1, 2, 3)
print(type(my_tuple))

# class of set for creating sets
my_set = {1, 2, 3}
print(type(my_set))
