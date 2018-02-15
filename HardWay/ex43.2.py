"""
Story
Planet of the capes
You awake abruptly and find yourself in a mysterious white cape. 
You're in a strange room with surrounded in 4 white walls, a white ceiling and a white floor.
As you struggle, the cape tightens.
What do you do?

action-> Stop

Enter
next

Beginning white room and white cape
death

Scenes
Death: When player dies and should be something gory
White Room: Starting point and has white cape waiting to strangle user
Black Room: pitch black, kindle - fire
Gray Room: Purgatory, tear gray cape to fully wake up.
Wake up: End of game, sweat and never wear a cape anymore.

List of nouns:
Map
Cape
Player
Room
Scene
Kindle
fire
Water

Make class hierarchy
*Map
	-opening_scene
	-next_scene
*Kindle
	-ignite
* Scene
	-enter
	*Death
	*white_room
	*black_room
	*gray_room
- enter under scene, all scenes under it will inherit and override it.

"""

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is under construction"
	exit(1)

class Kindle(object):

    def __init__(self, scene_map):
	self.scene_map = scene_map

    def ignite(self):
	current_scene = self.scene_map.opening_scene()

	while True:
	    print "\n------------"
	    next_scene_name = current_scene.enter()
	    current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	
	dendings = [
	    "Death is like sweet candy. You savour it.",
	    "You really need to improve in gaming.",
	    "Your imaginary 4 year old sister can play better than you."	
	]

	def enter(self):
	    print Death.dendings[randint(0, len(self.dendings)-1)]
	    exit(1)

def WhiteRoom(Scene):

    def enter(self):
	print "You awake abruptly and find yourself in a mysterious white cape."
	print "You're in a strange room with surrounded in 4 white walls,"
	print "a white ceiling and a white floor."
	print "As you struggle, the cape tightens."
	print "What do you do?"
	
	action = raw_input("> ")
	
	if action == "struggle":
		print "The more you move the tighter it gets"
		print "You lose air"
		return 'death'
		
	elif action == "stop":
		print "The cape loosens, something drops down onto you from above your head."
		print "Darkness befalls you, as you reach out, you touch something silky"
		print "This time, it's another cape but black"
		return 'BlackRoom'
	
	else:
		print "Type something sensible!"
		return 'WhiteRoom'

def BlackRoom(Scene):
	
	def enter(self):
		print "The room is pitch black."
		print "As you move your hands around,"
		print "You touch something that feels like 1 wood and 2 stones"
		print "You try to ignite a kindle but how many times do you try?"
		ignite = "%d%d" % (randint(1,2),randint(1,2))
		guess = raw_input("> ")
		guesses = 0
		
		while guess != ignite and guess < 7:
			print "Chk chk chk, nothing happens"
			guesses += 1
			guess = raw_input(">")
		
		if guess == ignite:
			print "A kindle lits up the room bright as daylight."
			return 'grayroom'
		else:
			print "You ran out of wood and stones..."
			print "Darkness engulfs you"
			return 'death'
		
class GrayRoom(Scene):
	
	def enter(self):
		print "As your eyes adjust to the sudden flash of light."
		print "You can now see yourself in a gray room."
		print "There are 3 doors in front of you."
		print "One of which may be your very chance to escape this strange place."
		print "However, the doors seem to randomly change positions."
		print "Which door do you pick? (1 to 3)"
		
		escape = randnint(1,3)
		guess = raw_input("[Door #]> ")
		
		if int(guess) != escape:
			print "You opened the door and rush towards your exit"
			print "However, your next step proved fatal."
			return 'death'
		else:
			print "You open the door to your escape"
			print "Running as fast as you could, you don't look back."
			
			return 'finished'
			
class Map(object):
	
	scenes = {
		'whiteroom': WhiteRoom(),
		'blackroom': BlackRoom(),
		'grayroom': GrayRoom(),
		'death': Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self,scene_name)
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)