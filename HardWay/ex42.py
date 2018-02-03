## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal that has-a __init__ that takes the self and name parameters.
class Dog(Animal):

	def __init__(self, name):
		## From self get the name attribute and set it to name. Person has a name.
		self.name = name
		
## Make a class named Cat that is-a Animal. Class Cat has-a __init__ that takes self and name parameters. 
class Cat(Animal):

	def __init__(self,name):
		## From self get the name attribute and set it to name. Person has a name.
		self.name = name
		
## Make a class named Person that is-a Object. Class Person has-a __init__ that takes self and name parameters.
class Person(object):

	def __init__(self, name):
	## From class get the name attribute and set it to name. Self has-a name.
	self.name = name
	
	## Person has-a pet of some kind. 
	self.pet = None
	
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