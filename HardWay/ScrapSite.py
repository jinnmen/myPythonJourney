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

# Take out the <div> of name and get its value
name_box = soup.find('div', attrs={'class': 'name'})
name = name_box.text # .strip() is used to remove starting and trailing 
print name

# Get time of content publication
time_box = soup.find('div', attrs = {'class': 'time'})
time = time_box.text 
print time

# Get contents of title
content_box = soup.find('p') 
content = content_box.text
print content

# Get website link of content : https://pythonspot.com/extract-links-from-webpage-beautifulsoup/
#for link in soup.findAll('a', attrs = {'href':re.compile("^http://")}):
#    print link.get('href')

# get the index price
## price_box = soup.find('div', attrs={'class': 'price'})
## price = price_box.text
## print price

# get the contents

# Export to Excel CSV
# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, time, content, link, datetime.now()])