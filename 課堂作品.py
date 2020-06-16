#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 18:46:30 2020

@author: gaoyixun
"""


score = []
name = []
H = 0
S = 100
T = 0

N = int(input("How many student?"))

for a in range(N):
    n = input("The name of the student:")
    s = int(input("The score of the student:"))
    name.append(n)
    score.append(s)
    
for each_score in score:
    if each_score > H:
        H = each_score
        
for each_score in score:
    if S > each_score:
        S = each_score
        
for each_score in score:
    T += each_score

T = T/5

print("Highest", H)
print("Lowest", S)
print("Total", T)