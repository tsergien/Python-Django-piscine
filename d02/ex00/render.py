#!/usr/bin/env python3

import sys
import os
import re
from settings import name, surname, age, prof

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Program accepts one only parameter.")
    if sys.argv[1][sys.argv[1].find('.')+1:] != "template" or\
        len(sys.argv[1][:sys.argv[1].find('.')]) < 1:
        exit("Program accepts only [.template] extensions.")
    try:
        template = open(sys.argv[1], "r+")
        settings = open("settings.py")
    except IOError:
        exit(f'Could not open file {sys.argv[1]}!')


    text = template.read()
    text = re.sub(r'\{name\}', name, text)
    text = re.sub(r'\{surname\}', surname, text)
    text = re.sub(r'\{age\}', age, text)
    text = re.sub(r'\{prof\}', prof, text)

    html = open('myCV.html','w')
    html.write(text)



    html.close()
