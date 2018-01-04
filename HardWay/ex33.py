i = 0
numbers = []

#if don't get rid of incrementor, the numbers will not add up correctly. Only applies to the first number.
for i in range(0, 20, 2): # range 0 to 20, with increments of 2.
	print "At the top i is %d" % i
	numbers.append(i)
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
		
print "The numbers: "

for num in numbers:
	print num
