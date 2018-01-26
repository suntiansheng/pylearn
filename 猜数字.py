# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 22:11:30 2017

@author: Administrator
"""

from random import randint

x=randint(0,300)
print x
for count in range(0,5,1):
    print 'please input a number between 0 and 300:'
    digit = input()
    if digit == x:
        print 'bingo!'
        break
    elif digit >x:
        print 'the number is too large'
    else:
        print 'the number is too small'
    count+=count
