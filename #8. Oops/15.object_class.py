######################### The Object Class ###################


class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("singing")


class John(Person):
    def running(self):
        print("Running")


runner = John()
print(isinstance(runner, John))
print(isinstance(runner, Person))

print(isinstance(Person, object))

base_object = object()
# to findout if a class inherits from another class

print(issubclass(John, Person))
print(issubclass(John, object))
