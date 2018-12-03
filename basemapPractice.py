# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 13:14:37 2018

@author: Jack Biscupski
"""

import matplotlib.pyplot as plt
import numpy as np
 
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

m = Basemap(projection='hammer',lon_0=90)
m.drawmapboundary(fill_color='#99ffff')
m.fillcontinents(color='#cc9966',lake_color='#99ffff')

m.scatter(np.random.uniform(low=2, high=90, size=(1,50)), np.random.uniform(low=2, high=90, size=(1,50)),
          latlon=True, # Ta-da!
          marker='o',color='k',
          zorder=10)

plt.title('Hammer projection, data on top',fontsize=12)
plt.show()

#map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
## draw coastlines, country boundaries, fill continents.
#map.drawcoastlines(linewidth=0.25)
#map.drawcountries(linewidth=0.25)
#map.fillcontinents(color='coral',lake_color='aqua')
## draw the edge of the map projection region (the projection limb)
#map.drawmapboundary(fill_color='aqua')c
## draw lat/lon grid lines every 30 degrees.
#map.drawmeridians(np.arange(0,360,30))
#map.drawparallels(np.arange(-90,90,30))
## make up some data on a regular lat/lon grid.
#nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
#lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
#lons = (delta*np.indices((nlats,nlons))[1,:,:])
#wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
#mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
## compute native map projection coordinates of lat/lon grid.
#x, y = map(lons*180./np.pi, lats*180./np.pi)
## contour data over the map.
#cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
#plt.title('contour lines over filled continent background')
#plt.show()