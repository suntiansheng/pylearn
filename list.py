# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 16:20:35 2017

@author: Administrator
"""

stuff = list()
stuff.append('book')
stuff.append(99)



numlist = list()
while True:
    num = raw_input('input a number:')
    if num == 'done':
        break
    num = float(num)
    numlist.append(num)
print numlist
avg = sum(numlist)/len(numlist)
print avg