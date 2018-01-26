# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 16:51:17 2017

@author: Administrator
"""

import math
signal_power = 9
noise_power = 10
signal_power = float(signal_power)
ratio = signal_power/noise_power
decibels = 10 * math.log10(ratio)
print decibels