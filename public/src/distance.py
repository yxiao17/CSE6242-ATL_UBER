#!/usr/bin/python
from math import radians, cos, sin, asin, sqrt
import csv
import sys
pos1= sys.argv[1]
pos2 = sys.argv[2]
# def haversine(pos1, pos2):
#     """
#     Calculate the great circle distance between two points
#     on the earth (specified in decimal degrees)
#     """
pos1 = int(pos1)
pos2 = int(pos2)


full = []

with open('./public/data/area.csv') as file:
    line = csv.reader(file)
    for l in line:
        full.append(l)



lon1, lat1, lon2, lat2 = map(radians, [float(full[pos1][0]), float(full[pos1][1]), float(full[pos2][0]), float(full[pos2][1])])

# haversine
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
c = 2 * asin(sqrt(a))
r = 6371  # R_earth
out = c*r*1000
print(out)
sys.stdout.flush()
#     print(c*r*1000)
#
#     return c * r * 1000
# haversine(pos1, pos2)
file.close()