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
    return ''


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
    return ''


if __name__ == '__main__':
    if len(sys.argv) != 2:
        pass
    else:
        line = sys.argv[1]
        names = line.split(',')
        for name in names:
            if name.strip(' ') == '':
                continue
            edited_name = name.lower().strip(' ').title()
            capital = get_capital(edited_name)
            if capital != '':
                print(f'{capital} is the capital of {edited_name}')
                continue
            state = get_state(edited_name)
            if state != '':
                print(f'{edited_name} is the capital of {state}')
                continue
            print(f'{name.strip(" ")} is neither a capital city nor a state')
        
        
