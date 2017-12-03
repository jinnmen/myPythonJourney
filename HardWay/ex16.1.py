from sys import argv

script, filename = argv

print "We're goign to erase %r. " % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1, line2, line3 = raw_input("line 1:, line 2:, line 3: in one line separated by comma: ").split(",")

print "I'm going to write these to the file."

line="\n"
target.write(line1+line+line2+line+line3)

print "And finally, we close it."
target.close()