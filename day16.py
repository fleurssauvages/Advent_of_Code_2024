#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import sys
import time
from heapq import heapify, heappop, heappush

f = open("ressources/day16.txt", "r") #Open File
lines = f.readlines() #Separate in lines

area = np.array([list(line.replace("\n", "")) for line in lines])
sys.setrecursionlimit(area.shape[0]*area.shape[1])
start = np.where(area == "S")
start = (start[0][0], start[1][0])
end = np.where(area == "E")
end = (end[0][0], end[1][0])
startDirection = (0, 1)

#Q1
start_time = time.time()
scoreMap = np.ones(area.shape)*area.shape[0]*1000
scoreMap[start] = 0

def updateScore(start, startDirection, scoreMap, area):
    queue = [(0, start, startDirection)]
    heapify(queue)
    while queue:
        score, currentPosition, currentDirection = heappop(queue)
        #Front
        front = (currentPosition[0] + currentDirection[0], currentPosition[1] + currentDirection[1])
        if area[front] != "#":
            if scoreMap[front] >= score+1:
                scoreMap[front] = score+1
                heappush(queue, (score+1, front, currentDirection))
        #Left
        left = (currentPosition[0] + currentDirection[1], currentPosition[1] - currentDirection[0])
        if area[left] != "#":
            if scoreMap[left] >= score+1001:
                scoreMap[left] = score+1001
                heappush(queue, (score+1001, left, (currentDirection[1], -currentDirection[0])))
        #Right
        right = (currentPosition[0] - currentDirection[1], currentPosition[1] + currentDirection[0])
        if area[right] != "#":
            if scoreMap[right] >= score+1001:
                scoreMap[right] = score+1001
                heappush(queue, (score+1001, right, (-currentDirection[1], currentDirection[0])))
                
updateScore(start, startDirection, scoreMap, area)
score = scoreMap[end]
print("--- %s seconds ---" % (time.time() - start_time))
print("Best Reindeer Score is: {}".format(int(score)))

#Q2
def reversePath(currentPosition, currentDirection, score, path, area, scoreMap):
    #Start from the end and tries to reach the start given the best score, exploring all paths
    path.add(currentPosition)
    if currentPosition == start: #Yeah ! We found the start with the correct score
        return path
    elif score < scoreMap[currentPosition]: #It means the start cannot be reached with the current score, give up this path
        return set()
    
    bestVisited = set()
    #Front
    front = (currentPosition[0] + currentDirection[0], currentPosition[1] + currentDirection[1])
    if area[front] != "#":
        bestVisited = bestVisited|reversePath(front, currentDirection, score-1, path.copy(), area, scoreMap)
    #Left
    left = (currentPosition[0] + currentDirection[1], currentPosition[1] - currentDirection[0])
    if area[left] != "#":
        bestVisited = bestVisited|reversePath(left, (currentDirection[1], -currentDirection[0]), score-1001, path.copy(), area, scoreMap)
    #Right
    right = (currentPosition[0] - currentDirection[1], currentPosition[1] + currentDirection[0])
    if area[right] != "#":
        bestVisited = bestVisited|reversePath(right, (-currentDirection[1], currentDirection[0]), score-1001, path.copy(), area, scoreMap)
    return bestVisited

start_time = time.time()
seatsWest = reversePath(end, (0, -1), score, set(), area, scoreMap)
seatsSouth = reversePath(end, (1, 0), score, set(), area, scoreMap)
seats = seatsWest|seatsSouth
print("--- %s seconds ---" % (time.time() - start_time))
print("Nb of seats is: {}".format(len(seats)))