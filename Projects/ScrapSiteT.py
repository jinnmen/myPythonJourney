# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# import libraries
import urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

import re

# specify the url
quote_page = 'http://yealink.com/news.html'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

link = soup.find("a class" , href="/news")
print link