import random


def gen_squares(n):
    for i in range(n):
        yield i**2


for x in gen_squares(10):
    print(x)

print('END')


def rand_num(low, high, n):
    for _x in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

print('END')

s = 'hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

print('END')

my_list = list(range(1, 6))

gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
