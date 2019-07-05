import math
import random
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

class Rival:
    def __init__(self,route):
        self.jealousy = 1
        self.route = route
        shuffle(self.route)
        self.convert_float()
        self.score = self.route_score(self.route)

    def route_score(self, route):
        score = 0
        len_route = len(route)
        for i in range(len_route):
            score = score + math.hypot(route[(i+1)%len_route][1]-route[i][1], route[(i+1)%len_route][2]-route[i][2])
        return score

    def convert_float(self):
        for i in range(len(self.route)):
            self.route[i] = list(map(float,self.route[i]))

    def make_move(self):
        num1 = random.randint(0,len(self.route)-1)
        num2 = random.randint(0,len(self.route)-1)

        if num1 < num2:
            temp_route = self.route[:num1+1] + self.route[num1+1:num2+1][::-1]+self.route[num2+1:]
        else:
            temp_route = self.route[:num2+1] + self.route[num2+1:num1+1][::-1]+self.route[num1+1:]

        temp_score = self.route_score(temp_route)
        diff = self.score - temp_score

        if diff > 0:
            self.score = temp_score
            self.route = temp_route

        else:
            diff = diff/150
            prob = math.exp(diff/self.jealousy)
            #print(prob)
            if (random.uniform(0,1) < prob):
                self.score = temp_score
                self.route = temp_route

f = open("qatar.txt","r")
lst = []
for x in f:
    lst.append(x.split())
    
r1 = Rival(lst)

for i in range(1000000):
    r1.make_move()
    lst.append(i)
    if i > 10 and i%10 == 0 :
        r1.jealousy = r1.jealousy * 0.9999
    if i%10000 == 0:  
        print(r1.score, r1.jealousy)

