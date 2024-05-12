import time

print("Immediately")
time.sleep(4.0)
print("Imediately after 4 seconds")

# creating a simple low level digital clock
while True:
    local_time = time.localtime()
    result = time.strftime("%I:%M:%S", local_time)
    print(result)
    time.sleep(1)
