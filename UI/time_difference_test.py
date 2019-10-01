import datetime
from datetime import timedelta

#now = datetime.datetime.now()
#time1 = datetime.timedelta(hours =9 , minutes = 0)
#time2 = datetime.timedelta(hours = 12, minutes = 0)

#if now > time1 and now < time2:
#    print("After 9.")
#elif now >time2 and now <time1:
#    print("after 12")

now = datetime.datetime.now()
today8am = now.replace(days = days +1 , hour = 8, minute = 0, second = 0)
if now > today8am:
    print("Time is ", now)
    print("Replacement ", today8am)
    print("After 8am")
elif now < today8am:
    print("Time is " ,now)
    print("Before 8am")
    
