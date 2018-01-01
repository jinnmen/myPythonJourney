print "You enter a dark room with two doors. Do you go through door #1, door #2, door #3 or door #4?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear." 
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a poool of muck. Good job!"

elif door == "3":
	print "You see a big hat with the number 3. It says 'You have 3 choices'"
	print "1. Choose Gryffindor"
	print "2. Choose Slytherine"
	print "3. Choose Ravenclaw"
	
	hp = raw_input("> ")
	
	if hp == "1":
		print "Welcome Harry!"
	elif hp == "2":
		print "Welcome Snape"
	else:
		print "Yes! You are the one Mr %s ." % hp
		
elif door == "4":
	print "You see a big hat with the number 4. It looks like a hat you saw, it says 'You have 3 choices'"
	print "1. Choose Gryffindor"
	print "2. Choose Slytherine"
	print "3. Choose Ravenclaw"
	
	hp = raw_input("> ")
	
	if hp == "1":
		print "Welcome Harry!"
	else:
		print "No choose 1!!!"
	if hp == "2":
		print "Welcome Snape"
	else:
		print "Noooo choose 2!!!"
	if hp == "3":
		print "Yes! You are the one Mr %s ." % hp
	else:
		print "Noooo choose 3!!!"
		
else:
	print "You stumble around and fall on a knife and die. Good job!"