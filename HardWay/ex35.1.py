from sys import exit # import the function exit from system

def strange_room():
	print "This room is strange. Dr. Strange is sitting on a chair. There's a door behind him. What do you do?"
	
	while True:
		next = raw_input("> ")
	
		if next == "say hi":
			dead("He says hi back to you and fall into eternal slumber")
		elif next == "nothing":
			dead("You both do nothing for eternity")
		elif "Ignore".lower() in next:
			print "Wise move, he ignores you too then you proceed to the gold room"
			gold_room()
		else:
			print "I'm not sure what you mean."

def gold_room(): #creates a new variable gold_room, step 4
	print "This room is full of gold. How much do you take?" #prints string
	
	next = raw_input("> ") #creates next variable, asks users to key in.
	if "0" in next or "1" in next: #if statement with 0 or 1.
		how_much = int(next) # creates how_much variable, with integer next parameter
	else:
		dead("Man, learn to type a number.") # other than numbers prints this string.
		
	if how_much < 50: #if less than 50
		print "Nice, you're not greedy, you win!" #prints string.
		exit(0) #exits code
	elif how_much > 100 and how_much < 1001:
		print "Just nice you rich b**tard!"
		exit(0)
	elif how_much > 1000:
		dead("You're too greedy for your own good man!")
	else: # otherwise prints string within dead var (along with dead var)
		dead("You greedy bastard!")
		
def bear_room(): #creates step 2 to move bear
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False # sets bear_moved variable default as False
	
	while True: # creates while loop
		next = raw_input("> ") #asks question for next var under bear_room indentation.
		
		if next == "take honey": #if ans is take honey
			dead("The bear looks at you then slaps your face off.") #reply with string then dead's string
		elif next == "taunt bear" and not bear_moved: #if taunt bear, and not False
			print "The bear has moved from door. You can go through it now." # bear moved
			bear_moved = True #sets bear_moved to True, perhaps won't need this
		elif next == "taunt bear" and bear_moved: # if taunt bear 2nd time and False
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved: #open door to enter gold room
			gold_room()
		else:
			print "I got no idea what that means." #if type anything else asides from above settings.
			
def cthulhu_room(): #creates var cthulhu_room. When first turned right
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	next = raw_input("> ") #allows user to key in.
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why): #defines var dead with parameter why
	print why, "Good job!"  #whys above + this extra sentence.
	exit(0) #exits.
	
def start(): #step 1, start.
	print "You are in a dark room."
	print "There is a door to your right, middle and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "middle":
		strange_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.") #dead, game over.
		
start() #starts function