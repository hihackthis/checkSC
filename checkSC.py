#!/usr/bin/env python3

# This program does a search by SC code number 
# on ShellCheck Wiki Page.
#
# by Diego Moicano (@hihackthis)
# July 02st, 2024
# version 1.0
#
# Run:
# python checkSC.py
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser

# Fetch ShellCheck Wiki
url = urlopen('https://www.shellcheck.net/wiki/')
bs = BeautifulSoup(url.read(), 'html.parser')

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
        urlSC = 'https://www.shellcheck.net/wiki/'
        fullUrl = urlSC + x
        webbrowser.open_new(fullUrl)
    else:
        print("\nCode number is not found")

# Puts all ShellCheck (SC) code numbers in a list
link_href = [ x.get("href") for x in bs.select('a[href^="SC"]') ]

# User input ShellCheck code number
x = input('\nEnter with the code (SCXXXX): ')
BinaryShell(link_href, x)

# Search with infinite loop
while True:
    ch = input("\nNew search? Press Y/y, if no, press ENTER: ")
    if ch == 'Y' or ch == 'y':
        x = input('\nEnter with the code (SCXXXX): ')
        BinaryShell(link_href, x)
    elif ch == "":
        print("\nBye!")
        break
    else:
        print("\nChoose the correct option")

