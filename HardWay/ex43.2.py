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