#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:58:32 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin



    
    
    # FTCS scheme with periodic boundaries 
def FTCS ( phi0, c , nt, Length, plotting=0): 
    "Linear advection of profile in phiOld using FTCS, Courant number c"
    "for nt time-steps"
    
    name = "FTCS"
    if np.abs(phi0[0] -phi0[-1])> 10**(-10):
        print('Careful: your c.i. PhiO does not have periodic boundaries')
            
    nx = len(phi0) 
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx,dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld = phi0.copy()
        
    # Loop over time steps
    for it in range(nt):
        # Loop over space (excluding end points, [0] and [nx-1])
        for ix in range(1,nx-1):
            phi[ix] = phiOld[ix] - 0.5 * c * (phiOld[ix+1] - phiOld[ix-1])
        # Update values at end points
        phi[0] = phiOld[0] -  0.5 * c * (phiOld[1] - phiOld[nx-2])
        phi[nx-1] = phi[0]
        # Update old time value
        phiOld = phi.copy() 
            
    if plotting != 0:
            
        x = np.linspace(0,Length,nx)
        plt.clf()
        plt.ion()
        plt.plot( x, phi , color='pink', label = name+" at time t=%g" %nt)
        plt.plot( x, phi0 , color='black',label = "Initial conditions" )
        plt.legend(loc="best")
        plt.title (name+" for linear advection with c=%g " %c)
        plt.show()
            
            
            
    return(phi)
