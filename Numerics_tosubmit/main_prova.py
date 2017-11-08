#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:09:46 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


exec(open("./InitialConditions.py").read())
# use exec for grid.py because in this way python re-read the file
exec(open("./grid.py").read()) 
import Analytical 
import CTCSAlone
import CTBSAlone
import FTCSAlone

def main():
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations. Thus grid.dx and    ###
    ## grid.x will automatically be defined
    gridx = Grid( 100 , 1.0 )
    x = gridx.x
    
    bell = cosBell(x)
    square = squareWave(x, 0.2 , 0.5 )
    k=5
    sines = sine (x, k , 2.0)
    
    plt.plot(x, bell, 'b', label = 'cosbell')
    plt.plot(x, square, 'r', label = 'square')
    plt.plot(x, sines, 'k', label = 'sine k=%g' %k)
    plt.legend()
    plt.show()
    
    
    
    

    
    
    
    
main()