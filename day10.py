#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import time 

f = open("ressources/day10.txt", "r") #Open File
lines = f.readlines() #Separate in lines
area = np.array([list(line.replace("\n", "")) for line in lines])
zeros = np.transpose(np.where(area == "0"))

#Q1
def findPaths(area, position, number, seens):
    if number == 9:
        if position in seens:
            return 0
        else:
            seens.add(position)
            return 1
    nbTrails = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for d in directions:
        newPosition = (position[0]+d[0], position[1]+d[1])
        if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= area.shape[0] or newPosition[1] >= area.shape[1]:
            continue
        if area[newPosition[0], newPosition[1]] == str(number+1):
            nbTrails+=findPaths(area, newPosition, number+1, seens)
    return nbTrails

total = 0
for zero in zeros:
    total+=findPaths(area, zero, 0, set())
print("Total nb of trails is: {}".format(total))

#Q2
def findDistinctsPaths(area, position, number):
    if number == 9:
        return 1
    nbTrails = 0
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    for d in directions:
        newPosition = (position[0]+d[0], position[1]+d[1])
        if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= area.shape[0] or newPosition[1] >= area.shape[1]:
            continue
        if area[newPosition[0], newPosition[1]] == str(number+1):
            nbTrails+=findDistinctsPaths(area, newPosition, number+1)
    return nbTrails

total = 0
for zero in zeros:
    total+=findDistinctsPaths(area, zero, 0)
print("Total nb of distinct trails is: {}".format(total))