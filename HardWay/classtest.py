class Human(object):
	# This will create Human type object
	
	
	def __init__(self):
		print "Human object is created."
	
	def __str__(self):
		return "This prints another line."
			
	#def __str__(self):	
		#return "Third line."
		
		
a = Human()

print a