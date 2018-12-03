# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:43:18 2018

@author: Jack Biscupski
"""

import matplotlib.pyplot as plt
from pylab import *

import pandas as pd

df = pd.read_excel('refrigerantsAVG.xlsx')

plt.figure(3)

plt.subplot(131)
m1, b1 = polyfit(df['Year'], df['R-22 avg (ppt)'], 1)
plt.plot(df['Year'], df['R-22 avg (ppt)'], label='HCFC-22 data')
plt.plot(df['Year'], m1*df['Year']+b1, '--k', label='slope of fit line: {0:.3f}'.format(m1))
plt.ylim([255, 290])
plt.title('ppt of HCFC-22')
plt.legend()

plt.subplot(132)
m2, b2 = polyfit(df['Year'], df['R-142b (avg ppt)'], 1)
plt.plot(df['Year'], df['R-142b (avg ppt)'], label='HCFC-142b data')
plt.plot(df['Year'], m2*df['Year']+b2, '--k', label='slope of fit line: {0:.3f}'.format(m2))
plt.ylim([22,30])
plt.title('ppt of HCFC-142b')
plt.legend()

plt.subplot(133)
m3, b3 = polyfit(df['Year'], df['R-141b (avg ppt)'], 1)
plt.plot(df['Year'], df['R-141b (avg ppt)'], label='HCFC-141b data')
plt.plot(df['Year'], m3*df['Year']+b3, '--k', label='slope of fit line: {0:.3f}'.format(m3))
plt.ylim([25, 33])
plt.title('ppt of HCFC-141b')
plt.legend()
