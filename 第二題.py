#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:06:41 2020

@author: gaoyixun
"""

def MultiplicationTable(a):
    for b in range(a):
        for t in range(a):
            print(str(b)+"+"+str(t)+"="+str(b*t),end='')
            print()
