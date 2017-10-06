# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 12:09:00 2017

@author: USER!
"""

from netCDF4 import Dataset
nc=Dataset('1.nc','r')
print nc.variables.keys()
print nc.dimensions.keys()
#print nc.dimensions['x']
#print nc.dimensions['data']
#print nc.variables['nav_lat']
#print nc.variables['lat']



#for varname in nc.variables.keys():
#     var = nc.variables[varname]
#     print varname, var.dtype, var.dimensions, var.shape


#
t=nc.variables['lat']
print t[0,0,1,0]

#print t.shape
#print t[0]

#v=nc.variables['vos']
#depthv=nc.variables['depthv_bounds']

#lon=nc.variables['nav_lon']
#v=nc.variables['vos']

#print lat.shape
#print lon.shape
#print lat[:523]
#print lon[:619]
#print v[0,0,100,100]

#print depthv[:2]

#print v[0,0,100,100]




#
#
#i=0
#e=0
#while i<5:
#    dt=t[i+1]-t[i]
#    if dt!=0.5:
#        print i, t[i], dt
#        e+=1
#    i+=1          
#if e==0: print "Data are increasing and regular"
#
#print t[2]-t[1]

#d=nc.variables['deptht']
##print u[:]
#print d.shape
##print nc.dimensions['deptht']
#print d[1,]

#d=nc.variables['deptht_bounds']
#print u[:]
#print d.shape
#print nc.dimensions['deptht']
#print d[1,]

#lat=nc.variables['nav_lat']
#lon=nc.variables['nav_lon']
#v=nc.variables['uos']
#print lat
#print v
#print lat.dimensions
#print v.dimensions
#
##print lat[0,104]
##print lon[0,104]
#print lat[300,480]
#print lon[300,480]
#
#print v[0,0,300,600]







#t=nc.variables['time_counter_bounds']
#print t.shape
#print t.dtype
#print t.dimensions
#print t[:]


nc.close()
