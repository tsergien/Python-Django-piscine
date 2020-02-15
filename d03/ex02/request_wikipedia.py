#!/usr/bin/env python3

import sys
import requests
from dewiki import from_string
import json

def get_wiki_info_to_file(word_to_find):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": word_to_find,
        "format": "json", 
        "prop": "wikitext",
        "redirects": True
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    res = DATA["parse"]["wikitext"]["*"]

    f = open(word_to_find + '.wiki', 'w')
    f.write(from_string(res).replace('\n\n', '\n'))
    f.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Program requires at least one argument.')

    try:
        get_wiki_info_to_file(sys.argv[1])
    except:
        exit('Something went wrong.')
    

