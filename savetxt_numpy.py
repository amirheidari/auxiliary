# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:10:48 2017

@author: USER!
"""

import numpy as np
x = np.arange(20).reshape((4,5))
np.savetxt('test.txt', x)