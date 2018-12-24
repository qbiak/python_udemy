def add(n1, n2):
	try:
		print(n1 + n2)
	except TypeError:
		print('Whoops TypeError here!')


add(1, 'a')

for i in ['a', 'b', 'c']:
	try:
		print(i**2)
	except TypeError:
		print('Whoops, error in iteration!')

x = 5
y = 0
try:
	z = x/y
except ZeroDivisionError:
	print('Pls. Do not divide by zero.')
finally:
	print('Block finished here.')


def ask():
	try:
		n = int(input('Give me a number!'))
		return n**2
	except ValueError:
		print('You did not enter a value :(')


print(ask())
