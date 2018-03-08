"""
Write out nouns/ draw problem. 
A lil' paragraph for the game:
Aliens have invaded a space ship and our hero has to go through a maze of rooms 
defeating them so he can escape into an escape pod to the planet below. 
The game will be more like a Zrok or Adventure type game with text outputs and funny 
ways to die.
The game wil involve an engine that runs a map full of rooms or scenes. Each room will 
print its own description when the
player enters it and then tell the engine what room to run next out of the map.

Describe each scene:
Death: When player dies and should be something funny.
Central Corridor: Starting point and has Gothon already standing there they have to 
defeat with a joke before continuing
Laser Weapon Armory: When hero gets neutron bomb to blow up ship before getting 
escape pod. Keypad and has to guess number.
The Bridge: Another battle sene with Gothon where hero places bomb.
Escape Pod: Hero escapes but only guessin right pod.

Make a list of all nouns:
Alien
Player
Ship
Maze
Room
Scene
Gothon
Escape od
Planet
Map
Engine
Death
Central Corridor
Laser Weapon Armory
The Bridge

Could possibly go through all verbs to see if any good function names but skip for now.

Make class hierarchy
* Map
* Engine
* Scene
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
	
Go through and figure out what actions needed based on verbs. "run" engine, 
"Get next scene" from map, "opening scene", "enter" scene:
*Map
	- next_scene
	- opening_scene
* Engine
	- play
* Scene
	- enter
	* Death
	* Central Corridor
	* Laser Weapon Armory
	* The Bridge
	* Escape Pod
-enter under Scene: All scenes under it will inherit it and override it.	
Now we code, small example:
"""
from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

# from skeleton code, have a base class for Scene. Common things all scenes do. In here, 
# not do as much, more of demo.
# Demo of what you would do to make a base class.

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
#Have Engine class, can see how using methods for Map.opening_scene and Map.next_scene.
				
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such as luser.",
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
	
# First scene is the odd scene named Death which shows simplest kind of scene can write

class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
		
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fbsng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughing ou run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
# After creating CentralCorridor, start of game, do scenes for game before Map because 
# need reference later.
			
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (1, 2, 3)   # (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input ("[keypad]> " )
		guesses = 0
		
		while guess != code and guesses <10:
			print "BZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print "You grav the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'
		
class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."
		
		action = raw_input ("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the grou of Gothons"
			print "and make a leap for the door. Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probrably blow up when"
			print "it goes off."
			return 'death'
			
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		
		else:
			print "DOES NOT COMPUTE!"
			return "the_bridge"
						
class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes. It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference. You get to the chamber with the escape pods, and"
		print "now need to pick one to take. Some of them could be damaged"
		print "but you don't have time to look. There's 5 pods, which one"
		print "do you take?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			print 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out onto space heading to"
			print "the planet below. As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time. You won!"
			
			return 'finished'

# This is the rest of the game's scenes, since I know I need them and have thought
# about how they'll flow together I'm able to code them directly.
# Not type in everything, build incrementally, one bit at a time.
					
class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

# After Map class, can see storing each scene by name in a dictionary, then refer to
# that dict with Map.scenes. Also why map comes after scenes because dict has to refer
# to them so need to exist.

# a_map is an instance of Map and gets 'central_corridor' stored in self.start_scene, refer __init__ of Map
a_map = Map('central_corridor')
# a_game = Engine(a_map) makes an instance of Engine handing in this instance a_map.
# It is stored in self.scene_map , refer to __init__() of Engine.
a_game = Engine(a_map)
# calling play finally comes to this line: current_scene = self.scene_map.next_scene(next_scene_name)
# this means current_scene = CentralCorridor()
a_game.play()



# more on classes and explanation of __int__ :
# https://stackoverflow.com/questions/8609153/why-do-we-use-init-in-python-classes
# https://stackoverflow.com/questions/34379653/lpthw-ex-43-queries-on-use-of-self


"""
Question
For this line,

current_scene = self.scene_map.next_scene(next_scene_name)
I believe this gets from value of CentralCorridor() using the central_corridor key from the dictionary. So it would look something like this:

current_scene = self.scene_map.CentralCorridor()
What exactly does the self.scene_map do?


Answer
I think the best way, after your read through the implementation of the classes, is to start at the end where the execution begins:

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
So a_map is an instance of Map and gets 'central_corridor' stored in self.start_scene (see __init__() of Map). 
Next, a_game = Engine(a_map) makes an instance of Engine handing in this instance a_map. 
It is stored in self.scene_map (see __init__() of Engine). Calling play() on this instance finally comes to this line:

current_scene = self.scene_map.next_scene(next_scene_name)
It means:

current_scene = CentralCorridor()
because it retrieves an instance of CentralCorridor from the dictionary scenes in Map, using the key 'central_corridor' via the method next_scene of Map.

The method next_scene() can only be reached via the class Map or an instance of this class. In Engine such an instance is stored in self.scene_map. 
Therefore, you need to use self.scene_map.next_scene(). 
Just using next_scene(next_scene_name) will give you a NameError because there is no such function defined. 
Again, methods in a class are not visible throughout the whole module. They can only be accessed via a class or an instance.


Question 2
For this line,

return self.next_scene(self.start_scene)
Why is it necessary to specify the self in front of next_return? Why can't it be as follows?

return next_scene(self.start_scene)

Answer 2

While this line works:

return self.next_scene(self.start_scene)

this line does not work:

return next_scene(self.start_scene)


because the method next_scene is defined in the class Map. 
It is not a normal function in the global module space. 
You can call it either via the class Map.next_scene(a_map, 'name_of_scene') (not often done) or via the instance  a_map.next_scene('name_of_scene'). 
The self stands for any instance. Therefore, in this case you call a_map.next_scene('name_of_scene').
"""