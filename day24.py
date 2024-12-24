#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
from functools import lru_cache as cache

f = open("ressources/day24.txt", "r") #Open File
lines = f.readlines() #Separate in lines

#Reading Data
def read(lines):
    wires = defaultdict(int)
    outputs = list()
    for i, line in enumerate(lines):
        line = line.replace("\n", "")
        line = line.replace(":", "")
        if len(line) == 0:
            break
        line = line.split(" ")
        wires[line[0]] = int(line[1])

    gates = defaultdict(tuple)
    for line in lines[i+1:]:
        line = line.split()
        gates[line[4]] = (line[0], line[1], line[2])
        if line[4].startswith("z"):
            outputs.append(line[4])
    outputs.sort()
    return wires, gates, outputs

#Q1
def solve(wires, gates, outputs):
    @cache
    def evaluate(wire):
        if wire in wires:
            return wires[wire]
        input1, gate, input2 = gates[wire]
        value1 = evaluate(input1)
        value2 = evaluate(input2)
        if gate == "AND":
            wires[wire] = (value1 & value2)*1
        if gate == "OR":
            wires[wire] = (value1 | value2)*1
        if gate == "XOR":
            wires[wire] = (value1 != value2)*1
        return wires[wire]
            
        
    bitList = []
    for output in outputs:
        value = evaluate(output)
        bitList.append(value)
    bitList.reverse()
    return int("".join(str(x) for x in bitList), 2)

wires, gates, outputs = read(lines)
result = solve(wires, gates, outputs)
print("The output is: {}".format(result))

#Q2
#Full adder using logic : 
# SUM = (xi XOR yi) XOR Cin
# CARRY-OUT = (xi AND yi) OR (Cin AND (xi XOR yi))
    
wrongGates = set()
for wire in wires:
    if (wire.startswith("x") or wire.startswith("y")):
        continue
    input1, gate, input2 = gates[wire]
    if not gate == "XOR" and wire.startswith("z") and wire != "z45": #SUM has an XOR output gate, except last one
        wrongGates.add(wire)
        continue
    input1, gate, input2 = gates[wire]
    if gate == "XOR" and not (input1.startswith("x") or input1.startswith("y")) and not wire.startswith("z"): #XORs that don't ouput z must be connected to x and y
        wrongGates.add(wire)
        continue
    input1, gate, input2 = gates[wire]
    if gate != "OR": #ANDs must have OR below
        if not (input1.startswith("x") or input1.startswith("y")):
            input11, gate, input22 = gates[input1]
            if gate == "AND" and input11 != "x00" and input11 != "y00":
                wrongGates.add(input1)
                continue
        if not (input2.startswith("x") or input2.startswith("y")):
            input11, gate, input22 = gates[input2]
            if gate == "AND" and input11 != "x00" and input11 != "y00":
                wrongGates.add(input2)
                continue
    input1, gate, input2 = gates[wire]
    if gate == "OR" and not wire.startswith('z'): #other XORs must have OR below
        if not (input1.startswith("x") or input1.startswith("y")):
            input11, gate, input22 = gates[input1]
            if gate == "XOR" and (input11.startswith("x") or input11.startswith("y")):
                wrongGates.add(input1)
        if not (input2.startswith("x") or input2.startswith("y")):
            input11, gate, input22 = gates[input2]
            if gate == "XOR" and (input11.startswith("x") or input11.startswith("y")):
                wrongGates.add(input2)

wrongGates = sorted(list(wrongGates))
print("The mismatchs are: {}".format(",".join(wrongGates)))