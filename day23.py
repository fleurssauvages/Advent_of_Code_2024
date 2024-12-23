#!/usr/bin/env python3
import numpy as np
import regex as re
from collections import defaultdict

f = open("ressources/day23.txt", "r") #Open File
lines = f.readlines() #Separate in lines

graph = defaultdict(set)
for line in lines:
    line = line.replace("\n", "")
    line = line.split("-")
    graph[line[0]].add(line[1])
    graph[line[1]].add(line[0])
    
#Q1
connections = set()
for node in graph:
    for subnode in graph[node]:
        for subsubnode in graph[subnode]:
            if subsubnode in graph[node]: #We know that subnode in node and subsubnode in subnode, so we check if subsubnode is in node
                if "t" in node[0] or "t" in subnode[0] or "t" in subsubnode[0]: #If one of them starts with a t
                    if node != subnode and node != subsubnode and subnode != subsubnode: #If they are all different
                        connections.add(tuple(sorted([node, subnode, subsubnode]))) #We add the connection to the set of connections

print("The number of connections is: {}".format(len(connections)))

#Q2
lans = set()
for node in graph:
    lan = set([node]) #We start with the node itself
    for subnode in graph[node]:
        if np.all([subnode in graph[lanNode] for lanNode in lan]): #If all the nodes in the LAN are connected to the subnode
            lan.add(subnode) #We add the subnode to the LAN
    lans.add(tuple(sorted(lan))) #We add the LAN to the set of LANs
    
longestLan = max(lans, key=lambda x: len(x)) #We get the longest LAN
print("The longest LAN is: {}".format(",".join(longestLan)))