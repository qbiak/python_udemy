from math import pi
import string

def lesser_of_two_evens(a,b):
	if a % 2 == 0 and b % 2 == 0:
		return min(a, b)
	else:
		return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))


def animal_crakcers(string):
	words = string.lower().split(' ')
	if words[0][0] == words[1][0]:
		return True
	else:
		return False


print(animal_crakcers('Leveled Lama'))
print(animal_crakcers('Leveled Pama'))


def makes_twenty(a,b):
	if a == 20 or b == 20 or a + b == 20:
		return True
	else:
		return False


def other_side_of_seven(num):
	result = 7
	if num < 7:
		result += (7 - num) * 2
	elif num > 7:
		result -= (num - 7) * 2
	return result


print(other_side_of_seven(4))
print(other_side_of_seven(12))


def old_macdonald(string):
	letters = list(string.lower())
	for i in [0, 3]:
		letters[i] = letters[i].upper()
	print(''.join(letters))


old_macdonald('tester')


def master_yoda(sentence):
	words = sentence.split(' ')
	words.reverse()
	return ' '.join(words)


print(master_yoda('you are my best friend'))


def almost_there(n):
	if 90 <= n <= 110 or 190 <= n <= 210:
		return True
	else:
		return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


def laughter(pattern, text):
	pass


def has_33(arr):
	for i in range(0, len(arr) - 1):
		if arr[i] == 3 and arr[i + 1] == 3:
			return True
	return False


def paper_doll(string):
	result = []
	for l in string:
		result += 3 * l
	return ''.join(result)


print(paper_doll('Hello'))


def blackjack(a, b, c):
	my_sum = a + b + c
	if my_sum < 21:
		return my_sum
	elif my_sum >= 31 and 11 in [a, b, c]:
		return my_sum - 10
	else:
		return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def summer_69(arr):
	total = 0
	add = True
	for n in arr:
		while add:
			if n != 6:
				total += n
				break
			else:
				add = False
		while not add:
			if n != 9:
				break
			else:
				add = True
				break
	return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


def spy_game(nums):
	code = [0, 0, 7, 'x']
	for i in nums:
		if i == code[0]:
			code.pop(0)
	return len(code) == 1


print(spy_game([1, 2, 4, 0, 4, 0, 7, 5]))


def count_primes(num):
	if num < 2: # check 0 and 1 in input
		return 0
	primes = [2]
	x = 3
	while x <= num:
		for y in range(3, x, 2):
			if x % y == 0:
				x += 2
				break
		else:
			primes.append(x)
			x += 2
	print(primes)
	return len(primes)


def print_big(letter):
	patterns = {
		1: '  *  ',
		2: ' * * ',
		3: '*   *',
		4: '*****',
		5: '**** ',
		6: '   * ',
		7: ' *   ',
		8: '*   *',
		9: '*    '
	}
	alphabet = {
		'A': [1, 2, 4, 3, 3],
		'B': [5, 3, 5, 3, 5],
		'C': [4, 9, 9, 9, 4],
		'D': [5, 3, 3, 3, 5],
		'E': [4, 9, 4, 9, 4],
	}
	for pattern in alphabet[letter.upper()]:
		print(patterns[pattern])


print_big('b')


def vol(rad):
	return (4/3) * pi * (rad ** 3)


print(vol(2.5))


def ran_check(num, low, high):
	return num in range(low, high)


print(ran_check(3, 2, 5))
print(ran_check(1, 2, 5))


def up_low(string):
	upper = 0
	lower = 0
	for i in string:
		print(i)
		if i.isupper():
			upper += 1
		elif i.islower():
			lower += 1
		else:
			continue
	print(f'Upper cases {upper}. Lower cases {lower}.')


up_low('Czesc Przyjacielyu.')


def unique_list(arr):
	unique = []
	for i in arr:
		if i not in unique:
			unique.append(i)
	return unique


print(unique_list([1, 1, 2, 2, 5, 5, 1, 1, 4, 1, 2, 5, 41, 6, 3, 1, 42, 3, 64, 1]))


def multiply(numbers):
	result = numbers[0]
	for i in numbers:
		result *= i
	return result


print(multiply([1, 2, 3]))
print(multiply([1, 0, 3]))


def palindrome(string):
	# s == s[::-1]
	result = False
	for i, let in enumerate(string):
		if let == string[-(i+1)]:
			result = True
		else:
			result = False
			break
	return result


print(palindrome('kajak'))
print(palindrome('kajaki'))


def is_panagram(str):
	alphabet = string.ascii_lowercase
	alphaset = set(alphabet)
	return alphaset <= set(str.lower()) # check it in section 53

