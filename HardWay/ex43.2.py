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

class Musical_box(object)

    def __init__(self, scene_map):
	self.scene_map = scene_map

    def play(self):
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
	    print Death.dendings[randint(0, len(self.dendings)-1]
	    exit(1)

def WhiteRoom(Scene):

    def enter(self):
	print 