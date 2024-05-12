######################### Generators ######################

# __iter__() & __next__() & iter() are implemented automatically


"""
Normal Fun
1 - return
2 - after the return, the variables are garable collected
3 - return terminates a func
4 - performs a task or caculates a value

Generator Function
1 - yied
2 - access to varaibales after func execution
3 - yied does not terimate a func
4 - return terminates a func

"""

# Creating a generator


def first_generator():
    x = 1
    print("1st iteration")

    yield x
    x = 2
    print("2nd iteration")

    yield x
    x = 3
    print("3rd iteration")

    yield x
    x = 4
    print("4th iteration")


my_gen = first_generator()
# print(my_gen)
# print(type(my_gen))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
