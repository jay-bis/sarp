# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:37:27 2018

@author: Jack Biscupski
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure()

# for loop fixes non-negative longitude values (the area we flew around in, all lon's should be negative)
df = pd.read_excel('SARP2018.xlsx')
for i in range(len(df)):
    if df['Decimal Longitude'].values[i] > 0:
        df['Decimal Longitude'].values[i] = -df['Decimal Longitude'].values[i]
        

H22 = df[['Decimal Latitude', 'Decimal Longitude', 'HCFC-22 (MS)', 'Pressure Altitude (feet)']]
H141b = df[['Decimal Latitude', 'Decimal Longitude', 'HCFC-141b (MS)', 'Pressure Altitude (feet)']]
H142b = df[['Decimal Latitude', 'Decimal Longitude', 'HCFC-142b', 'Pressure Altitude (feet)']]

m = Basemap(projection='cea',llcrnrlat=30,urcrnrlat=38,\
            llcrnrlon=-121,urcrnrlon=-114,resolution='f')

# check for altitude bias
alts22, alts141b, alts142b = H22[H22['Pressure Altitude (feet)'] > 2000], H141b[H141b['Pressure Altitude (feet)'] > 2000], H142b[H142b['Pressure Altitude (feet)'] > 2000]
lon, lat = H22['Decimal Longitude'].values, H22['Decimal Latitude'].values
altlon, altlat = alts22['Decimal Longitude'].values, alts22['Decimal Latitude'].values
#colors22 = np.linspace(H22['HCFC-22 (MS)'].min(), H22['HCFC-22 (MS)'].max(), num=20)

m.drawcountries()
m.drawcoastlines()
m.drawmapboundary(fill_color='#46bcec')
#m.drawparallels(np.arange(30,39,1),labels=[1,0,0,0],linewidth=0)
#m.drawmeridians(np.arange(-121,-113,1),labels=[0,0,0,1],linewidth=0)
m.drawstates()
m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
                 
            
#m.scatter(lon, lat, c=H22['HCFC-22 (MS)'].values, cmap='jet', latlon=True, vmax=600, vmin=150, marker="^", zorder=10, alpha=0.9)
#m.scatter(lon, lat, c=H141b['HCFC-141b (MS)'].values, cmap='jet', vmin=20, vmax=45, latlon=True, marker="^", zorder=10, alpha=0.9)
m.scatter(lon, lat, c=H142b['HCFC-142b'].values, cmap='jet', vmin=20, vmax=35, latlon=True, marker="^", zorder=10, alpha=0.9)

# altitude bias mapping
#m.scatter(altlon, altlat, c=alts22['HCFC-22 (MS)'].values, cmap='jet', latlon=True, vmax=600, vmin=150, marker="^", zorder=10, alpha=0.9)
#m.scatter(altlon, altlat, c=alts141b['HCFC-141b (MS)'].values, cmap='jet', vmin=20, vmax=45, latlon=True, marker="^", zorder=10, alpha=0.9)
#m.scatter(altlon, altlat, c=alts142b['HCFC-142b'].values, cmap='jet', vmin=20, vmax=35, latlon=True, marker="^", zorder=10, alpha=0.9)

  
plt.title('Mixing Ratios of HCFC-142b', fontsize=20)
#plt.title('Mixing Ratios of 142b (pressure altitude > 2000)')
lb = plt.colorbar()
lb.ax.set_title('ppt', fontsize=16)


# bakersfield point
m.plot(-119.0187, 35.3732, latlon=True, markersize=9, marker="o", color="k", zorder=10, alpha=0.5, label='Bakersfield')
plt.text(253053, 507285, 'Bakersfield', fontsize=12)
# LA point
m.plot(-118.2472, 34.08307, latlon=True, markersize=9, marker="o", color="k", zorder=10, alpha=0.5, label='Los Angeles')
plt.text(208710, 391787, 'Los Angeles', fontsize=12)
# Riverside point
m.plot(-117.0090, 33.9552, latlon=True, markersize=9, marker="o", color="k", zorder=10, alpha=0.5, label='Los Angeles')
plt.text(398457, 386630, 'Riverside', fontsize=12)

lb.ax.tick_params(labelsize=14)

plt.show()