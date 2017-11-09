#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:59:47 2017

@author: es3017
"""

import numpy as np


# CTCS scheme fro linear advection with periodic boundaries 
# Accuracy : 2 - 2
# Stability : c in [-1,1]

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def CTCS ( gridx, phi0, c , nt , T ): 
    "Linear advection of initial profile phi0 using CTCS, Courant number c"
    "for nt time-steps which cover a total time T"
    # gridx = the grid object
    # phi0 = initial contition
    # c = courant number
    # Nt = number of time steps
    # T = physical time 
    
    # Note: choosing T,c,Nt,gridx.dx means you have determined U and dt
        
    if np.abs(phi0[0] -phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
    
    # initialize all relevant paramenters        
    nx = gridx.nx  # number of grid points
    # dt = T / nt # width of single time step ( ie time resolution)
    
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx , dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld2 = phi0.copy()
        
    # For CTCS you need also to initialize phi1 
    # Create phiOld1 and initialize it to phi1=f (phi0) 
    # via FTCS
    phiOld1 = np.zeros(nx , dtype=float)
    for ix in range(1, nx-1):
        phiOld1[ix] = phiOld2[ix] - 0.5 * c * (phiOld2[ix+1] - phiOld2[ix-1])
    # Update values at end points ([0] and [nx-1])
    phiOld1[0] = phiOld2[0] -  0.5 * c * (phiOld2[1] - phiOld2[nx-2])
    phiOld1[nx-1] = phiOld1[0]
        
    # Loop over time steps t = 1,..(nt)  (total of nt-1 elements)
    for it in range(1,nt):  
            # Loop CTCS over space (excluding end points)
        for ix in range(1,nx-1):
            phi[ix] = phiOld2[ix] - c * ( phiOld1[ix+1] - phiOld1[ix-1] )
            # Update values at end points
        phi[0] = phiOld2[0] -  c * (phiOld1[1] - phiOld1[nx-2])
        phi[nx-1] = phi[0]
            # Update old time value 
        phiOld2 = phiOld1.copy()
        phiOld1 = phi.copy()
            
            
    return(phi)
        
