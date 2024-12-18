#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import sys
import time
from heapq import heapify, heappop, heappush

f = open("ressources/day18.txt", "r") #Open File
lines = f.readlines() #Separate in lines

falls = list()
for line in lines:
    x = re.findall(r"\d+", line)
    falls.append((int(x[0]), int(x[1])))
    
width = 71
height = 71
start = (0,0)
end = (70,70)

#Q1
area = np.zeros((width, height))
for fall in falls[0:1024]:
    area[fall[0], fall[1]] = 1
sys.setrecursionlimit(area.shape[0]*area.shape[1])

scoreMap = np.ones(area.shape)*area.shape[0]*1000
scoreMap[start] = 0

def updateScore(start, scoreMap, area):
    queue = [(0, start)]
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heapify(queue)
    while queue:
        score, currentPosition = heappop(queue)
        for n in neighbours:
            neighbour = (currentPosition[0] + n[0], currentPosition[1] + n[1])
            if neighbour[0] < 0 or neighbour[0] >= area.shape[0] or neighbour[1] < 0 or neighbour[1] >= area.shape[1]:
                continue
            if area[neighbour] != 1:
                if scoreMap[neighbour] > score+1:
                    scoreMap[neighbour] = score+1
                    heappush(queue, (score+1, neighbour))
    return scoreMap

scoreMap = updateScore(start, scoreMap, area)
score = scoreMap[end]

print("Mimimum path to reach the end is: {}".format(int(score)))

#Q2
maxPixels = len(falls)
minPixels = 1024
iprev = 0
while True:
    i = (maxPixels + minPixels)//2
    area = np.zeros((width, height))
    for fall in falls[0:i]:
        area[fall[0], fall[1]] = 1
    scoreMap = np.ones(area.shape)*area.shape[0]*1000
    scoreMap[start] = 0
    scoreMap = updateScore(start, scoreMap, area)
    if scoreMap[end] == area.shape[0]*1000:
        maxPixels = i
    else:
        minPixels = i
    if maxPixels-minPixels == 1 and iprev == i:
        break
    iprev = i

print("First Falling pixel is: {}".format(falls[i]))