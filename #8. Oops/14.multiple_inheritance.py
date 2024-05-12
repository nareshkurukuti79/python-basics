#################  Multiple Inheritance ##########

# Multiple Inheritance with bad example
class Person:
    def sport_status(self):
        print("Runner")


class John:
    def sport_status(self):
        print("Jogger")


class Jane(John, Person):
    pass


print("output of multiple inheritance with bad way")
jane = Jane()
jane.sport_status()
john = John()
john.sport_status()


# Multiple Inheritance with good way

class Person:
    def runner(self):
        print("Runner")


class John:
    def jogger(self):
        print("Jogger")


class Jane(Person, John):
    pass


print("output of multiple inheritance with good way")
jane = Jane()
jane.runner()

john = John()
john.jogger()
