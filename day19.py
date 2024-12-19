#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import sys
import time
from functools import lru_cache as cache

f = open("ressources/day19.txt", "r") #Open File
lines = f.readlines() #Separate in lines

towels = tuple(lines[0].replace("\n", "").replace(",", "").split(" "))
desiredPatterns = []

for line in lines[2:]:
    desiredPatterns.append(line.replace("\n", ""))

@cache #Memorization of seen patterns ! Important for performance, otherwise will be incredibly slow
def isPossible(pattern, possibleTowels):
    if len(pattern) == 0: #If the pattern is empty, it is possible
        return 1
    #If start can be made, check if the rest is possible
    return np.sum(tuple([isPossible(pattern[len(towel):], possibleTowels) for towel in possibleTowels if pattern.startswith(towel)]))

possiblePatterns = 0
possibleWays = 0
for pattern in desiredPatterns:
    result = isPossible(pattern, towels)
    possiblePatterns += result > 0 #Possible patterns
    possibleWays += int(result) #Possible ways of each pattern

print("Number of possible patterns: {}".format(possiblePatterns))
print("Number of different ways: {}".format(possibleWays))