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
        urlSC = 'https://www.shellcheck.net/wiki/'
        fullUrl = urlSC + x
        #print(fullUrl)
        webbrowser.open_new(fullUrl)
    else:
        print("\nKey is not found")

#codes = bs.find_all('a', href=True)
#code = bs.select('a[href^="SC"]')
#print(code)

link_href = [ x.get("href") for x in bs.select('a[href^="SC"]') ]
#print(link_href)

x = input('\nEnter with the code (SCXXXX): ')
BinarySearch(link_href, x)

while True:   
    ch = input("\nNew research? Press Y, if no, press ENTER: ")    
    if ch == 'Y':
        x = input('\nEnter with the code (SCXXXX): ')
        BinarySearch(link_href, x)
    elif ch == "":
        print("\nBye!")
        break
    else:
        print("\nChoose the correct option")

