####################### Method Overriding #######################

# method overriding

class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("singing")


class John(Person):
    # method overriding
    def __init__(self):
        self.jogger = True

    def run(self):
        print("Running")


runner = John()

print(runner.jogger)
# print(runner.employed)#it throws error because of method overriding


# fixing method overriding
class Person:
    def __init__(self):
        print("Base class")
        self.employed = True

    def sing(self):
        print("singing")


class John(Person):
    def __init__(self):
        super().__init__()

        print("sub class")

        self.jogger = True

    def run(self):
        print("Running")


runner = John()
print("output of fixing method overriding")
print(runner.jogger)
print(runner.employed)
