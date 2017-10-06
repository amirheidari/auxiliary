# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 09:31:57 2017

@author: USER!
"""
from shapely.geometry import Polygon, LineString, Point, MultiPoint
from shapely.ops import polygonize_full, polygonize, split

points = MultiPoint([(4,5),(9,18),(6,5)]) 
line = LineString([(1,2),(8,7),(4,5),(2,4),(4,7),(8,5),(9,18),(1,2),(12,7),(4,5),(6,5),(4,9)])
splitted = split(line, points)
for lin in splitted:
      print lin