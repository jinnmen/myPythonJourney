#https://docs.python.org/2/tutorial/classes.html

"""
class Dog:
	
	def __init__(self, name):
		self.name = name
		self.tricks = [] # creates a new empty list for each Dog
	
	def add_trick(self, trick):
		self.tricks.append(trick)
		
d = Dog('Fido')
e = Dog('Buddy')
f = Dog.tricks
d.add_trick('roll over')
e.add_trick('play dead')

print d.tricks
print e.tricks
"""

class Cat:
	
	tricks = []
	
	def __init__(self,name):
		self.name = name
	
	def add_trick(self, trick):
		self.tricks.append(trick)

a = Cat('Mimo')
b = Cat('Lilo')
a.add_trick('jump')
b.add_trick('shoot')
print b.tricks
