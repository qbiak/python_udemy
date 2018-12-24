#
# Example file for working with functions
#

# define a basic function


def func1():
    print("Hello from func1")

# function that takes arguments


def take_args(arg1, arg2):
    print("here is a " + arg1 + " and a " + arg2)

# function that returns a value


def cube(x):
    print(x*x*x)

# function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments


def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result


func1()
take_args("user", "password")
cube(7)
print(power(4))
print(power(4, 2))
print(multi_add(1))
print(multi_add(2, 2, 6, 7))
