#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day12.txt", "r") #Open File
lines = f.readlines() #Separate in lines
garden = np.array([list(line.replace("\n", "")) for line in lines])
plants = np.unique(garden)

def fill(currentPosition, positions, group):
    x, y = currentPosition[0], currentPosition[1]
    group.append([x,y])
    neighbors = [[x-1,y],[x+1,y], [x,y-1],[x,y+1]]
    for n in neighbors:
        if n in positions:
            positions.remove(n)
            fill(n,positions,group)
    return group

def getPerimeter(group):
    perimeter = 0
    for g in group:
        x,y = g[0], g[1]
        neighbors = [[x-1,y],[x+1,y], [x,y-1],[x,y+1]]
        perimeter += 4
        for n in neighbors:
            if n in group:
                perimeter-=1
    return perimeter

def getSides(group): #Nb Sides = Nb of Corners
    sides = 0
    for g in group:
        x,y = g[0], g[1]
        sides += [x-1, y] not in group and [x, y-1] not in group #Top left corner
        sides += [x+1, y] not in group and [x, y-1] not in group #Top right corner
        sides += [x-1, y] not in group and [x, y+1] not in group #Bottom left corner
        sides += [x+1, y] not in group and [x, y+1] not in group #Bottom right corner
        sides += [x-1, y] in group and [x, y-1] in group and [x-1, y-1] not in group #Top left corner inside
        sides += [x+1, y] in group and [x, y-1] in group and [x+1, y-1] not in group #Top right corner inside
        sides += [x-1, y] in group and [x, y+1] in group and [x-1, y+1] not in group #Bottom left corner inside
        sides += [x+1, y] in group and [x, y+1] in group and [x+1, y+1] not in group #Bottom right corner inside
    return sides

#Q1 and 2
total = 0
total2 = 0
for plant in plants:
    positions = np.transpose(np.where(garden == plant)).tolist()
    while len(positions) > 0:
        start = positions.pop(0)
        group = fill(start, positions, [])

        area = len(group)
        perimeter = getPerimeter(group)
        sides = getSides(group)
        
        total+= area*perimeter
        total2 += area*sides

# print(len(areas), len(perimeters))
print("Total price for fences is: {}".format(total))
print("Total price for fences with discount is: {}".format(total2))