import time
import datetime
import text_test


stop = False
while stop == False:
    now = str(datetime.datetime.now().time())
    print(now)
    if now >= "08:55:00.000000":
        text_test.text()
        stop = True
