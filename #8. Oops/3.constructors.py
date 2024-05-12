########################## Constructors #####################


class Robot:
    def __init__(self, x, y):  # constructor
        self.x = 10
        print(f"Before assigning x value {self.x}")

        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}, {self.y})")


robot = Robot(2.4, 6.5)
robot.walk()
