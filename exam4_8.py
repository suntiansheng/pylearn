# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:38:39 2018

@author: Administrator
"""

a , b , c = eval(input('a')) , eval(input('b')) , eval(input('c'))
if a+b>c and a+c>b and b+c>a :
    l = a + b + c
    print(l)
else:
    print('error')