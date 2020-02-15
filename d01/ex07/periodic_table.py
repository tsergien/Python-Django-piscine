#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    f = open('periodic_table.txt')
    lines = f.read().splitlines()
    elements = {}

    for line in lines:
        ind = line.find(' ')
        name = line[:ind]
        ind = ind + 3
        line = line[ind:]
        chars = line.split(',')

        position = int(chars[0][chars[0].find(':')+1:])
        number = int(chars[1][chars[1].find(':')+1:])
        small = chars[2][chars[2].find(':')+1:].strip(' ')
        molar = chars[3][chars[3].find(':')+1:]
        electrons = chars[4][chars[4].find(':')+1:]
        electron = electrons.split(' ')
        # print(f'name = {name}, position: {position}, number: {number}, small: {small}, molar: {molar}, electron: {electron}')
        elements[number] = [name, position, small, molar, electron]


    f = open('periodic_table.html','w')

    message = """<!DOCTYPE html>
                <html  lang="en">
                <head>
                <title> Periodic table</title>
                <meta charset="utf-8">
                <style>
                ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                }
                </style>
                </head>
                <body  style="background-color:#E4E4E4;">
                <h1>Mendeleev\'s table</h1>"""
    f.write(message)

    headers_groups = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7:'VII', 8: 'VIII', 9: 'IX',\
        10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV', 16: 'XVI', 17: 'XVII'}

    f.write('<table>')
    number = 1
    for i in range(7):
        f.write('<tr>')
        j = 0
        while j < 18:
            if number in elements.keys() and j != elements[number][1]:
                while j != elements[number][1] and j < 18:
                    f.write('<td>')
                    f.write('</td>')
                    j = j + 1
            
            if number not in elements.keys():
                number = number + 1
                continue
            # print(f'{elements[number][0]}:number = {number}, j = {j}, position = {elements[number][1]}')

            f.write('<td style="border: 1px solid #FFFFFF">')
            f.write(f'<h4>{elements[number][0]}</h4>')
            f.write('<ul>')
            f.write(f'<li><h2>{elements[number][2]}</h2></li>')
            f.write(f'<li>{number}</li>')
            f.write(f'<li>{elements[number][3]}</li>')
            f.write(f'<li>')
            for e in elements[number][4]:
                f.write(f'{e} ')
            f.write(f'</li>')
            f.write('</ul>')
            f.write("</td>")
            number = number + 1
            j = j + 1
        f.write("</tr>")

    f.write("</table></body></html>")
    f.close()