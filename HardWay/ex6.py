#Assigns string #"There are..." with a decimal 10 inside to variable x
x = "There are %d types of people. " % 10
#Assigns variable binary to string binary
binary = "binary"
#Assigns variable do_not to string don't
do_not = "don't"
#assigns var y to string "Those..." then include 2 strings inside - binary and do_not which were assigned above
y = "Those who know %s and those who %s. " % (binary, do_not) #string is inside string 2x

#prints variable x
print x
#prints var y
print y

#prints string and then uses %r repr() . x as a whole which had string and decimal
print "I said: %r." % x #string is inside string
print "I also said: '%s'." % y  #string is inside string

#testing
happy = True
sad = False 
print "Happy is?! %r"
print "Sad is?! %r"

#assigns var hilarious as False
hilarious = False
#print string with %r which repeats above line
joke_evaluation = "Isn't that joke so funny?! %r"

#prints variables joke and hilarious with a space in between
print joke_evaluation % hilarious

#assigns var w to string "This is..."
w = "This is the left side of..."
#Assigns var e to string "a string..."
e = "a string with a right side."

#prints combination of both w+e
print w+e