# Web scraping with Beautiful Soup 4 Part 3
# Working with tables
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce,'xml')

#print(soup)

for url in soup.find_all('loc'):
    print(url.text)
