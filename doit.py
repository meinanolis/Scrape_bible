from bs4 import BeautifulSoup
from urllib.request import urlopen

#url='https://www.bibleserver.com/text/HFA/1.Mose1'
#page = urlopen(url)

class vers:
    def __init__(self,html):
        self.html=html
        self.number=self.html.find('span',class_='verseNumber').text
        self.htmlclone=BeautifulSoup(str(self.html))
        self.htmlclone.span.decompose()
        self.text = self.htmlclone.text

class headline:
    def __init__(self,html):
        self.html=html
        self.text=self.html.text


pagepath='Quelltexte/01-1Mose1.html'

f=open(pagepath,'r')
page=f.read()
f.close()

soup = BeautifulSoup(page, 'html.parser')
main=soup.find(id='pageMain')

chapter=main.find('div', class_='chapter')

verses=list()
for v in chapter.contents:
    ve=None
    try:
        if 'caption' in v['class']:
            ce=headline(v)
        elif 'verse' in v['class']:
            ce=vers(v)
        verses.append(ce)
    except:
        pass
print(len(verses))
print(verses[0].text)

