#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:42:47 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


def main():
    
    
    # FTCS scheme with periodic boundaries 
    def FTCS ( phi0, c , nt): 
        
        if (phi0[0] != phi0[-1]):
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
            
            
        return(phi)
        
    # Set the space grid
    Nx = 100                    # Number of points from x=0 to x=1 inclusive
    Length=1
    x = np.linspace(0,Length,Nx)     # Points in the x direction
    
    # Initial conditions for dependent variable phi 
    f_0 = where(x>0.25, 1, 0 ) - where(x>0.75, 1, 0 )
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, f_0, label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()
    
    
    
    c = 0.3
    
    # Call  FTCS 
    
    t4 = 50
    f4_FTCS = FTCS ( f_0, c , t4 )
    
    # Plot result
    plt.clf()
    plt.ion()
    plt.plot(x, f4_FTCS, label="Profile at time t = %g" %t4 , color = 'orange')
    plt.legend(loc="best")
    plt.title("FTCS scheme for Linear Advection, Courant c = %g" %c)
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()

    
        
        
        
main()