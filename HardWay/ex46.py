# Skeleton contents
# commands for terminal

"""
mkdir projects
cd projects/
mkdir skeleton
cd skeleton
mkdir bin
mkdir NAME
mkdir tests
mkdir docs

touch NAME/__init__.py
touch tests/__init__.py

"""

# This is a new file: setup.py
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My Project',
	'author' : 'My Name',
	'url' : 'URL to get it at.',
	'download_url' : 'Where to download it.',
	'author_email' : 'My email.',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'projectname'	
}

setup(**config)

# This is a new file NAME_tests.py

from nose.tools import *
import NAME

def setup():
	print "SETUP!"
	
def teardown():
	print "TEAR DOWN!"
	
def test_basic():
	print "I RAN!"

"""	
nose needs to be installed: pip install nose
disribute and virtualenv needs to be installed the same way too
"""