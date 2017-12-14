# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
# creates a file handler myfile 
myfile = open ("/Users/l.jinnmen/Documents/Qloog/pyway-master/J/ScrapSite/threesisters.html", "r")
data = myfile.read()
soup = BeautifulSoup(data,'html.parser')

print(soup.prettify())