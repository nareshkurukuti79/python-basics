###################### Comparing objects using Magic methods ##################


# __gt__ magic method and __eq__ magic method and __lt__ magic method


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


test = Robot(4.015, 9.2345)
other_test = Robot(4.015, 9.2345)

print("output of __gt__ magic method")
print(test > other_test)

print("output of __eq__ magic method")
print(test == other_test)

print("output of __lt__ magic method")
print(test < other_test)

print(id(test))
print(id(other_test))
