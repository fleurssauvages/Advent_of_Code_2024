#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day14.txt", "r") #Open File
lines = f.readlines() #Separate in lines

mapWidth = 101
mapHeight = 103
positions = []
velocities = []

for line in lines:
    x = re.findall("-?[0-9]+", line)
    positions.append([int(x[0]), int(x[1])])
    velocities.append([int(x[2]), int(x[3])])
    
#Q1
newPositions = []
for i, data in enumerate(zip(positions, velocities)):
    p, v = data
    newPositions.append([(p[0]+v[0]*100)%mapWidth, (p[1]+v[1]*100)%mapHeight])

quadrant1 = np.sum([1 if p[0] < mapWidth//2 and p[1] < mapHeight//2 else 0 for p in newPositions])
quadrant2 = np.sum([1 if p[0] > mapWidth//2 and p[1] < mapHeight//2 else 0 for p in newPositions])
quadrant3 = np.sum([1 if p[0] < mapWidth//2 and p[1] > mapHeight//2 else 0 for p in newPositions])
quadrant4 = np.sum([1 if p[0] > mapWidth//2 and p[1] > mapHeight//2 else 0 for p in newPositions])
safety = quadrant1*quadrant2*quadrant3*quadrant4

print("Safety is: {}".format(safety))

#Q2
seconds = 100
while True:
    newPositions = set()
    for i, data in enumerate(zip(positions, velocities)):
        p, v = data
        newPositions.add(((p[0]+v[0]*seconds)%mapWidth, (p[1]+v[1]*seconds)%mapHeight))
    if len(newPositions) == len(positions):
        break
    seconds += 1
    
print("Seconds to wait for christmas tree: {}".format(seconds))