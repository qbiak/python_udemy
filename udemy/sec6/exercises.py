def my_func(string):
	letters = list(string)
	result = []
	for i, l in enumerate(letters):
		if i % 2 == 0:
			result.append(l.lower())
		else:
			result.append(l.upper())
	return ''.join(result)


print(my_func('czesc'))


def square(num):
	return num**2


my_nums = range(1, 6)
print(list(map(square, my_nums)))
