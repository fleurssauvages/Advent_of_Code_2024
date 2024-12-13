#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day6.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
area = np.array([list(line.replace("\n", "")) for line in lines])

start = np.where(area == "^")
start = (start[0][0], start[1][0])
firstStart = (start[0], start[1])
direction = (-1, 0)
area[start[0], start[1]] = "."

seenSquares = set()
seenSquares.add(start)

seenPositions = set() #Added for Q2

while True:
    checkedSquare = (start[0]+direction[0], start[1]+direction[1])
    if checkedSquare[0] < 0 or checkedSquare[1] < 0 or checkedSquare[0] >= area.shape[0] or checkedSquare[1] >= area.shape[1]:
        break
    if area[checkedSquare[0], checkedSquare[1]] == ".":
        start = checkedSquare
        if start not in seenSquares: #Take only first occurence for Q2
            seenPositions.add((start, direction))
        seenSquares.add(start)
    elif area[checkedSquare[0], checkedSquare[1]] == "#":
        direction = (direction[1], -direction[0])

print("Total of visited square is: {}".format(len(seenSquares)))

#Q2
workingObstructions = set()
seenSquares.remove(firstStart)

for block, direction in seenPositions:
    i,j = block[0], block[1]
    area[i,j] = "#"
    
    start = (i-direction[0], j-direction[1])
    direction = (direction[1], -direction[0])
    
    seenNewPositions = set()
    seenNewPositions.add(str([start, direction]))

    while True:
        checkedSquare = (start[0]+direction[0], start[1]+direction[1])
        if checkedSquare[0] < 0 or checkedSquare[1] < 0 or checkedSquare[0] >= area.shape[0] or checkedSquare[1] >= area.shape[1]:
            break
        if area[checkedSquare[0], checkedSquare[1]] == ".":
            start = checkedSquare
        elif area[checkedSquare[0], checkedSquare[1]] == "#":
            direction = (direction[1], -direction[0])
        
        if str([start, direction]) in seenNewPositions:
            workingObstructions.add((i,j))
            break
        else:
            seenNewPositions.add(str([start, direction]))
                
    area[i,j] = "."

print("Total of working obstructions is: {}".format(len(workingObstructions)))