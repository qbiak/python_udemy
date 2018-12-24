my_string = 'hello'
my_list = my_string.split()
print(my_list)
print(list(my_string))

print('\ntest 1')
st = 'Print only the words that starts with s in this sentence'
words = st.split(' ')
s_words = []
for w in words:
	if w[0].lower() == 's':
		s_words.append(w)
print(s_words)

print('\ntest 2')
for n in range(0, 11):
	if n % 2 == 0:
		print(n)

evens = list(range(0, 11, 2))
print(evens)

print('\ntest 3')
div_3 = [n for n in range(1,50) if n % 3 == 0]
print(div_3)

print('\ntest 4')
st = 'Print every word in this sentence that has an even number of letters'
words = st.split(' ')
for w in words:
	if len(w) % 2 == 0:
		print(w)

print('\ntest 5')
for n in range(1, 101):
	if n % 3 == 0 and n % 5 == 0:
		print('FizzBuzz')
	elif n % 3 == 0:
		print('Fizz')
	elif n % 5 == 0:
		print('Buzz')
	else:
		print(n)

print('\ntest 6')
st = 'Create a list of the first letters of every word in this string'
words = st.split(' ')
letters = []
for w in words:
	letters.append(w[0])
print(letters)