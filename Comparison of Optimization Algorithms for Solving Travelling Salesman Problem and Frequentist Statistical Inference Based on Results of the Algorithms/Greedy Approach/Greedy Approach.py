import math
import random
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

## Score Calculating Function
def route_score(route):
    score = 0
    len_route = len(route)
    for i in range(len_route):
        score = score + math.hypot(route[(i+1)%len_route][1]-route[i][1], route[(i+1)%len_route][2]-route[i][2])
    return score 

## Convert the data into float
def convert_float(route):
        for i in range(len(route)):
            route[i] = list(map(float,route[i]))
        return route


score = 0
final_route = []

## Opening the file
f = open("qatar.txt","r")
route = []
for x in f:
    route.append(x.split())

print(len(route))

## Randomizing the cities in the list
shuffle(route)

## Converting data into float
route = convert_float(route)
    
## Calculate Initial Score
score = route_score(route)


final_route.append(route[0])
dummy_lst = []

del route[0]
len_route = len(route)


current_score = 999999999999999
final_score = 999999999999
final_city = 0


## Greedy Route Function
for i in range(len_route):
    for j in range(len(route)):

        dummy_lst = []
        
        dummy_lst.append(final_route[i])
        dummy_lst.append(route[j])

        current_score = route_score(dummy_lst)
        if current_score < final_score:
            final_score = current_score
            final_city = j


    dummy_lst = []
    final_route.append(route[final_city])
    del route[final_city]
    final_score = 99999999999999
    #print(len(route))
        

print(len(final_route))
final_score = route_score(final_route)
print(final_score)
        
        
        
    
    
    
    
    
