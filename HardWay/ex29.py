people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
	
#eg to q4
if people == dogs or cats <= dogs:
	print "What?!!"
	
if people != dogs or people <> cats:
	print "No way!"

"""
1. I think if is a conditional statement. It executes the code only if the conditions are met.
2. The code needs to be indented 4 spaces as it belongs to the local chunk of code. Not global. -> So python knows its the if block.
3. If not indented, code won't be recognized as local. Will be executed but not as if block.
4. Yes. 
5. You'll need to change the variables throughout the code too. Get different print statement.
"""