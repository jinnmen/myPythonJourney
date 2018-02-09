"""
Write out nouns/ draw problem. 
A lil' paragraph for the game:
Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. 
The game will be more like a Zrok or Adventure type game with text outputs and funny ways to die.
The game wil involve an engine that runs a map full of rooms or scenes. Each room will print its own description when the
player enters it and then tell the engine what room to run next out of the map.

Describe each scene:
Death: When player dies and should be something funny.
Central Corridor: Starting point and has Gothon already standing there they have to defeat with a joke before continuing
Laser Weapon Armory: When hero gets neutron bomb to blow up ship before getting escape pod. Keypad and has to guess number.
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
	
Go through and figure out what actions needed based on verbs. "run" engine, "Get next scene" from map, "opening scene", "enter" scene:
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
class Scene(object):
	
	def enter(self):
		pass

class Engine(object):

	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
		
class Death(Scene):

	def enter(self):
		pass

class CentralCorridor(Scene):

	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass
		
class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass
		
class Map(object):

	def __init__(self, start_scene):
		pass
	
	def next_scene(self, scene_name):
		pass
	
	def opening_scene(self):
		pass
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
