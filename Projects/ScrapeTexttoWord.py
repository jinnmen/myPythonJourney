"""
Scrape Texts from http site then export to Word (does not work on https)
References:
https://python-docx.readthedocs.io/en/latest/
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation
https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
"""

import urllib2
import urllib3
from bs4 import BeautifulSoup

from docx import Document
from docx.shared import Inches

import requests

document = Document()

quote_page = 'http://www.magickeys.com/books/gingerbread/index.html'
response = requests.get(quote_page, verify = False)
response.status_code

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('p')

name = name_box.text.strip()

print name


# Export to doc
p = document.add_paragraph(name)

document.add_page_break()

document.save('pyscrape.docx')

