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

# Override Explicitly

class Parent(object):
	
	def override(self):
		print "PARENT override"

class Child(Parent):

	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()
"""

class Parent(object):
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() #Use super to get parent altered version. Call super with arguments Child and self, then call the function altered on whatever it returns.
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()
son = Child()

dad.altered()
son.altered()