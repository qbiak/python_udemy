class BankAccount:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f'Account owner: {self.owner}\nAccount balance: #{self.balance}'

	def deposit(self, amount=0):
		if type(amount) == int:
			if amount > 0:
				self.balance += amount
				print(f'Added ${amount}. Current balance: ${self.balance}')
			else:
				print('Amount must be an int bigger than 0.')
		else:
			print('Incorrect amount.')

	def withdraw(self, amount):
		if type(amount) == int:
			if amount <= self.balance:
				self.balance -= amount
				print(f'Paid ${amount}. Current balance: ${self.balance}')
			elif amount > self.balance:
				print('Not enough money.')
		else:
			print('Incorrect amount.')


acct1 = BankAccount('Krzysiek', 100)
print(acct1)
acct1.deposit(0)
acct1.deposit(50)
acct1.withdraw('a')
acct1.withdraw(220)
acct1.withdraw(20)
print(acct1.owner)
print(acct1.balance)
