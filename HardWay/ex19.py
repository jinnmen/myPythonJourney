# defines variable cheese_and crackers with parameters cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count #prints string which includes decimal numerical cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers #prints string which includes decimal numerical boxes_of_crackers
	print "Man that's enough for a party!" #prints string
	print "Get a blanket.\n" #prints string 

print "We can just give the function numbers directly: " #prints string
cheese_and_crackers(20,30) #calls the function cheese_and_crackers with the parameter values 20 for cheese_count and 30 for boxes_of_crackers

print "OR, we can use variables from our script:" #prints string
amount_of_cheese = 10 #assigns value 10 to amount_of_cheese variable
amount_of_crackers = 50 #assigns value 50 to amount_of_crackers variable

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #assigns variables amount_of_cheese and amount_of_crackers into function cheese_and_crackers

print "We can even do math inside too:" #prints string
cheese_and_crackers(10 + 20, 5 + 6) #calls function cheese_and_crackers which includes parameters 10+20, 5+6 , calculation can be done inside function's parameter.

print "ANd we can combine the two, variables and math:" #prints string
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #calls cheese_and_crackers with variable and number parameters