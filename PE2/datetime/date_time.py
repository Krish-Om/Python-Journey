from datetime import date
import time

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1993, month=3, day=19)
print(d)
e = d.fromisoformat("1990-12-12")
print(e)


print(d.weekday())  # what day of week is it?
time.sleep(3)
print("Hello world")
