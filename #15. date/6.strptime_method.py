################################ strptime() ########################

from datetime import datetime

# strptime()
date_str = "21 December, 2111"

date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)

# string to datetime object
date_str_two = "21 Aug, 2099"

date_obj = datetime.strptime(date_str_two, "%d %b, %Y")
print(date_obj)

# string to datetime object

date_str3 = "31/01/2200 19:10:10"
date_str4 = "12/31/2200 10:19:19"

# Corrected format strings
date_obj3 = datetime.strptime(date_str3, "%d/%m/%Y %H:%M:%S")
date_obj4 = datetime.strptime(date_str4, "%m/%d/%Y %H:%M:%S")
print(date_obj3)
print(date_obj4)
