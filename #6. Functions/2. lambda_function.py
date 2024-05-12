######################### Lambda / Lambda Function ######################
# Lambda functions are anonymous functions
# syntax:
# lambda arguments: expression
# Lambda functions are frequently used with built-in functions like map(), filter(), and reduce(). They allow you to define a simple function on the fly without the need for a separate named function

# Example1

products = [
    ("Product-1", 15),
    ("Product-2", 25),
    ("Product-3", 5),
    ("Product-4", 45),
    ("Product-5", 20),
    ("Product-6", 30),
]

products.sort(key=lambda product: product[1])
print(products)


# EXample2 lambda + filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: (x % 2 == 0), numbers)
print("\n output of lambda + filter()")
print(list(even_numbers))


# Example3 lambda + map()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(lambda x: x * 2, my_list))
print("\n output of lambda + map")
print(new_list)
