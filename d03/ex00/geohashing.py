#!/usr/bin/env python3

import sys
import antigravity

if __name__ == '__main__':
    if len(sys.argv) != 4:
        exit('Program needs exactly 3 arguments: 2 floats - latitude, longitude and datedow.\n')


    try:
        latitude = sys.argv[1]
        longitude = sys.argv[2]
        datedow = sys.argv[3]
        antigravity.geohash(float(latitude), float(longitude), datedow.encode('utf-8'))
    except:
        exit('Latitude and longitude must be floats, datedow: 2020-05-26-19045.77')

