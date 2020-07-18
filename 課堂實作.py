#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:21:41 2020

@author: gaoyixun
"""


d = {}
print('########################')
print('#Python英文字典#')
print('########################')
while True:
    print('功能=>')
    print('1. 設定英文單字')
    print('2. 列出英文單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    sel = input('請輸入欲執行選項: ')
    if sel=='1': # 設定英文單字
       while True:
           Voc = input('輸入英文單子（案Q可退出）')
           if Voc == 'Q':
               break
           if Voc not in d:
               CVoc = input('輸入中文翻譯')
               d[Voc] = CVoc
           else:
                print('已經有這個單字')     
        if not os.path.isfile('Thedictionary.txt'):
            fo = open('Thedictionary.txt','w')
        else:
            fo = open('Thedictionary.txt','a')
        for k, v in d.itmes():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('/n')
        fo.close()
    elif sel=='2': # 列出英文單字
        if not os.path.isfile('Thedictionary.txt'):
            print('目前字典是空的')
        else:
            fo = open('Thedictionary.txt','r')
            foc = fo.read()
            print(foc)
    elif sel=='3': # 英翻中
        Voc = input('輸入想要翻譯的英文單字:')
        print(d[Voc])
    elif sel=='4': # 中翻英
        Word_exist = False
        CVoc = input('輸入想要翻譯的中文單字')
        for k, v in d.itmes():
            if v==CVoc:
                print(k)
                Word_exist = True
        if Word_exist== False:
            print('查不到')
    elif sel=='5': # 測驗學習成果
        score = 0
        print('你的總分是', len(d))
        for k, v in d.itmes():
            print(v,':')
            ans = input()
            if ans==k:
                score+=1
                print('正確，你的總分是', score)
            else:
                print('錯誤，你的總分是', score)
    elif sel=='6':
            break
    else:
        print('wrong input')