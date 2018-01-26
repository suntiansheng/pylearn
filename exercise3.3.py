# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 16:58:29 2017

@author: Administrator
"""

score = raw_input('score:')
try:
    score = float(score)
except:
    #print 'please input a number!'
    score = -1
if score == -1:
    print 'please input a number!'
elif 0.9 < score <= 1:
    print 'A'
elif 0.8 < score <= 0.9:
    print 'B'
elif 0.7 < score <= 0.8:
    print 'C'
elif 0.6 <= score <=0.7:
    print 'D'
else:
    print 'BAD SCORE!'