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
positions, velocities = np.array(positions), np.array(velocities)

#Q1
newPositions = (positions + velocities*100)%[mapWidth, mapHeight]
quadrant1 = np.sum(np.logical_and(newPositions[:,0] < mapWidth//2, newPositions[:,1] < mapHeight//2))
quadrant2 = np.sum(np.logical_and(newPositions[:,0] > mapWidth//2, newPositions[:,1] < mapHeight//2))
quadrant3 = np.sum(np.logical_and(newPositions[:,0] < mapWidth//2, newPositions[:,1] > mapHeight//2))
quadrant4 = np.sum(np.logical_and(newPositions[:,0] > mapWidth//2, newPositions[:,1] > mapHeight//2))
safety = quadrant1*quadrant2*quadrant3*quadrant4

print("Safety is: {}".format(safety))

#Q2
seconds = 100
while True:
    newPositions = np.unique((positions + velocities*seconds)%[mapWidth, mapHeight], axis=0)
    if newPositions.shape[0] == positions.shape[0]:
        break
    seconds += 1
    
print("Seconds to wait for christmas tree: {}".format(seconds))