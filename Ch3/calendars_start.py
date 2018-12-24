#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2018, 10, 0, 0)
print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
hst = hc.formatmonth(2018, 10)
print(hst)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdates(2018, 10):
    print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1, 13):
    cal = calendar.monthcalendar(2018, m)
    week_one = cal[0]
    week_two = cal[1]
    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]
    print("%10s %2d" % (calendar.month_name[m], meet_day))  # first element is for text formatting
