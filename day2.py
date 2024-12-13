#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day2.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1 and 2
nbReports = 0
nbReportsRemoving = 0
for line in lines:
    numbers = line.replace("\n", "").split(" ")
    numbers = np.array([int(x) for x in numbers])
    diff = numbers[:-1]-numbers[1:]
    sign = np.all(diff>0) or np.all(diff<0)
    minmax = np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)
    if sign and minmax:
        nbReports += 1
    else:
        for i, number in enumerate(numbers):
            mask = np.ones(numbers.shape,dtype=bool)
            mask[i] = False
            array = numbers[mask]
            diff = array[:-1]-array[1:]
            sign = np.all(diff>0) or np.all(diff<0)
            minmax = np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)
            if sign and minmax:
                nbReportsRemoving += 1
                break
        
print("Nb Correct reports is: {}".format(nbReports))
print("Nb Correct reports with removing is: {}".format(nbReports+nbReportsRemoving))