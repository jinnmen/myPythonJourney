ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() # Remove the item at the given position in the list, and return it.
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!

"""
1. Take each function that is called, and go through the steps outlined above to translate them to what Python does.
For example, ' '.join*things) is join(' ', things).
2. Translate these two ways to view the function calls in English. For example, ' '.join(things) reads as "Join things with '' between them." 
Meanwhile, join(' ',things) means, "Call join with '' and things." Understand how they are really the same thing.
3. Go read about "Object Oriented Programming" online. Confused? I was too. Do not worry. You will learn enough to be dangerous, and you can slowly learn more later.
4. Read up on what a "class" is in Python. Do not read about how other languages use the word "class". That will only mess you up.
# Read up on class vs instances. Keywords: _init_
5. What's the relationship between dir(something) and the "class" of something?
6 Find out OOP vs functional programming. 
https://docs.python.org/2/howto/functional.html
"""