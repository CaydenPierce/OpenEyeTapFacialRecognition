import datetime as dt
from time import sleep

t1 = dt.datetime.now()
sleep(2)
t2 = dt.datetime.now()

duration = (t2-t1).total_seconds()

if duration > 3:
    print("lol")
