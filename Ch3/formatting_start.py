#
# Example file for formatting time and date output
#

from datetime import datetime


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()
    print(now.strftime("The current year is: %Y"))

    # Date Formatting

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("Today is year %Y, %A weekday, month %B so it is %D"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Here is %c"))

    # Time Formatting

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time is: %H %M %S"))
    print(now.strftime("Current time is: %I %M %S %p"))


if __name__ == "__main__":
    main()
