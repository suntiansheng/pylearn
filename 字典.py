# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:03:53 2017

@author: Administrator
"""

count = dict()
names = ['sunao','sunao','sunao','sunao','huangxiao','huangxiao','huangxiao']
'''
for name in names:
   if name not in count:
       count[name] = 1
   else:
       count[name] = count[name]+1
print count
'''


for name in names:
    count[name] = count.get(name,0)+1
print count

mydic = dict()
mydic['A'] = 1
mydic['B'] = 2

'''
for key,value in mydic.items():
    if bigcount == None or value > bigcount:
        bigcount = value
        bigword = key
print bigword,bigcount
'''
lines = str()
mhand = open(r'F:\pythondir\mbox-short.txt')
mhand.seek(0)
mytext = mhand.read()
#print lines
words = mytext.split()
count = dict()
for word in words:
    count[word] = count.get(word,0)+1
print count


#找最大
bigcount = None
bigword = None
for word,count in count.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigword = word
print bigword,bigcount
    
