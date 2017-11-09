#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:41:17 2017

@author: es3017
"""

## This function computes the analytical solution for the linear advection eq,
## given an initial condition. 

import numpy as np

# use exec because in this way python re-reads the file every time
exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 


SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def Analytical ( InitialConditions_type , grid , c, Nt , T , *args):

    " Analytical solution to linear advection in 1d given the initial profile "
    # Inputs are :
    # InitialConditions_type = a string teling the initial function type,
    # chosen from InitialConditions.py
    # grid = is the grid object defined for the 1d space dimension
    # c= the courant number, 
    # Nt = number of time step , T = physical total time , 
    # Extra args needed when calling squarewave or sine
    
    # Initialise dependent variable ( accounting for phiOld args)
    phiOld = InitialConditions_type(grid.x , *args)
    # Check periodic boundaries
    if np.abs(phiOld[0] - phiOld[-1])> SMALL :
        print('Careful: your initial conditions \
              Phi_O does not have periodic boundaries')
            
    # Exact solution is the initial condition shifted around the domain
    phiExact = InitialConditions_type((grid.x - c*Nt*grid.dx)%grid.length ,\
                                      *args)
    
    return( phiOld , phiExact )
    

