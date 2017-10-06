# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:19:58 2017

@author: USER!
"""

#from windrose import WindroseAxes
#from matplotlib import pyplot as plt
#import numpy as np
#from matplotlib.projections import register_projection
#ws = [20, 20, 20, 1000, 1000,1000]
#wd = [270,270,270,12,12,12]
##
#fig=plt.figure()
#rect=[1,1,1,1] 
#wa=WindroseAxes(fig, rect)
#fig.add_axes(wa)
#wa.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
#
#plt.show()

#----------------------------------------------
from matplotlib import pyplot as plt
import windrose
import matplotlib.cm as cm
import numpy as np

ws = np.random.random(500) * 6
wd = np.random.random(500) * 360

fig = plt.figure()
ax = fig.add_subplot(111, projection="windrose")

ax.contourf(wd, ws, bins=np.arange(0, 8, 1), cmap=cm.hot)

ax.legend(bbox_to_anchor=(1.02, 0))
plt.show()
#----------------------------------------------------
