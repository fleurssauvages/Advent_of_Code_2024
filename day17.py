#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict
import sys
import time

f = open("ressources/day17.txt", "r") #Open File
lines = f.readlines() #Separate in lines

registers = defaultdict(int)
registers["A"] = int(re.findall(r"\d+", lines[0])[0])
registers["B"] = int(re.findall(r"\d+", lines[1])[0])
registers["C"] = int(re.findall(r"\d+", lines[2])[0])

def combo(x, y):
    if y == 0: return 0
    if y == 1: return 1
    if y == 2: return 2
    if y == 3: return 3
    if y == 4: return x["A"]
    if y == 5: return x["B"]
    if y == 6: return x["C"]
    return None

def operation(operand, registers, literal):
    literal = int(literal)
    comboNumber = combo(registers, literal)
    if operand == "0": 
        registers["A"] = registers["A"]//(2**comboNumber)
        return "instruction", None
    elif operand == "1": 
        registers["B"] = registers["B"] ^ literal
        return "instruction", None
    elif operand == "2": 
        registers["B"] = comboNumber % 8
        return "instruction", None
    elif operand == "3":
        if registers["A"] != 0:
            return "JUMP", literal
        else:
            return "instruction", None
    elif operand == "4":
        registers["B"] = registers["B"] ^ registers["C"]
        return "instruction", None
    elif operand == "5": 
        return "instruction", comboNumber % 8
    elif operand == "6":
        registers["B"] = registers["A"]//(2**comboNumber)
        return "instruction", None
    elif operand == "7":
        registers["C"] = registers["A"]//(2**comboNumber)
        return "instruction", None

def run(program, registers):
    outputs = []
    instructionPointer = 0
    while True:
        if instructionPointer >= len(program): break
        operand = program[instructionPointer]
        literal = program[instructionPointer+1]
        toDo, output = operation(operand, registers, literal)
        if toDo == "JUMP":
            instructionPointer = output
        else:
            if output is not None:
                outputs.append(output)
            instructionPointer += 2
    return outputs

#Q1
program = re.findall("\d+", lines[4])
outputs = run(program, registers)
print("Output is: {}".format("".join([str(output)+"," for output in outputs])))

#Q2
solutions = []
possibilities = [(1, 0)] #Start by finding one digit
for nbDigits, a in possibilities:
    for a in range(a, a+8): #We solve bit per bit : each bit can be between 0 and 7
        registers = defaultdict(int)
        registers["A"] = a
        output = run(program, registers)
        output = [str(output) for output in output]
        if output == program[-nbDigits:]: #We found the correct first nb bits, we can now find the next one, add this to the possibiles solutions
            if nbDigits == len(program): #We have the correct number of bits ! This is a solution !
                solutions.append(a)
            else: #Otherwise we need more bits !
                possibilities += [(nbDigits+1, a*8)] #We multiply by 8 to shift the bits
                
print("Solution is: {}".format(np.min(solutions))) #There are several solutions, we take the smallest one