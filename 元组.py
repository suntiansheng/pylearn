# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:15:05 2017

@author: Administrator
"""

rhand = open(r'F:\pythondir\romeo.txt')
romeo = rhand.read()
words = romeo.split()
cou = dict()
for wrd in words:
    cou[wrd] = cou.get(wrd,0)+1

print cou
print cou.items()

print sorted([ (v,w) for (w,v) in cou.items()],reverse=True)
