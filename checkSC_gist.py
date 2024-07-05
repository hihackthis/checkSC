#!/usr/bin/env python3

# This program does a search by SC code number 
# on ShellCheck Wiki Page on GitHub.
#
# by Diego Moicano (@hihackthis)
# July 04th, 2024
# version 1.0
#
# Run:
# python checkSC.py
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import re

# Binary search function ShellCheck code number
def BinaryShell(lst, x):
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
        urlSC = 'https://github.com/koalaman/shellcheck/wiki/'
        fullUrl = urlSC + x
        webbrowser.open_new(fullUrl)
    else:
        print("\nCode number is not found")
        
# Fetch ShellCheck Wiki
url = urlopen('https://gist.github.com/nicerobot/53cee11ee0abbdc997661e65b348f375')
bs = BeautifulSoup(url.read(), 'html.parser')

patt = re.compile(r'SC[0-9]{4}')
link_href = [ x.get("href") for x in bs.select('a[href*="SC"]') ]
all_codesc = patt.findall(str(link_href)) 
# print(codesc)

# User input ShellCheck code number
x = input('\nEnter with the code (SCXXXX): ')
BinaryShell(all_codesc, x)

# Search with infinite loop
while True:
    ch = input("\nNew search? Press Y/y, if no, press ENTER: ")
    if ch == 'Y' or ch == 'y':
        x = input('\nEnter with the code (SCXXXX): ')
        BinaryShell(all_codesc, x)
    elif ch == "":
        print("\nBye!")
        break
    else:
        print("\nChoose the correct option")

