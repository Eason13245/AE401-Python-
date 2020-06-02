#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:26:47 2020

@author: gaoyixun
"""


import random
D = random.randint(1,20)
a = 0

while a < 5:
    guess = int(input('Guess the number'))
    if D == guess:
        print('Bingo')
        print(a)
    elif D < guess:
        print("higher")
        a = a+1
    else:
        print('lower')
        a = a+1




