"""
1. Make a different game from the one I made.

2. Use more than one file, and use import to use them. Make sure you know what that is.

3. Use one class per room and give the classes names that fit their purpose. Like GoldRoom, KoiPondRoom.

4. Your runner will need to know about these rooms, so make a class that runs them and knows about them. There's
plenty of ways to do this, but consider having each room return what room is next or setting a variable of what
room is next.

5. Add comments!


Game concept and idea:
Have 3 dogs, 3 rooms
Need to teach them 1 skill each that matches room requirements to clear
The skills needs to be fetched from other files.
A tale of 3 dogs: Dido, Fido, Kido
tricks: roll, jump, sit
rooms : R, J, S
get a bone for each room's trick cleared. 
After getting 3 bones, you win as best dog trainer of 2018.

For story starting scene, read from file (ex.15)

*Dog
-Fido
-Dido
-Kido

*Skills
-roll
-jump
-sit

*Map
-opening scene
-next scene

*Scenes
-enter
*death
*room r
*room j
*room s
*hall #this is main area you are in, always return here to train dogs

#To start game:
*Wishbone
-star


"""

from sys import argv 
from sys import exit

#To run this correctly, type python this file name + "/Users/Mac/Documents/jimmy personal/python/ex45op.txt"
script, filename = argv

txt = open(filename)

print "Contents of file opened %r: " % filename
print txt.read()

class Scene(object):

	def enter(self):
		print "This scene is under construction"
		exit (1)
		
class wishbone(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def star(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n-------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
# https://stackoverflow.com/questions/34379653/lpthw-ex-43-queries-on-use-of-self			

class Death(object):

	dendings = [
		"Your mama told you not to game",
		"Your papa told you not to game",
		"Your dog told you to sit"
	]
	
	def enter(self):
		print Death.dendings[randint(0, len(self.dendings)-1]
		exit(1)

class hall(object):
	
	return 'dog'

"""	
	dog = []
	
	def enter(self):
		
		print "Here you train your dogs"
		print "Which dog?"
		
		action = raw_input("> ")

		if action == "Fido":
			print "Here comes Fido!"
			dog.append(action)
		elif action == "Dido":
			print "Here comes Dido!"
			dog.append(action)
		elif action == "Kido":
			print "Here comes Kido!"
			dog.append(action) 
		else: 
			print "Pick a valid dog name"
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


class roomr(object):

	def enter(self):
		script, filenamer = argv
		
		txt = open(filenamer)
		
		print "Contents of file opened %r: " % filenamer
		print txt.read()
	
		action = raw_input("> ")
		
		if action == "roll":
			print "Yes! You rolled! Good dog!"
			return 'hall'
					

	

