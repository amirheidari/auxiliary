# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:00:17 2017

@author: USER!
"""

f = open('myfile.txt','w')
#f.seek(0)
number=2
f.write('hi there %i\n'%number)
f.write('hi there' ) #
f.close()



f=open('myfile.txt','r')
f.seek(0,1) #second parameter: 0:begining of file,1: current poition, 2: end of file 
for index in range(2):
   line = f.readline()
   print "Line No %d - %s" % (index, line)
f.close()