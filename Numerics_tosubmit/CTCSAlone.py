#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:59:47 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin




# CTCS scheme with periodic boundaries 
def CTCS ( phi0, c , nt , Length, plotting=0): 
    "Linear advection of profile in phiOld using CTCS, Courant number c"
    "for nt time-steps"
        
    if np.abs(phi0[0] -phi0[-1])> 10**(-10):
        print('Careful: your c.i. PhiO does not have periodic boundaries')
            
    nx = len(phi0) 
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
        
        # Loop over time steps t = 1,..(nt-1)  (total of nt-2 elements)
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
            
            
    if plotting != 0:
            
        x = np.linspace(0,Length,nx)
        plt.clf()
        plt.ion()
        plt.plot( x, phi , color='orange', label = "CTCS at time t=%g" %nt)
        plt.plot( x, phi0 , color='black',label = "Initial conditions" )
        plt.ylim([min(phi0),max(phi0)])
        plt.legend(loc="best")
        plt.title ("CTCS for linear advection with c=%g " %c)
        plt.show()
            
            
    return(phi)
        
