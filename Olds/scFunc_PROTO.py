from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from scrapy import Spider, Request

WHITE = '\033[97m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_RED = '\033[41m'
BACKGROUND_MAGENTA = '\033[45m'
RESET = '\033[0m'

# providing url 
url = urlopen('https://www.shellcheck.net/wiki/SC2033')
bs = BeautifulSoup(url.read(), 'html.parser')
#print(bs)

title = bs.find('title')
print('\n', title.get_text())

    
h1 = bs.find('h3', {'id':'problematic-code'}).get_text()
print('\n', '\n', BACKGROUND_RED + WHITE + h1 + RESET)
for child1 in bs.find('div', {'id':'cb1'}):
    print('\n', '#', child1.get_text(), '\n')
        
h2 = bs.find('h3', {'id':'correct-code'}).get_text()
print('\n', '\n', BACKGROUND_GREEN + WHITE + h2 + RESET)
for child2 in bs.find_all('div', {'id':re.compile('cb2|cb[3-9]')}):
    print('\n', '#', child2.get_text(), '\n')
    
for div in response.selector.css('.sourceCode'):
    if div.css('div[id="correct-code"]'):
        for child2 in bs.find_all('div', {'id':re.compile('cb2|cb[3-9]')}):
            print('\n', '#', child2.get_text(), '\n')
            
h3 = bs.find('h3', {'id':'rationale'}).get_text()
print('\n', '\n', BACKGROUND_MAGENTA + WHITE + h3 + RESET)
for child3 in bs.find_all('div', {'id':re.compile('cb5|cb[6-9]')}):
    print('\n', '#', child3.get_text(), '\n')
    
    
# https://www.youtube.com/watch?v=MMyTGhgvH4A
# https://www.synvert-tcm.com/blog/web-scraping-using-python-scrapy/
# https://scrapy2.readthedocs.io/en/latest/topics/selectors.html
# https://stackoverflow.com/questions/41696386/scrapy-conditional-crawling
