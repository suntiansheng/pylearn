# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:28:46 2017

@author: Administrator
"""
def compute_pay(time,rate):
    #time=raw_input('please imput the time:')
    try:
        time=float(time)
    except:
        time=-1    #error in time
    #rate=raw_input('please imput the rate:')
    try:
        rate=float(rate)
    except:
        rate=-1    #error in rate
    if 0<time < 40 and rate != -1:
        pay = rate * time
    elif time > 40 and rate != -1:
        pay = rate * 40 + (time - rate) * 55
    elif time == -1 and rate != -1:
        pay = 'error in time'
    elif rate == -1 and time != -1:
        pay = 'error in rate'
    elif time== -1 and rate == -1:
        pay = 'both error'
    return pay