# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:38:37 2018

@author: Administrator
"""


q = eval(input('day = ?'))

m = eval(input('month = ?'))

if m == 1 or m == 2:
    m += 12

y = eval(input('year = ?'))
j = y//100
k = y%100 - 1

print('day',q ,'month' , m , 'year' , y ,'j' , j ,'k', k)

h = (q + (26 * (m + 1))//10+ k + k//4 + j//4 + 5 * j)%7

print(h)

if h == 0:
    print('saturday')

if h == 1:
    print('sunday')

if h == 2:
    print('monday')
    
if h == 3:
    print('tuesday')
    
if h == 4:
    print('wednesday')
    
if h == 5:
    print('thursday')
    
if h == 6:
    print('friday')