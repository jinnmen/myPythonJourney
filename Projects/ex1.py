# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
# creates a file handler myfile 
myfile = open ("/Users/l.jinnmen/Documents/Qloog/pyway-master/J/ScrapSite/threesisters.html", "r")
data = myfile.read()
soup = BeautifulSoup(data,'html.parser')

#print(soup.prettify())

#print soup.title

#print soup.title.name

#print soup.title.string

#print soup.title.parent.name

#print soup.p

#print soup.p['class']

#print soup.a

#print soup.find_all('a')

print soup.find(id = "link3")

for link in soup.find_all('a'):
    print(link.get('href'))