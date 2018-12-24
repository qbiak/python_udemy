import datetime
import timeit

t = datetime.time(5, 25, 1)
print(t)

perf = timeit.timeit('-'.join(map(str, range(100))), number=1000)
print(perf)
