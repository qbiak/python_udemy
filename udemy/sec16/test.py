# problem 1
x = 1024
binary = bin(x)
hexadecimal = hex(x)
print(binary)
print(hexadecimal)

# problem 2
y = 5.23222
print(round(y, 2))

# problem 3
s = 'hello how are you Marys, are you feeling okay?'
print(s.islower())

# problem 4
t = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(t.count('w'))

# problem 5
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
diff = set1.difference(set2)
print(diff)

# problem 6
either = set1.intersection(set2)
print(either)

# problem 7
sq = {x: x**3 for x in range(5)}
print(sq)

# problem 8
l1 = [1, 2, 3, 4]
l1.reverse()
print(l1)

# problem 9
l2 = [3, 4, 2, 5, 1]
l2.sort()
print(l2)
