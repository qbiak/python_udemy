import math


def find_pi_up_to(precision, n):
    pi = 4/1
    for x in range(3, precision, 4):
        pi -= (4/x)
        pi += (4/(x+2))
    return round(pi, n+1)


print(find_pi_up_to(100000, 3))
print(format(math.pi, '.50g'))
