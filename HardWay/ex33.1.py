i = 0
numbers = []

# while i is less than 20
while i < 20:
	#print's the first i, from global this is 0
	print "At the top i is %d" % i
	# adds first number into numbers list
	numbers.append(i)
	
	#calculation for i + 2
	i = i + 2
	#does not calculate here, prints numbers list starting with 0
	print "Numbers now: ", numbers
	#starts calculating here, prints i which is 0 +2 ,according to formula.
	print "At the bottom i is %d" % i

#after loop only prints numbers
print "The numbers: "

for num in numbers:
	print num
	
