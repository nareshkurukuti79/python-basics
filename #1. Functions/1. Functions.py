def book():
    print("Thriller")


book()

sucess = True


def operation():
    if sucess:
        print("yay!!")


operation()

# ****** Arthametic Operations*****


def arithemtic_operatons(x, y):
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")


arithemtic_operatons(20, 5)


# ********************** Real Time Age**********
def legal_age(name, age, allowed_age):

    if age >= allowed_age:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")


legal_age("nares", 30, 18)


# ************** Function Types *****************
def facebook(name, status):
    return f"{name} is {status}"


user_status = facebook("Naresh", "active")
print(user_status)
print(id(user_status))

# *************** Keywords and Arguments***********


def multipy(number, by):
    return number * by


result = multipy(15, 4)
print(result)

result = multipy(number=65, by=15)
print(result)

# *********  Required & Optional Parameters


def working_conditon(device, status="working"):
    return f"The {device} is {status}"


print(working_conditon("Drill Press"))
print(working_conditon("Wleding Machine", "Out of Order"))

# ****** Non-keyword Arguments (*args) ****************
# we don't know how many arguments to pass
# we get tuples


def numebrs(*numbers):
    return numbers


print(numebrs(10, 21, 55, 24, 5435))

# ******** Keyword Arguments (**kwargs) *******
# we get dict


def employee(**info):
    print(info)


employee(name="Naresh", last_name="Kurukuti", age=34, skill_set="delveloper")


def to_do(**to_do_status):
    return to_do_status


to_do_status_result = to_do(
    get_coffer="Done", exercise="Pending", watch_tv="In Progress")

print(to_do_status_result)

# *********  Scope *********
# LocalVariable
# GlobalVariable


def comment(date):
    content = "amazing landscape"  # LocalVariable


comment("May 23, 2024")

# GlobalVairable
dob_name = "Hachi"


def animal_names():
    global dog_name
    dog_name = "Georgie"


animal_names()
print(dog_name)
