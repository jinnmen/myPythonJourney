print "Let's practise everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. # \n is new line, \t is tab
"""

print "______________"
print poem
print "______________"

five = 10 - 2 +3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) #prints string with decimal variables individually. Changed jelly beans to beans as this is part of function. Can change to any value as long as match order.

start_point = start_point / 10 # divides start point by 10

print "We can also do that this way:" # prints string
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) #print's string with decimal variables from function secret_formula(<#started#>)