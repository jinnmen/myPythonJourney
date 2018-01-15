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
	print "You see 3 items on the table."
	print "A shield, a sword, and some garlic"
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
				items_picked.append("sword")
				break
			elif "garlic".lower() in next:
				print "You picked up garlic."
				items_picked.append("garlic")
				break
			else:
				print "I'm not sure what you want to do"
		

def door_left():
	print "Some alien bats charge at you!"
	while True:
		print "What do you do?"
		
		next = raw_input("> ")
	

"""
def door_middle():
	print "Undead zombies!"
	
	while True:
		print "Your move?!"
		
		next = raw_input("> ")
		
		if next.lower == "Use garlic":
			print die("They're zombies! Not vampires!")
		elif 
"""			
		

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
		
def silver_room():
	print "Welcome to the silver room"
	
def die(end):
	print "You're dead!", end
	exit(0)
	
#table()	#start game from table, test code
in_castle() # start game from castle, to test code		
# gow() # start game from beginning