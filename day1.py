#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day1.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
total = 0
data1 = []
data2 = []
for line in lines:
    numbers = line.replace("\n", "").split("   ")
    data1.append(int(numbers[0]))
    data2.append(int(numbers[1]))
data1.sort()
data2.sort()
diff = np.sum(np.abs(np.array(data1)-np.array(data2)))
print("Difference score is: {}".format(diff))

#Q2
similarity = 0
for number in data1:
    similarity += number * data2.count(number)
    
print("Similarity score is: {}".format(similarity))