#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day15.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1, Reading Data
for i, line in enumerate(lines):
    line = line.replace("\n", "")
    if len(line) == 0:
        break
    
area = np.array([list(line.replace("\n", "")) for line in lines[:i]])

instructions = []
for line in lines[i+1:]:
    instructions += list(line.replace("\n", ""))
    
directions = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}

robot = tuple(np.array(np.where(area == '@')).T.tolist()[0])
walls = np.array(np.where(area == '#')).T.tolist()
walls = set([(x[0], x[1]) for x in walls])
stones = np.array(np.where(area == 'O')).T.tolist()
stones = set([(x[0], x[1]) for x in stones])

#Q1
for instruction in instructions:
    direction = directions[instruction]
    newPosition = (robot[0]+direction[0], robot[1]+direction[1])
    stonesToMove = []
    while True:
        if newPosition in walls:
            break #There is a wall, don't move
        elif newPosition in stones:
            stonesToMove.append(newPosition) #There is a stone, which we might move
            newPosition = (newPosition[0]+direction[0], newPosition[1]+direction[1]) #Check next position
        else: #There is nothing, move
            robot = (robot[0]+direction[0], robot[1]+direction[1]) #Move robot
            for stone in stonesToMove:
                stones.remove(stone) #Remove stone from old position
            for stone in stonesToMove:
                stones.add((stone[0]+direction[0], stone[1]+direction[1])) #Add stone to new position
            break

distanceScore = np.sum([stone[0]*100+stone[1] for stone in stones])
print("Distance Score is: {}".format(distanceScore))

#Q2 Reading Data
area = np.array([list(line.replace("\n", "").replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")) for line in lines[:i]])
robot = tuple(np.array(np.where(area == '@')).T.tolist()[0])
walls = np.array(np.where(area == '#')).T.tolist()
walls = set([(x[0], x[1]) for x in walls])
stonesLeft = np.array(np.where(area == '[')).T.tolist()
stonesRight = np.array(np.where(area == ']')).T.tolist()
stonesLeft = set([(x[0], x[1]) for x in stonesLeft])
stonesRight = set([(x[0], x[1]) for x in stonesRight])

#Q2
for instruction in instructions:
    direction = directions[instruction]
    newPosition = (robot[0]+direction[0], robot[1]+direction[1])
    stonesToMoveRight = []
    stonesToMoveLeft = []

    positionsToCheck = set()
    positionsToCheck.add(newPosition)
    while True:
        newPositionsToCheck = set()
        if np.any([position in walls for position in positionsToCheck]):
            break #Don't move, there is a wall
        elif np.any([position in stonesRight|stonesLeft for position in positionsToCheck]): #There is a stone part
            for position in positionsToCheck:
                if position in stonesRight and position not in stonesToMoveRight: #There is a right part of a stone which we might move (and haven't checked yet)
                    stonesToMoveRight.append(position) #There is a right part of a stone which we might move
                    stonesToMoveLeft.append((position[0], position[1]-1)) #We add the associated left stone part
                    newPositionsToCheck.add((position[0]+direction[0], position[1]+direction[1])) #Check next position in front of right stone part
                    newPositionsToCheck.add((position[0]+direction[0], position[1]-1+direction[1])) #Check next position in front of left stone part
                elif position in stonesLeft and position not in stonesToMoveLeft: #There is a left part of a stone which we might move (and haven't checked yet)
                    stonesToMoveLeft.append(position) #There is a left part of a stone which we might move
                    stonesToMoveRight.append((position[0], position[1]+1)) #We add the associated right stone part
                    newPositionsToCheck.add((position[0]+direction[0], position[1]+direction[1])) #Check next position in front of left stone part
                    newPositionsToCheck.add((position[0]+direction[0], position[1]+1+direction[1])) #Check next position in front of right stone part                    
        else: #Move, there is nothing
            robot = (robot[0]+direction[0], robot[1]+direction[1]) #Move robot
            for stone in stonesToMoveRight:
                stonesRight.remove(stone) #Remove right stone part from old position
            for stone in stonesToMoveRight:
                stonesRight.add((stone[0]+direction[0], stone[1]+direction[1])) #Add right stone part to new position
            for stone in stonesToMoveLeft:
                stonesLeft.remove(stone) #Remove left stone part from old position
            for stone in stonesToMoveLeft:
                stonesLeft.add((stone[0]+direction[0], stone[1]+direction[1])) #Add left stone part to new position
            break
        positionsToCheck = newPositionsToCheck

distanceScore = np.sum([stone[0]*100+stone[1] for stone in stonesLeft])
print("Distance Score is: {}".format(distanceScore))