#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:11:48 2017

@author: es3017
"""

import numpy as np

exec(open("./FTBS.py").read()) 
exec(open("./FTFS.py").read())


# UPWIND scheme for linear advection with periodic boundaries 
# Accuracy : 1 - 1
# Stability : c in [-1,+1] 

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def UPWIND ( gridx, phi0, c , nt , T ): 
    "Linear advection of initial profile phi0 using FTFS or FTBS, \
    dependind on sign of Courant number c (negative: FTFS, positive : FTBS"
    "for nt time-steps which cover a total time T"
    
    # gridx = the grid object
    # phi0 = initial contition
    # c = courant number
    # Nt = number of time steps
    # T = physical time 
    
    # Note: choosing T,c,Nt,gridx.dx means you have determined U and dt
        
    if np.abs(phi0[0] - phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
    
    # initialize all relevant paramenters        
    nx = gridx.nx  # number of grid points
    # dt = T / nt # width of single time step ( ie time resolution)
    
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx,dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld = phi0.copy()
    
    if c>= 0:
        return( FTBS(gridx, phi0, c , nt , T ) )
        
    else :
        return( FTFS(gridx, phi0, c , nt , T ) )
        