#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:12:38 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi 

f1 = np.array([0,1,2,3])
f2 = np.array([1,2,3,4])
somma = f1 - f2
print( type(somma))
print(somma)
norma = np.sum(np.absolute(somma))
print(norma)

f1_sq= f1**2
print(f1)
print(f1_sq)