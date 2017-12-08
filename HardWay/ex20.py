# imports argv from module sys
from sys import argv 

# assigns 2 functions to argv
script, input_file = argv

# defines function print_all with parameter f
def print_all(f): 
	print f.read() #prints parameter f with read function which returns specified amount of bytes from file.
	
def rewind (f): # defines rewind with parameter f
	f.seek(0) # adds functions seek to set the file's current position to start reading from 0 = from beginning of file, 1 = current position, 2 = end of file.   f = file. 
	
def print_a_line(line_count, f): # defines print a line
	print line_count, f.readline() # print line_count, reads one entire line from file. http://python-reference.readthedocs.io/en/latest/docs/file/readline.html?highlight=readline

current_file = open(input_file) # opens a file returning a file object.

print "First let's print the whole file:\n" # prints string

print_all(current_file) # prints current file

print "Now let's rewind, kind of like a tape." #prints string

rewind(current_file) #repeats the file contents

print "Let's print three lines:" #prints string

current_line = 1 #assigns first line
print_a_line(current_line, current_file) # sets which line and file to print . Current_line =1

current_line = current_line + 1
print_a_line(current_line, current_file) # prints second line and file.  Current_line =2

