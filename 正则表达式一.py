# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:58:14 2017

@author: Administrator
"""
import re


lis = list()
fhand = open(r'F:\pythondir\mbox.txt')
fhand.seek(0)
for line in fhand:
    line = line.rstrip()
    if re.search('^From:',line):
        lis.append(line)
print lis

f1 = list()
for wrd in lis:
    print wrd
    f1.append(re.findall('@\S+',wrd))
print f1

cou = dict()
for wrd in lis:
    cou[wrd] = cou.get(wrd,0)+1
print cou


print sorted([(v,s) for (s,v) in cou.items()],reverse = True)

    
    
x = 'sfsfd 12 dsa fds fdssd wfrew 234 45 342423 dsf d fsdf sd'

y1 = re.findall('[0-9]+',x)

y2 = re.findall('[0-9]*',x)

y3 = re.findall('[sdfs]+',x)

y3 = re.findall('[sdfs]*',x)