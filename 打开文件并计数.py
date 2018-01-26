# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 14:53:40 2017

@author: Administrator
"""

fhand = open(r'F:\pythondir\mbox.txt')


shand = open(r'F:\pythondir\mbox-short.txt')

fhand.seek(0)
count = 0
for line in fhand:
    count = count + 1
print 'Line Count:', count


shand.seek(0)
count1 = 0
for line in shand:
    count1 = count1 + 1
print 'Line Count:', count1

shand.seek(0)
for line in shand:
    print line
    
for line in range(100):
    print shand[line]


shand.seek(0)
for line in shand:
    line = line.rstrip()
    if line.startswith('From'):
        print line
    
shand.seek(0)
for line in shand:
    line = line.rstrip()
    if not line.startswith('From'):
       continue
    print line


shand.seek(0)
for line in shand:
    line = line.rstrip()
    if line.startswith('From '):
        #print line
        word = line.split()
        print word[2]
'''
shand = open(r'F:\pythondir\mbox-short.txt')
count1 = 0
for i in shand:
    count1 = count1 + 1 

for line in shand:
    if line.startswith('From'):
        print line
'''