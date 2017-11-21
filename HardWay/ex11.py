print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
#raw input represents a prompt to the user (the optional arg of raw_input([arg])), gets input from the user and returns the data input by the user in a string. 