#https://docs.python.org/2/tutorial/classes.html

class Dog:

	kind = 'canine'
	
	def __init__(self, name):
		self.name = name
		
d = Dog('Fido')
e = Dog('Buddy')

print d.kind
print e.kind
print e.name
