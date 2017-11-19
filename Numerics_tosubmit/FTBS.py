#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 16:54:46 2017

@author: es3017
"""



import numpy as np


# FTBS scheme fro linear advection with periodic boundaries 
# Accuracy : 1 -1
# Stability : c in [0,1] 

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def FTBS ( gridx, phi0, c , nt): 
    "Linear advection of initial profile phi0 using FTBS, Courant number c"
    "for nt time-steps "
    
    # gridx = the grid object
    # phi0 = initial contition
    # c = courant number
    # Nt = number of time steps
    
        
    if np.abs(phi0[0] - phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
    
    # initialize all relevant paramenters        
    nx = gridx.nx  # number of grid points
    # dt = T / nt # width of single time step ( ie time resolution)
    
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx,dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld = phi0.copy()
        
    # Loop over time steps
    for it in range(nt):
        # Loop over space (excluding end points, [0] and [nx-1])
        for ix in range(1,nx-1):
            phi[ix] = phiOld[ix] -  c * (phiOld[ix] - phiOld[ix-1])
        # Update values at end points
        phi[0] = phiOld[0] -  c * (phiOld[0] - phiOld[nx-2])
        phi[nx-1] = phi[0]
        # Update old time value
        phiOld = phi.copy() 
        
    return(phi)