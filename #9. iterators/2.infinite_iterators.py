########################### Infinite Iterators #################

# infinite iterators using the next()
number = iter(int, 1)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


# infinite iterators using class

class OddNums:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


odd_nums = OddNums()

iterable_nums = iter(odd_nums)

print(next(iterable_nums))
print(next(iterable_nums))
