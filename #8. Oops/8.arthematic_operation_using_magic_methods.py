############################## Arthematic operation using magic methods #######################

# __add_ magic method
# __sub__ magic method
# __mul__ magic method
# __floor_div__ magic method

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"Coordinates ({self.x + other.x}, {self.y + other.y})"

    def __sub__(self, other):
        return f"Coordinates ({self.x - other.x}, {self.y - other.y})"

    def __mul__(self, other):
        return f"Coordinates ({self.x * other.x}, {self.y * other.y})"

    def __floordiv__(self, other):
        return f"Coordinates ({self.x // other.x}, {self.y // other.y})"


test = Robot(12, 1)
other_test = Robot(4.12, 8.45)

print(test.x)
print(test.y)
print(other_test.x)
print(other_test.y)
print("output of __add__ magic method")
print(test + other_test)
print("output of __sub__ magic method")
print(test - other_test)
print("output of __mul__ magic method")
print(test * other_test)
print("output of __floordiv__ magic method")
print(test // other_test)
