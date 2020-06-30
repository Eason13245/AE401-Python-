#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:30:55 2020

@author: gaoyixun
"""
import random

Name = ["Eason", "Lee", "Ray"]
Verb = ["play", "kick", "read"]
Noun = ["ball", "game", "book"]

def Sentence_Vocabulary(List):
    Word = random.sample(List,1)[0]
    return Word

def Creat_sentence(List1,list2,List3):
    sentence = Sentence_Vocabulary(List1)+Sentence_Vocabulary(list2)+Sentence_Vocabulary(List3)
    return sentence

for i in range(10):
    print(Creat_sentence(Name,Verb,Noun), ".")
    