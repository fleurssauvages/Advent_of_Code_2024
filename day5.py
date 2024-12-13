#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day5.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Read Data
rules = defaultdict(set)
prints = []
for line in lines:
    line = line.replace("\n","")
    if "|" in line:
        numbers = line.split("|")
        rules[int(numbers[0])].add(int(numbers[1]))
    if "," in line:
        prints.append([int(x) for x in line.split(",")])

#Q1
def checkIfCorrect(printing, rules):
    printing = printing.copy()
    doAdd = True
    while len(printing) > 0:
        elem = printing.pop(0)
        if any([elem in rules[element] for element in printing]):
            doAdd = False
            break
    return doAdd

total = 0
#Identify correct prints
for printing in prints:
    middle = printing[len(printing)//2]
    doAdd = checkIfCorrect(printing, rules)
    total += middle*int(doAdd)

print("Total of middle correct prints is: {}".format(total))

#Q2
total = 0
for printing in prints:
    if not checkIfCorrect(printing, rules):
        while not checkIfCorrect(printing, rules):
            elem = printing.pop()
            indexes = [printing.index(rule) if rule in printing else 1000 for rule in rules[elem]]
            minIndex = min(indexes)
            if minIndex < len(printing):
                printing.insert(minIndex,elem)
            else:
                printing.insert(0, elem)
        middle = printing[len(printing)//2]
        total += middle
            
print("Total of middle corrected prints is: {}".format(total))
