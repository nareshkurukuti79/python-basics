############################# Getting the current Date & Time #####################


# To print the current date&time
# from datetime import datetime
# print(datetime.now())

# Getting the current date

# import datetime
# print(datetime.date.today())

# Getting the Datetime attributes
# print(dir(datetime))

# Creating a date object

# date = datetime.date(2100, 12, 31)
# print(date)

#  importing the date class

# from datetime import date

# print(date(2100, 12, 30))


# getting date from a timestamp
# from datetime import date

# time_stamp = date.fromtimestamp(409899999)
# print(time_stamp)

# getting today's year, month and day
from datetime import date

today = date.today()
print("Current Year:", today.year)
print("Current Month:", today.month)
print("Current Day:", today.day)
