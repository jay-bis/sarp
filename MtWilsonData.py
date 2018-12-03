# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:35:52 2018

@author: Jack Biscupski
"""

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_excel('MtWilson.xlsx')
df = df[:-6]

plt.scatter(df['Julian Open Time'], df['HCFC-142b (MS)'])
#plt.scatter(df['Julian Open Time'], df['HCFC-22 (MS)'])
plt.xlim([41700, 42600])
plt.ylim([20, 50])
plt.xlabel('Julian Open Time', fontsize=18)
plt.ylabel('ppt of HCFC-142b', fontsize=18)
plt.annotate('Start of January 2015', xy=(42004, 29), xytext=(41983, 40), fontsize=20, arrowprops=dict(arrowstyle="->"))
plt.title('Time series of HCFC-142b mixing ratios at Mt. Wilson, June 2014-May 2016', fontsize=20)
plt.tick_params(axis='both', labelsize=16)