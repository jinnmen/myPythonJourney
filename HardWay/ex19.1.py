def life1(dollar_count,something):
	print "Now you'll have to pay $%d if you want to live" % dollar_count
	print "Or you can choose to die!!"
	print "But wait! You can also choose to say %s" % something
	print "What'll it be?"

question1 = raw_input("Say hello: ")

dollar_count = 100
something = "No!"

life1(dollar_count, something)