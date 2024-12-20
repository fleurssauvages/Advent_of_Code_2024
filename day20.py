#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from scipy.spatial.distance import pdist, squareform

f = open("ressources/day20.txt", "r") #Open File
lines = f.readlines() #Separate in lines

area = np.array([list(line.replace("\n", "")) for line in lines])
start = np.where(area == "S")
start = (start[0][0], start[1][0])
end = np.where(area == "E")
end = (end[0][0], end[1][0])

def updateScore(start, end, area):
    scoreMap = np.ones(area.shape)*area.shape[0]*1000
    scoreMap[start] = 0
    queue = [(0, start, [start])]
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heapify(queue)
    while queue:
        score, currentPosition, path = heappop(queue)
        for n in neighbors:
            newPosition = (currentPosition[0]+n[0], currentPosition[1]+n[1])
            if area[newPosition] != "#":
                if scoreMap[newPosition] >= score+1:
                    path.append(newPosition)
                    scoreMap[newPosition] = score+1
                    heappush(queue, (score+1, newPosition, path))
                    if newPosition == end:
                        return scoreMap, path

scoreMapFromStart, path = updateScore(start, end, area) #Classic Dijkstra to know the best path
scoreMapFromEnd, _ = updateScore(end, start, area) #We also store the reverse path, useful for the cheats
scoreWithoutCheats = scoreMapFromStart[end] #Length of the shcortest path without cheats

#Q1
cheats = []
for tile in path:
    tile = tuple(tile)
    for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newTile = (tile[0]+2*n[0], tile[1]+2*n[1]) #We check the tile 2 steps away
        if newTile[0] > 0 and newTile[0] < area.shape[0] and newTile[1] > 0 and newTile[1] < area.shape[1]:
            if area[newTile] != "#": #If the tile is not a wall and is in the grid
                scoreWithCheats = scoreMapFromStart[tile] + 2 + scoreMapFromEnd[newTile] #The score with the cheat is score from start, +2, +remaining score to end
                if scoreWithCheats < scoreWithoutCheats: #If it saves time
                    cheats.append(scoreWithoutCheats-scoreWithCheats) #We store the time saved by the cheat

cheats = sorted(Counter(cheats).items(),key = lambda i: i[0])
bestCheats = np.sum([cheat[1] for cheat in cheats if cheat[0] >= 100]) #Only keep the best cheats
# print("Cheats are: {}".format(cheats))
print("Nb of Good Cheats is: {}".format(bestCheats))

#Q2
cheats = []
manhattanDistances = squareform(pdist(np.array(path), metric='cityblock')) #We compute the manhattan distances between all the tiles in the path
for i, startTile in enumerate(path):
    mask = manhattanDistances[i, i+1:] <= 20 #We only keep the tiles that are at most 20 steps away, the max length of a cheat
    newTiles = np.array(path[i+1:])[mask] 
    for endTile in newTiles: 
        startTile, endTile = tuple(startTile), tuple(endTile)
        distance = np.abs(startTile[0]-endTile[0])+np.abs(startTile[1]-endTile[1])
        scoreWithCheats = scoreMapFromStart[startTile] + distance + scoreMapFromEnd[endTile] #The score with the cheat is score from start, +distance, +remaining score to end
        if scoreWithCheats < scoreWithoutCheats: #If it saves time
            cheats.append(scoreWithoutCheats-scoreWithCheats) #We store the time saved by the cheat
                
cheats = sorted(Counter(cheats).items(),key = lambda i: i[0])
bestCheats = np.sum([cheat[1] for cheat in cheats if cheat[0] >= 100])
# print("Cheats are: {}".format(cheats))
print("Nb of Good Cheats is: {}".format(bestCheats))