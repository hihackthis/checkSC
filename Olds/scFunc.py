from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

WHITE = '\033[97m'
BACKGROUND_GREEN = '\033[42m'
BACKGROUND_RED = '\033[41m'
RESET = '\033[0m'

# providing url 
url = urlopen('https://www.shellcheck.net/wiki/SC2031')
bs = BeautifulSoup(url.read(), 'html.parser')
#print(bs)


#divs = bs.find_all('h2', class_='heading-element')
#for div in divs:
    #div_h2 = div.get_text()
    #print(div_h2)
    
#divs = bs.find_all('h3', class_='heading-element')

#divs1 = bs.select('.va.ex.st')
#for div in divs:
    #div_h3 = div.get_text()
#print(divs1, end="\n")

#divs2 = bs.find('div', class_='highlight highlight-source-shell notranslate position-relative overflow-auto').find_next(string=True)
#for div in divs:
#print(divs2, end='\n')

#for parent_div in bs.find_all('div', class_='sourceCode'):
#parent_div = bs.find('div', class_='sourceCode')
#child_div1 = parent_div.find('span', class_='va').text
#child_div2 = parent_div.find('span', class_='ex').text
#child_div3 = parent_div.find('span', class_='st').text
#print(child_div1, child_div2, child_div3)
    #if child_div:
        #process_data(child_div)
        #print(child_div)
    
    #html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div[3]/div/div[1]/div/div[1]/div[3]/pre/span[2]/text()
    
#for h1 in bs.find('h2', {'id':'dont-use--on-the-left-side-of-assignments'}).descendants:
    #print('\n', h1.get_text(), end='')
    
#for h0 in (bs.find('h2', {'id':'dont-use--on-the-left-side-of-assignments'}).get_text()):
#    print('\n', h0, end='')
    
#h1 = (bs.find('h2', {'id':'dont-use--on-the-left-side-of-assignments'}).get_text(' | ',strip=True))
#print('\n', h1, end='')

title = bs.find('title')
print('\n', title.get_text())

#h1 = (bs.find(re.compile('h1|h2'), {'id':re.compile('.*')}).get_text(' ',strip=True))
#print('\n', h1)
    
# for h2 in bs.find_all('h3', {'id':re.compile('[A-Za-z_-]')}):
#    print('\n', '\n', h2.get_text())
    
# for child1 in bs.find_all('div', {'id':re.compile('cb[0-9]+')}):
#    print('\n', child1.get_text())
    
for h1 in bs.find_all('h3', {'id':'problematic-code'}):    
    #for child1 in bs.find_all('div', {'id':re.compile('cb1|cb1-[0-9]+')}):
    for child1 in bs.find_all('div', {'id':'cb1'}):
        print('\n', '\n', BACKGROUND_RED + WHITE + h1.get_text(), '\n' + RESET)
        print('#', child1.get_text(), '\n')
        
for h2 in bs.find_all('h3', {'id':'correct-code'}):    
    #for child2 in bs.find_all('div', {'id':re.compile('cb2|cb2-[0-9]+')}):
    for child2 in bs.find_all('div', {'id':re.compile('cb2|cb[3-9]')}):
        print('\n', '\n', BACKGROUND_GREEN + WHITE + h2.get_text(),'\n' + RESET)
        print('#', child2.get_text(), '\n')
        
#for h3 in bs.find_all('h3', {'id':'rationale'}):    
    #for child3 in bs.find_all('div', {'id':re.compile('cb4')}):
        #print('\n', '\n', h3.get_text(), '\n', child3.get_text())
        
#for h4 in bs.find_all('h3', {'id':'exceptions'}):    
    #for child4 in bs.find_all('div', {'id':re.compile('cb5')}):
        #print('\n', '\n', h4.get_text(), '\n', child4.get_text())
    
#for child2 in bs.find('div', {'id':'cb2'}).children:
#    print('\n', '\n', child2.get_text())
    
#for child3 in bs.find('div', {'id':'cb3'}).children:
#    print('\n', '\n', child3.get_text())
    
#for child4 in bs.find('div', {'id':'cb4'}).children:
#    print('\n', '\n', child4.get_text())

# https://parfeniukink.medium.com/reduce-the-amount-of-nested-loops-in-python-code-9f6b5949a895
# https://cursos.alura.com.br/forum/topico-web-scraping-funcao-get_text-147382
# https://stackoverflow.com/questions/58329827/how-to-use-findall-while-web-scraping
# https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-findall/
# https://www.freecodecamp.org/news/print-newline-in-python/
# https://realpython.com/python-formatted-output/
# https://sentry.io/answers/print-colored-text-to-terminal-with-python/
