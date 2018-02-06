## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal that has-a __init__ that takes the self and name parameters.
class Dog(Animal):

	def __init__(self, name):
		## From self get the name attribute and set it to name. Person has a name.
		self.name = name

class Mouse(Animal):
	def __init__(self, name):
		self.name = name
		
	def terry_say(self):
		for line in self.name:
			print line

mouse_terry = Mouse(["Hi, my name is Terry the mouse!"])

mouse_terry.terry_say()


## Make a class named Cat that is-a Animal. Class Cat has-a __init__ that takes self and name parameters. 
class Cat(Animal):

	def __init__(self,name):
		## From self get the name attribute and set it to name. Person has a name.
		self.name = name

	def meow_says(self):
		for line in self.name:
			print line
			
Cat_mando = Cat(["Catmando says Meow"])

Cat_mando.meow_says()


		
## Make a class named Person that is-a Object. Class Person has-a __init__ that takes self and name parameters.
class Person(object):

	def __init__(self, name):
	## From class get the name attribute and set it to name. Self has-a name.
		self.name = name
	
	## Person has-a pet of some kind. 
		self.pet = None

	def person_do(self):
		for line in self.name:
			print line

"""	
Can't do below because above is None
	def pet_do(self):
		for line in self.pet:
			print line
"""

Person_saydo = Person(["Man do see what say do"])

# Pet_saydo = Person(["Who's da pet?"])

Person_saydo.person_do()

# Pet_saydo.pet_do()

"""
## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
	## ?? hmm what is this strange magic? super is-a employee, self.
	super(Employee, self).__init__(name)
	## ?? self has a salary
	self.salary = salary
	
## ?? Fish is-a object
class Fish(object):
	pass
	
## ?? Salmon is-a Fish
class Salmon(Fish):
	pass
	
## ?? Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet and is satan.
mary.pet = satan

## frank is-a Employee.  
frank = Employee("Frank", 120000)

## frank has a pet and is-a rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()

"""

"""
Extra Questions
Why python added strange object class?
http://python-history.blogspot.jp/2009/02/adding-support-for-user-defined-classes.html

Possible to use Class like an object?
Everything in Python is an object, including classes
https://softwareengineering.stackexchange.com/questions/245929/using-class-like-an-object-in-python

Add functions in class:
class AnimalActor(Dog):
   def __init__(self, salary):
      self.__salary = salary

s = Salary(50000)
lassie = AnimalActor(s)
https://stackoverflow.com/questions/6976988/learn-python-the-hard-way-2nd-edition-exercise-45
"""