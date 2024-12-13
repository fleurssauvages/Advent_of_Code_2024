#!/usr/bin/env python3
import numpy as np
import regex as re

f = open("ressources/day4.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
total = 0
lines = np.array([list(line.replace("\n", "")) for line in lines])

#Seach in lines
for line in lines:
    x = re.findall("XMAS|SAMX", ''.join(line), overlapped=True)
    total+=len(x)

#Search in columns
for column in lines.T:
    x = re.findall("XMAS|SAMX", ''.join(column), overlapped=True)
    total+=len(x)

#Seach in diagonals
for i in range(-lines.shape[0], lines.shape[0]):
    x = re.findall("XMAS|SAMX", ''.join(np.diag(lines,i)), overlapped=True)
    total+=len(x)
    #and reverse diag
    x = re.findall("XMAS|SAMX", ''.join(np.diag(np.fliplr(lines),i)), overlapped=True)
    total+=len(x)

print("Total XMAS is: {}".format(total))

#Q2
total = 0
for i in range(lines.shape[0]-2):
    for j in range(lines.shape[1]-2):
        submat = lines[i:i+3,j:j+3]
        x1 = re.findall("MAS|SAM", ''.join(np.diag(submat)))
        x2 = re.findall("MAS|SAM", ''.join(np.diag(np.fliplr(submat))))
        if x1 and x2:
            total += 1

print("Total XMAS is: {}".format(total))