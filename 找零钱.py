# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:15:15 2017

@author: Administrator
"""

money = raw_input('Enter your money:')
money = int(money)
quarters = money/15
print quarter
money = money - quarter * 15
dimes = money/10
print dimes
print('{0:<20s}{1:2d}'.format('money:',money))