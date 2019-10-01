from time import sleep
from datetime import datetime  # To receive live time to be as accurate as possible.
import text_test

I1 = input('Set Alarm Time: ')  # Makes it easy to set the alarm.
if len(I1) > 3:  # The time needs to be 4 numbers long with no semicolon e.g. 0730
    hour1 = I1[0:2]  # seperrates the hour from the minutes
    minute1 = I1[2:]  # seperrates the minutes from the hours
    print ('Alarm set for: %s:%s' % (hour1,minute1))  # confirms the set time

while True:  # constantly updates the current time and variables
    now = datetime.now()
    hournow = now.hour
    minnow = now.minute
    if int(hournow) == int (hour1) and int(minnow) == int(minute1):
        print ('ALARM!' ) # this is a substitute for a buzzer or a beeper
        text_test.text()
        break
    sleep (1)
