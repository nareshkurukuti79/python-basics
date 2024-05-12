################################ Iterators #########################

# Example1 __iter()__ & __next()__

numbers = [1, 2, 3, 4, 5]

first_iterator = iter(numbers)

print(next(first_iterator))
print(next(first_iterator))

# next() == __next__()
print(first_iterator.__next__())
print(first_iterator.__next__())
print(type(first_iterator.__next__()))

# Example2
numbers = [1, 2, 3, 4, 5]

iterable_obj = iter(numbers)

while True:
    try:
        element = next(iterable_obj)

        print(f"ELement: {element}")

    except StopIteration:
        break


# Example3 buiding a custom iterator

class NumberPower:
    def __init__(self, maxi_num):
        self.maxi_num = maxi_num

    # creating the iterator object
    def __iter__(self):
        self.n = 0
        return self

    # iterate over the created iterator object and generate one value each time
    def __next__(self):
        if self.n <= self.maxi_num:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopAsyncIteration


# creating an instance/object of the class NumberPower
num_pow = NumberPower(2)
# print(num_pow)

# creating an iterable from the object

iterable_obj = iter(num_pow)

# using the next() to go the next iterator element

print(next(iterable_obj))
print(next(iterable_obj))
print(next(iterable_obj))
