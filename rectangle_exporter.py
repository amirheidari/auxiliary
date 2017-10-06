# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:21:39 2017

@author: USER!
"""

import shapefile
import matplotlib.pyplot as plt
import numpy as np
import os

sf = shapefile.Reader("mygeodata/gulf")
shapes = sf.shapes()

shape_ex = sf.shape(0)
x_lon = []
y_lat = []

for ip in range(len(shapes[0].points)):
    x_lon.append(shape_ex.points[ip][0])
    y_lat.append(shape_ex.points[ip][1])
    
#------------------------------------------------------------------------------
from shapely.geometry import box, Polygon, Point
#
gulf=Polygon(shape_ex.points[:])
#
##b=box(50,28,50.2,28.2)
##print b.area
##print b.disjoint(gulf)
#
##
fig=plt.figure()
#ax = plt.axes() # add the axes
ax = fig.add_subplot(1,1,1)

ax.set_aspect('equal')
x=np.linspace(47, 56, num=51)
y=np.linspace(23, 31, num=51)

sensitivity=10

lon=[[] for i in xrange(2501)] 
lat=[[] for i in xrange(2501)]
master_rectangle=[] 
for i in range(1,51):
    for j in range(1,51):
        b=box(x[i-1],y[j-1],x[i],y[j])
        min_area=b.area*0.8
#        
#        print b.area
        if gulf.intersection(b).area>min_area:
            master_rectangle.append(list(b.exterior.coords))
            master_rectangle.append(sensitivity)
#            print a [0][0]
#            b2=gulf.intersection(b)
            for k in range(len(b.exterior.coords[:])):
    #            print k
    #            print list(b.exterior.coords[k])
                lon[i].append(b.exterior.coords[k][0])
                lat[i].append(b.exterior.coords[k][1])
        
    
#    print 'payam'
#    print lon[i][:]
#    print lat[i][:]
    ax.plot(lon[i][:],lat[i][:],'red')
ax.plot(x_lon,y_lat, 'blue')

fig.show()
#    

# rectangle save as .txt
rec_gen='rectangle_generator_result'
if not os.path.exists(rec_gen):
    os.makedirs(rec_gen)
#np.savetxt(rec_gen+'/Rectangles.txt',master_rectangle[:],fmt='%s')

s=open(rec_gen+'/rectangle_input.txt','w')
for i in range(10):
    s.write("%i"%i)
    for j in range(5):
        s.write("-%f-%f"%(master_rectangle[2*i][j][0],master_rectangle[2*i][j][1]))
    s.write("-%f"%master_rectangle[(2*i)+1])
    s.write("\n")
s.close()
