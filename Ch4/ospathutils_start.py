#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("Exists? " + str(path.exists("textfile.txt")))
    print("Is a file? " + str(path.isfile("textfile.txt")))
    print("Is a dir? " + str(path.isdir("textfile.txt")))

    # Work with file paths
    print(path.split(path.realpath("textfile.txt")))

    # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp((path.getmtime("textfile.txt"))))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print(td)
    print(td.total_seconds())

  
if __name__ == "__main__":
  main()
