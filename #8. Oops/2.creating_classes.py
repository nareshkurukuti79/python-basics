##################### Creating Class #####################

# Example1

class Robot:
    def walk(self):
        print("The robot is walking")


robot = Robot()

robot.walk()

# using isinstance()

print("using instance")
print(isinstance(robot, Robot))

robot_obj = Robot()
print(isinstance(robot_obj, Robot))
