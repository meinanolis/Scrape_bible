from bs4 import BeautifulSoup
from urllib.request import urlopen

#url='https://www.bibleserver.com/text/HFA/1.Mose1'
#page = urlopen(url)


pagepath='1.Mose 1 - Hoffnung für Alle   BibleServer.html'

f=open(pagepath,'r')
page=f.read()
f.close()

soup = BeautifulSoup(page, 'html.parser')

chapter=soup.find('div', class_='chapter')

verses=list()
for v in chapter.find_all('div',class_='verse'):
    v.span.decompose()
    verses.append(v.text)
print(verses)