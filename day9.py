#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import time 

f = open("ressources/day9.txt", "r") #Open File
line = f.readlines() #Separate in lines
line = line[0].replace("\n", "")

#Q1
info = list(line)
ids = []

isData = True
id = 0
for number in info:
    ids += [id]*int(number) if isData else [-1]*int(number)
    id += 1*isData
    isData = not isData

ids = np.array(ids)
blanks = np.where(ids == -1)[0]
ids[blanks] = np.flip(np.delete(ids, blanks))[0:len(blanks)]
ids = ids[0:(len(ids)-len(blanks))]

total = np.sum(ids*np.arange(0, len(ids)))
print("Disk Result is: {}".format(total))

#Q2
start_time = time.time()
info = list(line)
ids = []
items = []
reversedItems = []

isData = True
id = 0
start = 0

for number in info:
    ids += [id]*int(number) if isData else [-1]*int(number)
    items += [(id*isData, start, int(number))] #id, start, length, whites have 0 as an id
    if isData:
        reversedItems += [(id, start, int(number))] #don't put whites in the reversed list
    start += int(number)
    
    id += 1*isData
    isData = not isData

reversedItems = reversedItems[::-1]

minLength = 0
for i, item in enumerate(items[1::2]):
    id, start, length = item[0], item[1], item[2]
    while length > minLength:
        desiredItem = next((x for x in reversedItems if x[1] > start and x[2] <= length), None)
        if desiredItem:
            ids[start:start+desiredItem[2]] = [desiredItem[0]]*desiredItem[2] #Turn Whites into the desired id
            ids[desiredItem[1]:desiredItem[1]+desiredItem[2]] = [-1]*desiredItem[2] #Remove the desired id from the list
            
            desiredItemIndex = reversedItems.index(desiredItem)
            reversedItems.pop(desiredItemIndex) #Remove the desired item from the available items
            reversedItems.pop() #Remove the first ones, which is left of the current white spaces
            length -= desiredItem[2] #Update starting point and remaining length
            start += desiredItem[2]
        else:
            minLength = length #There is no block left of that given length
            break

ids = np.array(ids)
blanks = np.where(ids == -1)[0]
ids[blanks] = np.zeros(len(blanks))
total = np.sum(ids*np.arange(0, len(ids)))
delta = time.time() - start_time
print("Time is: {}".format(delta))
print("Disk Result 2 is: {}".format(total))