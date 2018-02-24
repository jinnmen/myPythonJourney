"""
1. Make a different game from the one I made.

2. Use more than one file, and use import to use them. Make sure you know what that is.

3. Use one class per room and give the classes names that fit their purpose. Like GoldRoom, KoiPondRoom.

4. Your runner will need to know about these rooms, so make a class that runs them and knows about them. There's
plenty of ways to do this, but consider having each room return what room is next or setting a variable of what
room is next.

5. Add comments!


Game concept and idea:
Have 3 dogs, 3 rooms
Need to teach them 1 skill each that matches room requirements to clear
The skills needs to be fetched from other files.
A tale of 3 dogs: Dido, Fido, Kido
tricks: roll, jump, sit
rooms : R, J, S
get a bone for each room's trick cleared. 
After getting 3 bones, you win as best dog trainer of 2018.

For story starting scene, read from file (ex.15)
"""

from sys import argv

#To run this correctly, type python this file name + "/Users/Mac/Documents/jimmy personal/python/ex45op.txt"
script, filename = argv

txt = open(filename)

print "Contents of file opened %r: " % filename
print txt.read()

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

