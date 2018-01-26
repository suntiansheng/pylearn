# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:24:04 2017

@author: Administrator
"""

import urllib,BeautifulSoup
#import xml.etree.ElementTree as ET

url = 'http://www.dr-chuck.com/page1.htm'
url = 'http://bbs.pinggu.org/thread-3942571-1-1.html'

html = urllib.urlopen(url).read()

soup = BeautifulSoup.BeautifulSoup(html)

tags = soup('p')
for tag in tags:
    print tag.text
    
tags = soup('a')
for tag in tags:
    print tag.get('href')
    