#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():

    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # print out the date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday is: ", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fir", "sat", "sun"]
    print("Today is", days[today.weekday()])

    # DATETIME OBJECTS
    # Get today's date from the datetime class
    now = datetime.now()
    print("Now is", now)

    # Get the current time
    current_time = now.time()
    print(current_time)


if __name__ == "__main__":
    main()
