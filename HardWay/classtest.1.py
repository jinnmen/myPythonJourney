
# Not necessary to have this. But if need Animal to be variable in Dog, then need this.
# Animal is-a object . Something needs to be master object
class Animal(object):
	pass

# Make a class named Dog that is-a Animal. Class Dog has-a __init__ that takes self, name and age parameters.
class Dog(Animal):

	# All dogs here are of mutt kind
	kind = 'mutt'

	# From self get the name and age attribute and set them to name and age. Animal Dog has name and age.
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print name, age
		
a = Dog('Frank', "11")
b = Dog("Danny", '12')
Dog("Batty", '10')

# print a's kind only
print a.kind
# print a's name only
print a.name
# print b's age only
print b.age

# Must attach instance to variable for printing else get error