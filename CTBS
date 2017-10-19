#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:56:09 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi


def main():
    
    
   
    
    
    # CTBS scheme with periodic boundaries 
    def CTBS ( phi0, c , nt): 
        
        if (phi0[0] != phi0[-1]):
            print('Careful: your c.i. PhiO does not have periodic boundaries')
            
        nx = len(phi0) 
        # Create the function phi(t) and initialize to 0
        phi = np.zeros(nx,dtype=float) 
        # Create phiOld and initialize it to phi0
        phiOld2 = phi0.copy()
        # For CTBS you need also to initialize phi1 
        # Create phiOld1 and initialize it to phi1=f (phi0) 
        # via FTCS
        phiOld1 = np.zeros(nx,dtype=float)
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
            
            
        return(phi)
    
    
    
    
    # Set the space grid
    Nx = 100                    # Number of points from x=0 to x=1 inclusive
    Length=1
    x = np.linspace(0,Length,Nx)     # Points in the x direction
    
    # Initial conditions for dependent variable phi 
    f_0 = where(x<0.5, 0.5*(1-cos(4*pi*x)),0 )
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, f_0, label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()
    
    
    
    c = 0.3
    
    # Call  CTBS 
    
    for t in [3,5,10,15,20,25,30]:
        f_CTBS = CTBS ( f_0, c ,t )
        # Plot result
        plt.clf()
        plt.ion()
        plt.plot(x, f_CTBS, label="Profile at time t = %g" %t , color = 'orange')
        plt.legend(loc="best")
        plt.title("CTBS scheme for Linear Advection, Courant c = %g" %c)
        plt.axhline(0, linestyle=':',color='black')
        plt.ylim([-0.2,1.2])
        #plt.show()


    # Initial conditions for dependent variable u , v
    u_0 = where(0.3<x<0.6,1,0 )
    
    v_0 = cos(3*pi*x)
    

    
    

main()