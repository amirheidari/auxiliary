# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 19:26:31 2017

@author: USER!
"""

from matplotlib import pyplot
from shapely.geometry import LineString
from descartes import PolygonPatch

BLUE = '#6699cc'
GRAY = '#999999'

def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)

line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

fig = pyplot.figure(1, figsize=(10, 4), dpi=180)

# 1
ax = fig.add_subplot(121)

plot_line(ax, line)

#dilated = line.buffer(0.5)
#patch1 = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
#ax.add_patch(patch1)
