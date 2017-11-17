#assigns cars with value of 100
cars = 100
#assigns space in car as float value of 4
space_in_a_car = 4
#assigns drivers with value of 30
drivers = 30
#assigns passengers with value of 90
passengers = 90
#Calculates the total of cars not driven by subtracting drivers from cars
cars_not_driven=cars-drivers
#sets value of cars driven as same number of drivers
cars_driven=drivers
#carpool capacity calculation is done by multiplying number of cars driven by space available in a car
carpool_capacity=cars_driven*space_in_a_car
#calculates average passengers per car by dividing passengers by cars driven
average_passengers_per_car=passengers/cars_driven

#prints words and calls value for cars
print "There are" , cars, "cars available."
#prints words and calls value for drivers
print "There are only", drivers, "drivers available."
#prints words and calls value for cars_not_driven
print "There will be", cars_not_driven, "empty cars today."
#prints words and calls value for carpool_capacity
print "We can transport", carpool_capacity, "people today."
#prints words and calls value for passengers
print "We have", passengers, "to carpool today."
#prints words and calls value for average_passengers_per_car
print "We need to put about", average_passengers_per_car,"in each car."

#without using spaces between words, can still print
print "Hey %s there." % "you"

