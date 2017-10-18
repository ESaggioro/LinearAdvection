#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:10:23 2017

@author: es3017
"""
### Simple numerical scheme for 1D linear advection 
### FTCS scheme
### Non exendible code---rethink in terms of functions and objects

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi


# Set the grid
nx = 61                   # Number of points from x=0 to x=1 inclusive
nt = 50                   # Number of time-steps
c = 0.3                   # Courant number = u dx / dt  u= velocity of advection
x = np.linspace(0,1,nx)     # Points in the x direction

# Initial conditions for dependent variable phi 
phi = where(x<0.5, 0.5*(1-cos(4*pi*x)),0 )
phiOld = phi.copy()

# Plot initial conditions
plt.clf()
plt.ion()
plt.plot(x, phi, label="Initial conditions")
plt.legend(loc="best")
plt.axhline(0, linestyle=':',color='black')
plt.ylim([-0.2,1.2])
plt.show()

input('Press return to start simulation')

# Start FT CS numerical to evolve the initial function
# Loop over time steps
for it in range(nt):
    # Loop over space (excluding end points )
    for ix in range(1,nx-1):
        phi[ix] = phiOld[ix] - 0.5 * c * (phiOld[ix+1] - phiOld[ix-1])
        
    phi[0] = phiOld[0] -  0.5 * c * (phiOld[1] - phiOld[nx-2])
    phi[nx-1] = phi[0]

    
    # Update old time value
    phiOld = phi.copy()
    
    # Check plots
    if it in [2,10,20,30,49]:
        
        # Plot result
        plt.clf()
        plt.ion()
        plt.plot(x, phi, label="Profile at time"+str(it) )
        plt.legend(loc="best")
        plt.title("FTCS scheme for Linear Advection, Courant c = %g" %c)
        plt.axhline(0, linestyle=':',color='black')
        plt.ylim([-0.2,1.2])
        plt.show()

    
    
    