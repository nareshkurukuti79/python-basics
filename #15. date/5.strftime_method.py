##################### strtime() method ############################


# Date Formats
# US ->>>> mm/dd/yyyy
# UK ->>>> dd/mm/yyyy

from datetime import datetime

# current date & time
now = datetime.now()

time = now.strftime("%H:%M:%S")

print(time)

s1 = now.strftime("%m/%d/%Y")
print(s1)

s2 = now.strftime("%m/%d/%Y, %H:%M:%S")
print(s2)

# datetime to string using strtime()
now = datetime.now()

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

print("year "+year)
print("monht"+month)
print("day"+day)

# creating string from a timestamp

timestamp = 4333259999
date_time = datetime.fromtimestamp(timestamp)

print(date_time)

print(type(date_time))

date = date_time.strftime("%m/%d/%Y, %H:%M:%S")

print(date)
print(type(date))

date2 = date_time.strftime("%d %b, %Y")
print("date2 "+date2)

# to get PM or AM

date3 = date_time.strftime("%I%p")
print("date3 "+date3)

# locale's appropriate date and time
timestamp = 4599998989
date_time = datetime.fromtimestamp(timestamp)

d1 = date_time.strftime("%c")
print('d1 '+d1)

d2 = date_time.strftime("%x")
print(d2)

# to get hh:mm:ss
d3 = date_time.strftime("%X")
print('d3 '+d3)

# python datetime to timestamp

now = datetime.now()

# converting to timestamp
time_stamp = datetime.timestamp(now)
print("converting to timestamp", time_stamp)

# converting from timestamp
time_stamp = datetime.fromtimestamp(time_stamp)
print("converting from timestamp", time_stamp)
