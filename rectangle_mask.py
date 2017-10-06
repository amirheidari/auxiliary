# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:15:34 2017

@author: USER!
"""

import matplotlib
import matplotlib.pyplot as plt

import shapefile
import matplotlib.pyplot as plt
import numpy as np
sf = shapefile.Reader("mygeodata/gulf")
shapes = sf.shapes()

#------------------------------------------------------------
shape_ex = sf.shape(0)
x_lon = []
y_lat = []

for ip in range(len(shapes[0].points)):
    x_lon.append(shape_ex.points[ip][0])
    y_lat.append(shape_ex.points[ip][1])
#

import numpy
from shapely.geometry import box, Polygon, Point
import shapely
import matplotlib.patches as patches
from random import *
#
gulf=Polygon(shape_ex.points[:])


fig=plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
x=numpy.linspace(47, 56, num=51)
y=numpy.linspace(23, 31, num=51)

lon=[[] for i in xrange(2501)] 
lat=[[] for i in xrange(2501)] 
for i in range(1,51):
    for j in range(1,51):        
        b=box(x[i-1],y[j-1],x[i],y[j])
        min_area=b.area*0.8
#        print list(b.exterior.coords)
#        print b.area
        if gulf.intersection(b).area>min_area:
            xmin= b.exterior.coords[3][0]
            ymin=b.exterior.coords[3][1]
            ax.add_patch(patches.Rectangle(
            (xmin,ymin), 0.18, 0.18, alpha=uniform(0,1),
            edgecolor=None))
            
            for k in range(len(b.exterior.coords[:])):
    #            print k
    #            print list(b.exterior.coords[k])
                lon[i].append(b.exterior.coords[k][0])
                lat[i].append(b.exterior.coords[k][1])
                

    ax.plot(lon[i][:],lat[i][:],'red')    
#    
ax.plot(x_lon,y_lat, 'blue')


#ax.add_patch(patches.Rectangle(
#(uniform(47,56),uniform(23,31)), 0.18, 0.18, alpha=0.5,
#edgecolor=None))
    

#rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='yellow')
#rect2 = matplotlib.patches.Rectangle((0,150), 300, 20, color='red')
#rect3 = matplotlib.patches.Rectangle((-300,-50), 40, 200, color='#0099FF')
#circle1 = matplotlib.patches.Circle((-200,-250), radius=90, color='#EB70AA')
#ax.add_patch(rect1)
#ax.add_patch(rect2)
#ax.add_patch(rect3)
#ax.add_patch(circle1)
#plt.xlim([-400, 400])
#plt.ylim([-400, 400])

fig.show()
fig.savefig('rect1.png', dpi=90, bbox_inches='tight')


