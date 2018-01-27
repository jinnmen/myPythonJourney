# https://www.daniweb.com/programming/software-development/threads/59117/why-use-a-python-class
# a typical Python class example
# newer class convention uses inheritance place holder (object)

class Account(object):
	# __init__() initializes a newly created class instance,
	# 'self' refers to the particular class instance
	# and also carries the data between the methods.
	# You have to supply the initial account balance
	# during creation of the class instance.
	def __init__(self, initial):
		self.balance = initial
		
	def deposit(self, amt):
		# a function within a class is called a method
		# self always starts the argument list of a method
		self.balance = self.balance + amt
		
	def withdraw(self, amt):
		self.balance = self.balance -amt
	
	def getbalance(self):
		return self.balance
		
# create two new class instance, Mary's and Tom's account
mary = Account(1000.00) # start with initial balance of 1000.00 . How to get users to key in value?
tom = Account(3000.00) # tom is lucky he starts with 3000.00

# Mary makes deposits and withdrawals
mary.deposit(500.00)
mary.deposit(23.45)
mary.withdraw(78.20)

# Tom also accesses his account
tom.withdraw(1295.50)

# now look at the account balances
print "Mary's balance = $%0.2f" % mary.getbalance() #1445.25
print "Tom's balance = $%0.2f" % tom.getbalance() #1704.50