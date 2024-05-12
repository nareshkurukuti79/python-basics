####################  Inheritance ################

# Method Inheritance

class Person:
    def sing(self):
        print("singing")


class John(Person):
    def jog(self):
        print("jogging")


class Jane(Person):
    def run(self):
        print("running")


runner = Jane()
runner.sing()

jogger = John()
jogger.sing()

# attributre inheritance


class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("singing")


class John(Person):
    def jog(self):
        print("jogging")


class Jane(Person):
    def run(self):
        print("running")


jogger = John()
print(jogger.employed)

runner = Jane()
runner.employed
print(runner.employed)
