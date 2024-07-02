from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import re

# providing url 
url = urlopen('https://www.shellcheck.net/wiki/')
bs = BeautifulSoup(url.read(), 'html.parser')

def BinarySearch(lst, x):
    ini = 0
    fim = len(lst) - 1
    flag = False
    while (ini <= fim and not flag):
        mid = (ini + fim) // 2
        if lst[mid] == x:
            flag = True
        elif x > lst[mid]:
            ini = mid +1
        else:
            fim = mid-1
    if flag == True:
        #print("Key is found", x)
        urlSC = 'https://github.com/koalaman/shellcheck/wiki/'
        fullUrl = urlSC + x
        webbrowser.open(fullUrl)
        #urlSCn = urlopen(fullUrl).read().decode('utf-8')
        #print(urlSCn)
        
    else:
        print("key is not found")

codes = bs.find_all('a', href=True)
code = bs.select('a[href^="SC"]')
#print(code)

link_href = [ x.get("href") for x in bs.select('a[href^="SC"]') ]
#print(link_href)
# print(link_href[53])

x = input('\nEnter de code (SCXXXX): ')
#print("the element needed to search, x =", x)
BinarySearch(link_href, x)



#scCode = int(input('Enter de code: '))
#codigo = f'SC{scCode}'
#print(codigo)
#for cod in codes:
    #a = cod.get_text()
    #b = re.search(codigo, a)
    #print(cod.get_text(), end=', ')
# rows = [x for x in bs.select('a[href]')]
#j = codes.get_text(separator=' ', strip=True)
    #b = j.replace('\n', ', ')
#print(j)
    #a = cod.get_text()
    #b = a.replace('\n', ', ')
    #print(a, end=',')
    #print(b)
    
# https://medium.com/@spaw.co/beautifulsoup-find-all-421385b341d4
# https://www.w3schools.com/python/python_regex.asp
# https://scrapeops.io/python-web-scraping-playbook/python-beautifulsoup-find/
# https://helpful.knobs-dials.com/index.php/BeautifulSoup
# https://www.alec.fyi/mastering-beautifulsoup
# https://www.digitalocean.com/community/tutorials/python-convert-string-to-list
# https://www.geeksforgeeks.org/python-program-convert-string-list/
# https://www.educative.io/answers/how-to-search-in-python
# https://www.freecodecamp.org/portuguese/news/pesquisa-binaria-em-python-como-escrever-o-algoritmo-de-pesquisa-binaria-e-exemplos/
# https://didatica.tech/tudo-sobre-listas-em-python/
# https://docs.python.org/pt-br/3/tutorial/inputoutput.html
# https://docs.python.org/3/howto/urllib2.html

# https://github.com/m14r41/PentestingEverything

