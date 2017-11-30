# imports argv feature from the system package
from sys import argv

# adds variables script and filename into argv function to get a file name
script, filename = argv

#assigns open filename function to txt
txt = open(filename)

#prints string filename
print "Here's your file %r: " % filename
#Gives file a command using the . 
print txt.read() # do read command with no parameters

#closes files when done
end1 = txt.close()

#prints string Type...
print "Type the filename again: "
#prompts user to input file name again
file_again = raw_input("> ")

#opens the file by file_again parameter for what user has input
txt_again = open(file_again)

#prints out by reading the file called by user
print txt_again.read()

#closes files when done
end2 = txt_again.close()