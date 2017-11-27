#import adds features/modules to script from Python feature set. Eg. sys is a module/library.
#argv is argument variable.  

from sys import argv

#unpacks argv then assigns to 4 values
script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third

# when running terminal must add 3 variables behind file destination so no error.

test = raw_input()
print test