#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print(now)

# print today's date one year from now
print(now + timedelta(days=365))

# create a timedelta that uses more than one argument
print(now + timedelta(days=2, weeks=3))

# calculate the date 1 week ago, formatted as a string
print(str(now - timedelta(weeks=1)))

# How many days until April Fools' Day?
today = date.today()
fools_date = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if fools_date < today:
    print("AFD wen by %d days ago" % (today - fools_date).days)
    fools_date = fools_date.replace(year=today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_fools = fools_date - today
print(time_to_fools.days, "days remains.")

