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

# Font colors
WHITE = '\033[97m'
BACKGROUND_RED = '\033[41m'
RESET = '\033[0m'

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
        print('\n', BACKGROUND_RED + WHITE + 'Code number is not found' + RESET)
        
# Fetch ShellCheck Wiki
url = urlopen('https://gist.github.com/nicerobot/53cee11ee0abbdc997661e65b348f375')
bs = BeautifulSoup(url.read(), 'html.parser')

# Puts all ShellCheck (SC) code numbers in a list
patt = re.compile(r'SC[0-9]{4}')
link_href = [ x.get('href') for x in bs.select('div#file-_shellcheck-md-readme ul li a[href*="SC"]') ]
all_codesc = patt.findall(str(link_href)) 

# User input ShellCheck code number
x = input('\nEnter with the code (SCXXXX): ').upper()
BinaryShell(all_codesc, x)

# Search with infinite loop
while True:
    ch = input('\nNew search? Press Y/y, if no, press ENTER: ').upper()
    if ch == 'Y':
        x = input('\nEnter with the code (SCXXXX): ').upper()
        BinaryShell(all_codesc, x)
    elif ch == "":
        print('\nBye!')
        break
    else:
        print('\nChoose the correct option')

