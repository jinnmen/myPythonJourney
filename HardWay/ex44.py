# Implicit Inheritence
"""
class Parent(object):

	def implicit(self):
		print "PARENT implicit()"
		
class Child(Parent):
	pass
	
dad = Parent()
son = Child()

dad.implicit()
son.implicit()
"""


# Override Explicitly

class Parent(object):
	
	def override(self):
		print "PARENT override"

