from nose.tools import *
import NAME

def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic():
	print "I RAN!"
	
# game.py section

"""
class Room(object):
	
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
"""