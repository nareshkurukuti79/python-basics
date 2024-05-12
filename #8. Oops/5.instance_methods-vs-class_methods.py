################################ Instance Methods VS class Methods ###########################


# instance methods

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x},{self.y})")


test_walk = Robot(1.1, 4.6)
print("output from the instance methods")
test_walk.walk()


# class methods

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # decorator

    @classmethod
    def specific_coordinate(cls):
        return cls(1.1, 4.6)

    def walk(self):
        print(f"\nwalking coordinates ({self.x},{self.y})")


test_walkn = Robot.specific_coordinate()
print("output for the class methods")
print(test_walkn.walk())
