#!/usr/bin/python
# -*- coding: <utf-8>-*-

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals[1]
print animals[2]
print animals[0]
print animals[3]
print animals[4]
print animals[2]
print animals[5]
print animals[4]

"""
1. The animal at 1 is the 2nd animal and is a python. The 2nd animal is at 1 and is a python.
2. The 3rd animal is at 2 and is a peacock. The animal at 2 is the 3rd animal and is a peacock.
3. The 1st animal is at 0 and is a bear. The animal at 0 is the 1st animal and is a bear.
4. The animal at 3 the 4th animal and is a kangaroo. The 4th animal is at 3 and is a kangaroo.
5. The 5th animal is at 4 and is a whale. The animal at 4 is the 5th animal and is a whale.
6. The animal at 2 is the 3rd animal and is a peacock. The 3rd animal is at 2 and is a peacock.
7. The 6th animal is at 5 and is a platypus. The animal at 5 is the 6th animal and is a platypus.
8. The animal at 4 is the 5th animal and is a whale. The 5th animal is at 4 and is a whale.
Study drills
2. For dates before the year 1, unlike the proleptic Gregorian calendar used in the international standard ISO 8601, the traditional proleptic Gregorian calendar (like the Julian calendar) does not have a year 0 and instead uses the ordinal numbers 1, 2, ... both for years AD and BC. Thus the traditional time line is 2 BC, 1 BC, AD 1, and AD 2. ISO 8601 uses astronomical year numbering which includes a year 0 and negative numbers before it. Thus the ISO 8601 time line is -0001, 0000, 0001, and 0002.
"""

office = ['kim', 'jeong', 'erki', 'robot']


print "The 1st person and at 0 is kim. The person at 0 is the first person and is %s." % office[0]
print "The 2nd person and at 1 is jeong. The person at 1 is the second person and is %s." % office[1] 
print "The person at 3 is the 4th person and is robot. The 4th person is at 3 and is %s." % office[3]
print "The person at 2 is the 3rd person and is %s. The 3rd person is at 2 and is %s." % (office[2], office [2])