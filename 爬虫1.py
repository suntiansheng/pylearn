# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:18:49 2017

@author: Administrator
"""

import urllib
from BeautifulSoup import *


url = 'http://www.dr-chuck.com/page2'

for i in range(2):
    i = str(1)
    url = 'http://www.dr-chuck.com/page'+i+''
    print url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    print soup
    tags = soup('a')
    for tag in tags:
        print tag
        print tag.get('href',None)
        print 'Contents:',tag.contents[0]
        print 'Attrs:',tag.attrs
    
    