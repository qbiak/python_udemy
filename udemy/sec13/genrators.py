def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result


def create_cubes_yield(n):
    for x in range(n):
        yield x**3


print(create_cubes(10))
print(create_cubes_yield(10))


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for n in gen_fibon(10):
    print(n)


def simple_gen(n):
    for x in range(n):
        yield x


for num in simple_gen(10):
    print(num)

try:
    print('Starting generator and prints.')
    g = simple_gen(3)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration:
    print('More prints than generated items.')
finally:
    print('Generator and prints executed.')

s = 'hello'
for l in s:
    print(l)

s_iter = iter(s)
print('\n' + next(s_iter))
print(next(s_iter))
print(next(s_iter))
