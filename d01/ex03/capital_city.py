#!/usr/bin/env python3

import sys

def get_capital(state: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    if state in states.keys():
        abbr = states[state]
        if abbr in capital_cities.keys():
            return capital_cities[abbr]
    return "Unknown state"
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        pass
    else:
        state = sys.argv[1]
        print(get_capital(state))
