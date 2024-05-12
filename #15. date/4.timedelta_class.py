######################## Timedelta Class #######################

from datetime import timedelta, datetime, date

# Difference between two dates and times

t1 = datetime(year=2060, month=12, day=15, hour=5, minute=39, second=31)
t2 = datetime(year=1970, month=1, day=1, hour=5, minute=39, second=31)

t3 = t1 - t2
print(t3)

t1 = datetime(year=2060, month=12, day=15, hour=5, minute=39, second=31)
t2 = datetime(year=1970, month=1, day=1, hour=5, minute=39, second=31)

t3 = t1 - t2
print(type(t3))


# Difference between two timedelta objects

t4 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t5 = timedelta(days=5, hours=11, minutes=12, seconds=33)

t6 = t4-t5
print(t6)
print(type(t6))

# Getting negative timedelta object

t7 = timedelta(seconds=33)
t8 = timedelta(seconds=54)

t9 = t7 - t8
print(t9)

# Time duration in seconds

time = timedelta(days=20, hours=25, minutes=110, seconds=10000)
print("total seconds:", time.total_seconds())
