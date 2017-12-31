people = 50
cars = 80
buses = 70

# creates a condition for when cars are more than people, to print "We should take the cars", otherwise print "We should not take the cars" when people are more than cars, else to print "We can't decide"
if cars > people:
	print"We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# creates a condition for when buses are more than cars, to print "That's too many buses.", otherwise print "Maybe we could take the buse" when buses are more than cars, else to print "We still can't decide."
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else: 
	print "We still can't decide."

# creates a condition for when people are more than buses, to print "Alright, let's just take the buses", otherwise print "Fine, let's stay home then." when buses are more than people or all other conditions
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
# 2 if conditions then print statement.
if cars > people and buses < cars:
	print "There's more cars than people and buses"
	
# elif = else if, it allows more conditions to be executed when if is True.
