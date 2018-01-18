import time
import sys
from time import sleep
import re

items = ['shield', 'sword', 'garlic']
# items = False
items_picked = []
# gow() = False
life = True

def gow():
	print "Welcome to the Game Of Wonders!"
	print "You see a castle, what do you do next?"
	print "Do you go in to the castle or flee?"
	
	while True: 
		next = raw_input("> ")
		if "go" in next:
			in_castle()
		elif next == "flee":
			print die("Goodbye!")
		else:
			"Sorry I don't know what you mean"

def in_castle():
	print "Welcome to the Castle! It's dimly lit by warm torches on the wall."
	
	while True:		
		print "You see a table, a door on the left, a door in the middle and a door on the right."
		print "What do you do?"
		next = raw_input("> ")
		if "table" in next:
			table()
		elif "left" in next:
			door_left()
		elif "middle" in next:
			door_middle()
		elif "right" in next:
			door_right()
		else:
			print "Sorry I'm not sure what you would like to do"


def table():	
	print "You see 4 items on the table."
	print "A shield, a sword, some garlic and holy water"
	print "What do you do?"
	
	while True:
			next = raw_input("> ")

			if "shield".lower() in next:
				print "You picked up a shield of the sun!"
				items_picked.append("shield") if "shield" not in items_picked else None #No duplicates into list #https://stackoverflow.com/questions/19834806/is-there-a-more-pythonic-way-to-prevent-adding-a-duplicate-to-a-list
				# print items[0] #prints first item, item 0
				print items_picked #prints items picked in list form
				print items_picked[0] #prints items within list 
				# exit(0) #exit(1) does not go back to castle. How to?
				break #breaks the current True statement then heads back to earlier. Can break, continue, pass, return, exit.
			elif "sword".lower() in next:
				#print "You picked up a sword of truth!"
				print "You picked up a %s of stars!" % items_picked[0]
				items_picked.append("sword") if "sword" not in items_picked else None
				break
			elif "garlic".lower() in next:
				print "You picked up garlic."
				items_picked.append("garlic") if "garlic" not in items_picked else None
				break
			elif "holy water".lower() in next:
				print "You picked up holy water."
				items_picked.append("holy water") if "holy water" not in items_picked else None
				break
			else:
				print "I'm not sure what you want to do"
		

def door_left():
	print "Some alien bats charge at you!"
	while True:
		print "What do you do?"
		
		next = raw_input("> ")
	
		if next.lower() == "fight":
			if "sword" in items_picked and "shield" in items_picked: #Why can't use [] or ()== True or False?
				print "You used both sword and shield!"
				time.sleep(1)
				print "swoosh! You slash some bats heads off"
				time.sleep(2)
				print "ping! (some bats smack into your shield)" 
				time.sleep(1)
				print "You killed all bats! Now you proceed into the next room"
				silver_room()
			elif "sword" in items_picked and "shield" not in items_picked:
				print "You used sword!"
				time.sleep(1)
				print "swosh!!! You slice some bats."
				time.sleep(1)
				print "But you have no shield!"
				time.sleep(1)
				print die("ping! Some bats smash into you and you die.")
			elif "sword" not in items_picked and "shield" in items_picked:
				print "You used shield!"
				time.sleep(1)
				print "ping!!! You defended some bats."
				time.sleep(1)
				print "But you have no sword!"
				time.sleep(1)
				print die("They overpower you and bite your head off.")
			else:
				print "You can't run away from the alien bats, they bite your ass off"
				time.sleep(1)
				print die("Goodbye young knight")
		else:
			print die("Goodbye dummy")
			
					
	
def door_middle():
	print "Undead zombies!"
	
	while True:
		print "Your move?!"
		
		next = raw_input("> ")
		
		if next.lower() == "Use garlic".lower():
			print die("They're zombies! Not vampires!")
		elif next.lower() =="Use holy water".lower():
			if items_picked("holy water") == True:
				print "You kicked zombie ass!"
				silver_room()
			else:
				print die("You would if you could, but you can't because you don't have it!")
		elif next.lower() == "flee".lower():
			print "You run away screaming like a little girl."
			break
		else:
			print "Please type in English, not jibberish."
		

def door_right():
	print "There's nothing here, phew!"
	print "Do you want to go through the door? (Yes/No)"
	
	while True:
		next = raw_input ("> ")
		
		if next.lower() == "yes":
			print "The room you walked into is pitch dark. Your next step was fatal as you walk straight into a death trap."
			print die("Game Over.")
		elif next.lower() == "no":
			print "You smell something fishy then take a step back."
			break
		else:
			print "Please key in something I could understand"
		
words = """Welcome to the silver room.\nIn here, time seems to slow down.\nYou feel comfortable but see tons of silver.\nHow much do you take?\n"""
def delay_typer(words, delay = 0.5, stream = sys.stdout):
	tokens = re.findall(r'\s*\S+\s*', words) # remove '+ beside S to print word by word, for more info on regular expressions: https://developers.google.com/edu/python/regular-expressions'
	for s in tokens:
		stream.write(s)
		stream.flush()
		sleep(delay)

def silver_room():
	delay_typer(words)
	
	next = raw_input("> ")
	
	if next == int and int(next) < 100:
		delay_typer('You aren\'t greedy, you snap and wake up from the spell, time speeds up again.\nYou wake up from the castle dream and things go back to normal\nThe End\n', 0.1)
	else:
		delay_typer(die("You either can't type of are too greedy!\nYou live in the curse forever til the end of time.\n"), 1)
	
	
	
def die(end):
	print "You're dead!", end
	exit(0)
	
#table()	#start game from table, test code
#in_castle() # start game from castle, to test code		
# gow() # start game from beginning
silver_room()