#!/usr/bin/env python3
import numpy as np
import re

f = open("ressources/day3.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Q1
file = ""
for line in lines:
    file += line.replace("\n", "")
    
x = re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", file)
total = 0
for mul in x:
    total += int(mul.split("(")[1].split(",")[0])*int(mul.split(",")[1].split(")")[0])
print("Total mul is: {}".format(total))

#Q2
x = re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)|do\(\)|don't\(\)", file)
do = 1
total = 0
for mul in x:
    if mul == "do()":
        do = 1
        pass
    elif mul == "don't()":
        do = 0
        pass
    else:
        total += do*int(mul.split("(")[1].split(",")[0])*int(mul.split(",")[1].split(")")[0])
print("Total mul with dos is: {}".format(total))
