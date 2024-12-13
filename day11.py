#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import time 

f = open("ressources/day11.txt", "r") #Open File
lines = f.readlines() #Separate in lines
data = [int(x) for x in lines[0].replace("\n", "").split(" ")]

stones = defaultdict(int)
for stone in data:
    stones[stone] = 1

def updateStones(stones):
    newStones = defaultdict(int)
    for stone in stones:
        nbStones = stones[stone]
        stoneString = str(stone)
        if stone == 0:
            newStones[1] += nbStones
        elif len(stoneString) % 2 == 0:
            newStones[int(stoneString[:len(stoneString)//2])] += nbStones
            newStones[int(stoneString[len(stoneString)//2:])] += nbStones
        else:
            newStones[stone*2024] += nbStones
    return newStones
    
#Q1
nbBlinks = 25
for _ in range(nbBlinks):
    stones = updateStones(stones)
print("Nb of stones after 25 blinks : {}".format(np.sum(list(stones.values()))))

#Q2
nbBlinks = 50
for _ in range(nbBlinks):
    stones = updateStones(stones)
print("Nb of stones after 75 blinks : {}".format(np.sum(list(stones.values()))))