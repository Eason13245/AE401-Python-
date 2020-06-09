#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:03:53 2020

@author: gaoyixun
"""


import turtle
Ray = turtle.Turtle()
Ray.color('blue')
Ray.shape('turtle')
canvas = turtle.Screen()
canvas.title('Turtle window')
canvas.bgcolor('white')

for x in range(0,60,2):
    Ray.forward(x)
    Ray.left(20)
    
turtle.done()
turtle.bye()



