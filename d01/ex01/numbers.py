#!/usr/bin/env python3

if __name__ == '__main__':
    f = open("numbers.txt", 'r')
    numbers = f.read().split(',')
    for n in numbers:
        print(f'{int(n)}')
