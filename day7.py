#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day7.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
total = 0
equations = defaultdict(list)
for line in lines:
    equation = re.findall(r"(\d+)", line.replace("\n", ""))
    equations[int(equation[0])] = [int(eq) for eq in equation[1:]]
    
def checkEquations(total, current, numbers):
    if len(numbers) == 0:
        if current == total:
            return True
        return False
    
    if current == 0:
        current = numbers.pop(0)
        return checkEquations(total, current, numbers.copy())
    
    element = numbers.pop(0)
    return checkEquations(total, current + element, numbers.copy()) or checkEquations(total, current*element, numbers.copy())

for equation in equations:
    isOk = checkEquations(equation, 0, equations[equation])*equation
    total += isOk
    
print("Total of correct equations is: {}".format(total))

#Q2
total = 0
equations = defaultdict(list)
for line in lines:
    equation = re.findall(r"(\d+)", line.replace("\n", ""))
    equations[int(equation[0])] = [int(eq) for eq in equation[1:]]

def checkEquations2(total, current, numbers):
    if len(numbers) == 0:
        if current == total:
            return True
        return False
    
    if current == 0:
        current = numbers.pop(0)
        return checkEquations2(total, current, numbers.copy())
    
    element = numbers.pop(0)
    return checkEquations2(total, current + element, numbers.copy()) or checkEquations2(total, current*element, numbers.copy()) or checkEquations2(total, int(str(current)+str(element)), numbers.copy())

for equation in equations:
    isOk = checkEquations2(equation, 0, equations[equation])*equation
    total += isOk
    
print("Total of correct equations is: {}".format(total))