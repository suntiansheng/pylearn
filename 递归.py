# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:57:34 2017

@author: Administrator
"""


import 
#循环
def fib(n):
    a,b=0,1
    count= 1
    while count < n:
        a,b=b,a+b
        count = count+1
    return a
    
#递归
def fib_other(n):
    if n==1:
        return n-1
    elif n==2:
        return n-1
    elif n>2:
        return(fib_other(n-1)+fib_other(n-2))