import requests

from datetime import datetime
import pytz

response = requests.get("http://google.com/")

print(response)


local = datetime.now()
print("local", local.strftime("%m/%d/%Y"))

tz_NYC = pytz.timezone("America/New_York")
datetime_NYC = datetime.now(tz_NYC)
print("tz_NYC", datetime_NYC.strftime("%m/%d/%Y, %H:%M:%S"))
