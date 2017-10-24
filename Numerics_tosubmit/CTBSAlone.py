#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:59:13 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin
from copy import deepcopy

# CTBS scheme with periodic boundaries 
def CTBS ( phi0, c , nt , Length, plotting=0): 
        
        if np.abs(phi0[0] -phi0[-1])> 10**(-10):
            print('Careful: your c.i. PhiO does not have periodic boundaries')
            
        nx = len(phi0) 
        # Create the function phi(t) and initialize to 0
        phi = np.zeros(nx , dtype=float) 
        # Create phiOld and initialize it to phi0
        
        #phi0copy= list(phi0)[:]
        phiOld2 = phi0.copy()
        
        # For CTBS you need also to initialize phi1 
        # Create phiOld1 and initialize it to phi1=f (phi0) 
        # via FTCS
        phiOld1 = np.zeros(nx , dtype=float)
        for ix in range(1, nx-1):
            phiOld1[ix] = phiOld2[ix] - 0.5 * c * (phiOld2[ix+1] - phiOld2[ix-1])
        # Update values at end points
        phiOld1[0] = phiOld2[0] -  0.5 * c * (phiOld2[1] - phiOld2[nx-2])
        phiOld1[nx-1] = phiOld1[0]
        
        # Loop over time steps t = 2,..nt
        for it in range(2,nt):  # it= 2,.., nt-1 (total of nt-2 elements)
            # Loop over space (excluding end points, [0] and [nx-1])
            for ix in range(1,nx-1):
                phi[ix] = phiOld2[ix] - 2 * c * ( phiOld1[ix] - phiOld1[ix-1] )
            # Update values at end points
            phi[0] = phiOld2[0] -  2 * c * (phiOld1[0] - phiOld1[nx-2])
            phi[nx-1] = phi[0]
            # Update old time value 
            phiOld2 = phiOld1.copy()
            phiOld1 = phi.copy()
            
        # Plot if required
        
        if plotting != 0:
            
            x = np.linspace(0,Length,nx)
            plt.clf()
            plt.ion()
            plt.plot( x, phi , color='green', label = "CTBS at time t=%g" %nt)
            plt.plot( x, phi0 , color='black',label = "Initial conditions" )
            
            plt.ylim([min(phi0),max(phi0)])
            plt.legend(loc="best")
            plt.title ("CTBS for linear advection with c=%g " %c)
            plt.show()
            
        return(phi)
        
