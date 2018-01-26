# Creating class try
class Say(object):
	#objects can save variables, functions
	def __init__(self, speech):
		self.speech = speech
		
	def tell_me_something(self):
		for line in self.speech:
			print line

say_hi = Say(["Hello. Friday is a good day",
			"But not sure about other days",
			"Let's see how it goes..."])

say_bye = Say(["Bye. It's the weekend!",
			"What should we do now I wonder."])

say_hi.tell_me_something()

say_bye.tell_me_something()