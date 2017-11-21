#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:59:47 2017

@author: es3017
"""

import numpy as np
exec(open("./FTBS.py").read())
exec(open("./FTFS.py").read())

# CTCS scheme fro linear advection with periodic boundaries 
# Accuracy : 2 - 2
# Stability : c in [-1,1]

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def CTCS ( gridx, phi0, c , tsteps ): 
    "Linear advection of initial profile phi0 using CTCS, Courant number c"
    "for tsteps time-steps "
    # gridx = the grid object
    # phi0 = initial contition
    # c = courant number
    # tsteps = number of time steps
    
    if np.abs(phi0[0] -phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
    
    # initialize all relevant paramenters        
    nx = gridx.nx  # number of grid points
    
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx , dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld2 = phi0.copy()
    # For CTCS you need also to initialize phi1 , use FTBS
    phiOld1 = FTBS (gridx, phi0, c , 1)    
    
    
    # Loop over time steps t = 1,..(tsteps)  (total of tsteps-1 elements)
    for it in range(1,tsteps):  
        # Loop CTCS over space (excluding end points)
        for ix in range(1,nx-1):
            phi[ix] = phiOld2[ix] - c * ( phiOld1[ix+1] - phiOld1[ix-1] )
        # Update values at end points
        phi[0] = phiOld2[0] -  c * (phiOld1[1] - phiOld1[-2])
        phi[-1] = phi[0]
        # Update old time value 
        phiOld2 = np.copy(phiOld1)
        phiOld1 = np.copy(phi)
            
            
    return(phi)
        
