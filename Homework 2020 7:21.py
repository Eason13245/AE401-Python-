#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:25:58 2020

@author: gaoyixun
"""


import os.path


if not os.path.isfile('a.txt'):
    fo = open('a.txt','w')
else:
    fo = open('a.txt','r')
    foc = fo.read() 

while True:
    print('Function=>')
    print('1. insort the text')
    print('2. Count the number of occurrences of a word')
    print('3. ')
    print('4  Instead the vocabulary')
    print('5  Finish')
    
    sel = input('Please insert the function you choose: ')
    
    if sel=='1': # 設定英文單字
        print(foc)
        foc = input("What do you want to write?")
        fo = open('a.txt','w')
        fo.write(foc)
        fo.close()
        
    elif sel=='2':     
        print(foc)
        Word = input('Whihc vocabulary do you want to inquire?')
        range1 = int(input('From which section of the text(with number)'))
        range2 = int(input('To which section of the text?(with number)'))
        Ans = foc.count(Word,range1,range2)
        print(Ans)
        
    elif sel=='4':
        print(foc)
        Voc = input('Which vocabulary are you going to replace?')
        IVoc = input('Which Vocabulary do you want to use to insteat?')
        foc = foc.replace(Voc,IVoc)    
        print(foc)
        fo = open('a.txt','w')
        fo.write(foc)
        fo.close()
        
    elif sel=='5':
        break
    
fo.close()
