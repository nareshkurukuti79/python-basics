################################## Instance Attributes VS Class Attributes ######################
# 1 - Instance Attr ->>> within the constructor
# 2 - Class Attr ->>> within the class itself


# Instance Attr

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"Walking CoOrdinates {self.x, self.y}")


# 1st instantiation

test_walk1 = Robot(8.9, 99.7)
test_walk1.walk()
print(test_walk1)

# 2nd instantiations

test_walk2 = Robot(4.5, 6.7)
test_walk2.walk()
print(test_walk2)

# different Instance attr

test_walk1.z = 2.3
print(test_walk1.z)


# class attr


class Robot:
    # class attr
    coordinate_z = 45.8

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


# 1st instantiation
test_walk1 = Robot(8.9, 99.7)
print(test_walk1.coordinate_z)


# 2st instantiation
test_walk2 = Robot(8.9, 99.7)
print(test_walk2.coordinate_z)
