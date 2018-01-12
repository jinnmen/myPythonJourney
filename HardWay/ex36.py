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
	print "You see a table, a door on the left, a door in the middle and a door on the right."
	print "What do you do?"
	
	while True:
		next = raw_input("> ")
		if "table" in next:
			print "You see 3 items on the table."
			print "A shield, a sword, and some garlic"
			print "What do you do?"
		
		while True:
			next = raw_input("> ")

			if "shield".lower() in next:
				print "You picked up a shield of the sun!"
				items_picked.append("shield")
				items[0]
				print items_picked
				print items_picked[0]
			elif "sword".lower() in next:
				print "You picked up a sword of truth!"
				items_picked.append("sword")
				items[1]
			elif "garlic".lower() in next:
				print "You picked up garlic."
				items_picked.append("garlic")
				items[2]
			else:
				print "I'm not sure what you want to do"
		



def silver_room():
	print "Welcome to the silver room"
	
def die(end):
	print "You're dead!", end
	exit(0)
		
gow()