#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from scipy.spatial.distance import pdist, squareform
from functools import lru_cache as cache
import time

f = open("ressources/day21.txt", "r") #Open File
lines = f.readlines() #Separate in lines

codes = []
for line in lines:
    codes.append(line.replace("\n", ""))
    
numericalKeyPad = {"7": (0, 0), "8": (0, 1), "9": (0, 2), "4": (1, 0), "5": (1, 1), "6": (1, 2), "1": (2, 0), "2": (2, 1), "3": (2, 2), " ": (3, 0), "0": (3, 1), "A": (3, 2)}
directionalKeyPad = {" ": (0, 0), "^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

@cache
def findPath(start, end, keyPad):
    keyPad = numericalKeyPad if keyPad == 0 else directionalKeyPad
    gapPos = keyPad[" "]
    startPos = keyPad[start]
    endPos = keyPad[end]
    x = endPos[0]-startPos[0]
    y = endPos[1]-startPos[1]
    if startPos[0] == gapPos[0] and endPos[1] == gapPos[1]: #If gap is in the same row as start and same column as end, first vertical then horizontal
        return (x>0)*abs(x)*"v"+(x<0)*abs(x)*"^"+(y<0)*abs(y)*"<"+(y>0)*abs(y)*">"+"A"
    elif startPos[1] == gapPos[1] and endPos[0] == gapPos[0]: #If gap is in the same column as start and same row as end, first horizontal then vertical
        return (y<0)*abs(y)*"<"+(y>0)*abs(y)*">"+(x>0)*abs(x)*"v"+(x<0)*abs(x)*"^"+"A"
    else: #Optimap path
        #Moving left then down or up is better than the opposite, because up and down are closer to A than left
        #Moving down then right is better than the opposite, because right is closer to A
        #Moving up then right or right then up is the same
        return (y<0)*abs(y)*"<"+(x>0)*abs(x)*"v"+(x<0)*abs(x)*"^"+(y>0)*abs(y)*">"+"A"

def findFirstSequence(code, keyPad):
    start = "A"
    sequence = defaultdict(int)
    for letter in code:
        path = findPath(start, letter, keyPad)
        sequence[path] += 1
        start = letter
    return sequence

def findSequence(codeSequence, keyPad):
    sequence = defaultdict(int)
    for subsequence in codeSequence:
        nb = codeSequence[subsequence]
        start = "A"
        for letter in subsequence:
            path = findPath(start, letter, keyPad)
            sequence[path] += nb
            start = letter
    return sequence

# start_time = time.time()
total = 0
intermediaries = 1
for code in codes:
    robot = findFirstSequence(code, 0)
    for _ in range(intermediaries):
        robot = findSequence(robot, 1)
    user = findSequence(robot, 1)
    codeValue = int(re.findall(r'\d+', code)[0])
    total += codeValue*np.sum([len(sequence)*user[sequence] for sequence in user])  
# print(time.time()-start_time)
print("The code value with 2 robots is: {}".format(total))

# start_time = time.time()
total = 0
intermediaries = 24
for code in codes:
    robot = findFirstSequence(code, 0)
    for _ in range(intermediaries):
        robot = findSequence(robot, 1)
    user = findSequence(robot, 1)
    codeValue = int(re.findall(r'\d+', code)[0])
    total += codeValue*np.sum([len(sequence)*user[sequence] for sequence in user])  
# print(time.time()-start_time)
print("The code value with 25 robots is: {}".format(total))