###################### Magic Methods ##################

# __str__ magic method
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"walking coordinates ({self.x}{self.y})")

    def __str__(self):
        return f"I am a magic method a coordinates ({self.x},{self.y})"


test = Robot(0.1, 0.5)
print(test)

print(str(test))
