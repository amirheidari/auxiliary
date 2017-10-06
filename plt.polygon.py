# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:51:03 2017

@author: USER!
"""
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
plt.axes()
points = [[2, 1], [8, 4], [8, 4],[2, 3]]
#polygon = plt.Polygon(points)
poly1 = Polygon([(0, 0), (10, 0),(10,1), (10, 4),(0, 4),(0,0)])
#bound1=poly1.boundary
poly2=poly1.buffer(0.5)
poly3=poly2.difference(poly1)
polygon = plt.Polygon(points)
plt.gca().add_patch(polygon)

plt.axis('scaled')
plt.show()