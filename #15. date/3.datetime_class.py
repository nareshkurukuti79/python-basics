######################## DateTime Class ##########################

from datetime import datetime

# Python datetime object
time_1 = datetime(2100, 1, 1)
print(time_1)

time_2 = datetime(2040, 10, 24, 20, 50, 50)
print(time_2)

# Getting year, month , hour, minute and timestamp

time_3 = datetime(2050, 10, 25, 20, 50, 50)


print("Year :", time_3.year)
print("Month :", time_3.month)
print("Hour :", time_3.hour)
print("Minute :", time_3.minute)
print("Second :", time_3.second)
print("Timestamp :", time_3.timestamp())
