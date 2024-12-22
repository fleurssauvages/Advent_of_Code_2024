#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush
from scipy.spatial.distance import pdist, squareform
from functools import lru_cache as cache
import time

f = open("ressources/day22.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
secretNumbers = []
for line in lines:
    secretNumbers.append(int(line.replace("\n", "")))

@cache
def secretOperation(number):
    number = ((number*64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number*2048) ^ number) % 16777216
    return number
    
for _ in range(2000):
    secretNumbers = [secretOperation(number) for number in secretNumbers]
    
print("The sum of secret numbers is: {}".format(sum(secretNumbers)))

#Q2
secretNumbers = []
for line in lines:
    secretNumbers.append(int(line.replace("\n", "")))
    
def secretSequences(number, sequences):
    changes = [-10, -10, -10, -10]
    digit = int(str(number)[-1])
    seens = set()
    for _ in range(2000):
        number = ((number*64) ^ number) % 16777216
        number = ((number // 32) ^ number) % 16777216
        number = ((number*2048) ^ number) % 16777216
        
        changes = changes[1:]
        changes.append(int(str(number)[-1])-digit)
        digit = int(str(number)[-1])
        
        if tuple(changes) not in seens: #If the sequence has not been seen yet: first occurence
            seens.add(tuple(changes)) #We add the sequence to the seen sequences
            sequences[tuple(changes)]+=digit #We add the digit to the total of that given sequence
    return sequences

sequences = defaultdict(int) #For each sequence, we store its total in a dictionary: key = sequence, value = total
for number in secretNumbers:
    sequences = secretSequences(number, sequences)
    
print("The best total is: {}".format(np.max(list(sequences.values()))))