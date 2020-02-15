#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys

if __name__ == '__main__':
    for arg in sys.argv:
        r = requests.get('https://en.wikipedia.org/wiki/' + sys.argv[1])
        # print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.prettify())
    

