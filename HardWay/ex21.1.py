def modulo(a,b):
	print "MODULO %d and %d" % (a, b)
	return a % b
	
	
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
timeleft = modulo(10, 3)

print "Age: %d, Height: %d, Weight: %d, IQ: %d, Time Left %d" % (age, height, weight, iq, timeleft)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# what = Height - IQ / 2 x weight + Age 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

what2 = height - iq / 2 * weight + age

print "That becomes: ", what, "Can you do it by hand?"

print what2