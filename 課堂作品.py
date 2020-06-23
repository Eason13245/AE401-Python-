#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:46:30 2020

@author: gaoyixun
"""


score = []
name = []
Highestname = 0
Lowname = 0
H = 0
S = 100
T = 0

N = int(input("How many student?"))

for a in range(N):
    n = input("The name of the student:")
    s = int(input("The score of the student:"))
    name.append(n)
    score.append(s)
    print(name)
    print(score)
    
def Highest_score():
    H = 0
    for i in range(0,1*N):
        if score[i] > H:
            H = score[i] 
    return H

H = Highest_score()

def Highest_name():
    H = 0
    for i in range(0,1*N):
        if score[i] > H:
            H = score[i]
            Highestname = name[i]
    return Highestname
        
Highestname = Highest_name()

def Lowest_score():
    S = 100
    for i in range(0,1*N):
        if S > score[i]:
            S = score[i]
    return S

S = Lowest_score

def Lowest_name():
    S = 100
    for o in range(0,1*N):
        if S > score[o]:
            S = score[o]
            Lowname = name[o]
    return Lowname
        
Lowname = Lowest_name

def Total():
    T = 0
    for i in range(0,1*N):
        T += score[i]
    T = T/N
    return T

T = Total()

print("Highest", Highestname, H)
print("Lowest", Lowname, S)
print("Average", T)

