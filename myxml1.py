# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:40:21 2017

@author: Administrator
"""

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)

tree.find('name').text
tree.find('phone').text.strip()