from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

# Fetch ShellCheck Wiki
url = urlopen('https://www.shellcheck.net/wiki/')
bs = BeautifulSoup(url.read(), 'html.parser')

# Search function ShellCheck code number
def BinarySearch(lst, x):
    ini = 0
    end = len(lst) - 1
    flag = False
    while (ini <= end and not flag):
        mid = (ini + end) // 2
        if lst[mid] == x:
            flag = True
        elif x > lst[mid]:
            ini = mid +1
        else:
            end = mid-1
    if flag == True:
        urlSC = 'https://www.shellcheck.net/wiki/'
        fullUrl = urlSC + x
        webbrowser.open_new(fullUrl)
    else:
        print("\nKey is not found")

# List all the ShellCheck code number
link_href = [ x.get("href") for x in bs.select('a[href^="SC"]') ]

# User input ShellCheck code number
x = input('\nEnter with the code (SCXXXX): ')
BinarySearch(link_href, x)

# Search infinite loop
while True:
    ch = input("\nNew search? Press Y/y, if no, press ENTER: ")
    if ch == 'Y' or ch == 'y':
        x = input('\nEnter with the code (SCXXXX): ')
        BinarySearch(link_href, x)
    elif ch == "":
        print("\nBye!")
        break
    else:
        print("\nChoose the correct option")

