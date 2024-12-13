#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day13.txt", "r") #Open File
lines = f.readlines() #Separate in lines

buttonsA = []
buttonsB = []
prizes = []

#Q1
for line in lines[0::4]:
    x = re.findall("[0-9]+", line)
    buttonsA.append([int(x[0]), int(x[1])])

for line in lines[1::4]:
    x = re.findall("[0-9]+", line)
    buttonsB.append([int(x[0]), int(x[1])])
    
for line in lines[2::4]:
    x = re.findall("[0-9]+", line)
    prizes.append([int(x[0]), int(x[1])])
    
tokens = []
for buttonA, buttonB, prize in zip(buttonsA, buttonsB, prizes):
    sol = np.linalg.solve([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]], prize)
    sol = np.round(sol)
    if buttonA[0]*sol[0]+buttonB[0]*sol[1] == prize[0] and buttonA[1]*sol[0]+buttonB[1]*sol[1] == prize[1]:
        tokens.append([np.round(sol[0]), np.round(sol[1])])

tokens = np.array(tokens)
money = int(np.sum(tokens[:,0]*3+tokens[:,1]))

print("Total money to win is: {}".format(money))

#Q2
prizes = []
for line in lines[2::4]:
    x = re.findall("[0-9]+", line)
    prizes.append([int(x[0])+10000000000000, int(x[1])+10000000000000])
    
tokens = []
for buttonA, buttonB, prize in zip(buttonsA, buttonsB, prizes):
    sol = np.linalg.solve([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]], prize)
    sol = np.round(sol)
    if buttonA[0]*sol[0]+buttonB[0]*sol[1] == prize[0] and buttonA[1]*sol[0]+buttonB[1]*sol[1] == prize[1]:
        tokens.append([np.round(sol[0]), np.round(sol[1])])

tokens = np.array(tokens)
money = int(np.sum(tokens[:,0]*3+tokens[:,1]))

print("Total money to win is actually: {}".format(money))