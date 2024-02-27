#Task 1:
from datetime import datetime,date, timedelta
print(datetime.now()+timedelta(days=-5))

#Task 2:
from datetime import datetime, date, timedelta

print(datetime.now() + timedelta(days=-1))
print(datetime.now())
print(datetime.now() + timedelta(days=+1))

#Task 3:
import datetime
from datetime import datetime,date,timedelta

def drop():
    print(datetime.now().replace(microsecond=0))

drop()

#Task 4:
from datetime import datetime

def date_difference_in_seconds(date1, date2):
    date1_obj = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    time_difference = date2_obj - date1_obj

    seconds_difference = time_difference.total_seconds()

    return seconds_difference

date_str1 = "2024-01-01 12:00:00"
date_str2 = "2024-02-25 18:30:45"

difference_seconds = date_difference_in_seconds(date_str1, date_str2)

print(f"The difference between the two dates is {difference_seconds} seconds.")
