name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

cm = height/2.54 #inches to cm
kg = weight/0.453592 #pound to kg

print "Let's talk about %s" % name
print "He's %i inches tall. Or %.2f cm tall" % (height, cm)
print "He's %i pounds heavy. Or %.4f kg heavy" % (weight, kg)
print "Actually that's not too heavy. "
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee. " % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " % (
	age, height, weight, age + height + weight)
print "Alternatively, in cm and kg, if you add %d, %6f, and %6f, you'd get %8f " %(
	age, cm, kg, age + cm + kg) # %.6f or %6f produces same results. i=d for integer decimal, s for string.
	
#python format characters: https://docs.python.org/2.4/lib/typesseq-strings.html