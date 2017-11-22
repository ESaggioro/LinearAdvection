#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:09:21 2017

@author: es3017
"""

# Test grid

exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Analytical_Slicing.py").read())

import matplotlib.pyplot as plt
import numpy as np

def main():
    
    # Set the grid
    nx = 3
    L = 1.0 # (meters)
    Gridx = Grid (nx,L)
    
    print('x=',Gridx.x)
    print('dx=',Gridx.dx)
    
    
main()