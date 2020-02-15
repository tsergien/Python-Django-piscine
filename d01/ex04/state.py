#!/usr/bin/env python3

import sys

def get_state(capital: str):
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
    if capital in capital_cities.values():
        for k in capital_cities.keys():
            if capital_cities[k] == capital:
                abbr = k
        if abbr in states.values():
            for k in states.keys():
                if states[k] == abbr:
                    return k
    return "Unknown capital city"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        pass
    else:
        capital = sys.argv[1]
        print(get_state(capital))
