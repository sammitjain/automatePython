# Web scraping and parsing with BS4
# Part1

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
#sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Krondor%27s_Sons').read()
soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup) Gives you the source code essentially
    
# print(soup.title) Gives HTML style tag information

print(soup.title.string)

# OR print(soup.title.text)

#This prints the first paragraph
#print(soup.p)

#Now if you want to print all paragraphs try this:

#print(soup.find_all('p'))

##for paragraph in soup.find_all('p'):
##    print(paragraph.text) #with child tags, or else use .string
    

print(soup.get_text()) #All the text

#The following prints out all the links
for url in soup.find_all('a'):
    print(url.get('href'))

