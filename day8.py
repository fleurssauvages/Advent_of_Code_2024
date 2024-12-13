#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
from itertools import combinations

f = open("ressources/day8.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
antennas = defaultdict(list)
mapSize = (len(lines), len(lines[0].replace("\n", "")))

for i, line in enumerate(lines):
    x = re.finditer("[a-zA-Z]|[0-9]", line.replace("\n", ""))
    for antenna in x:
        antennas[antenna.group()].append((i, antenna.start()))

antinodes = set()
for key in antennas:
    antennasList = list(combinations(antennas[key], 2))
    for antenna1, antenna2 in antennasList:
        antinode1 = (antenna1[0]-(antenna2[0]-antenna1[0]), antenna1[1]-(antenna2[1]-antenna1[1]))
        antinode2 = (antenna2[0]-(antenna1[0]-antenna2[0]), antenna2[1]-(antenna1[1]-antenna2[1]))
        if antinode1[0] >= 0 and antinode1[0] < mapSize[0] and antinode1[1] >= 0 and antinode1[1] < mapSize[1]:
            antinodes.add(antinode1)
        if antinode2[0] >= 0 and antinode2[0] < mapSize[0] and antinode2[1] >= 0 and antinode2[1] < mapSize[1]:
            antinodes.add(antinode2)
        
print("Total of antinodes on the map is: {}".format(len(antinodes)))

#Q2
antinodes = set()
for key in antennas:
    antennasList = list(combinations(antennas[key], 2))
    for antenna1, antenna2 in antennasList:
        k = 0
        while True:
            antinode1 = (antenna1[0]-(antenna2[0]-antenna1[0])*k, antenna1[1]-(antenna2[1]-antenna1[1])*k)
            if antinode1[0] >= 0 and antinode1[0] < mapSize[0] and antinode1[1] >= 0 and antinode1[1] < mapSize[1]:
                antinodes.add(antinode1)
                k += 1
            else:
                break
        k = 0
        while True:
            antinode2 = (antenna2[0]-(antenna1[0]-antenna2[0])*k, antenna2[1]-(antenna1[1]-antenna2[1])*k)
            if antinode2[0] >= 0 and antinode2[0] < mapSize[0] and antinode2[1] >= 0 and antinode2[1] < mapSize[1]:
                antinodes.add(antinode2)
                k += 1
            else:
                break

print("Total of antinodes on the map with repetition is: {}".format(len(antinodes)))