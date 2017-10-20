#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:16:03 2017

@author: es3017
"""

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
    
    
   
    
    
    # CTCS scheme with periodic boundaries 
    def CTCS ( phi0, c , nt): 
        
        if (phi0[0] != phi0[-1]):
            print('Careful: your c.i. PhiO does not have periodic boundaries')
            
        nx = len(phi0) 
        # Create the function phi(t) and initialize to 0
        phi = np.zeros(nx,dtype=float) 
        # Create phiOld and initialize it to phi0
        phiOld2 = phi0.copy()
        
        # For CTCS you need also to initialize phi1 
        # Create phiOld1 and initialize it to phi1=f (phi0) 
        # via FTCS
        phiOld1 = np.zeros(nx,dtype=float)
        for ix in range(1, nx-1):
            phiOld1[ix] = phiOld2[ix] - 0.5 * c * (phiOld2[ix+1] - phiOld2[ix-1])
        # Update values at end points ([0] and [nx-1])
        phiOld1[0] = phiOld2[0] -  0.5 * c * (phiOld2[1] - phiOld2[nx-2])
        phiOld1[nx-1] = phiOld1[0]
        
        # Loop over time steps t = 2,..(nt-1)  (total of nt-2 elements)
        for it in range(2,nt):  
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
    
    # Call  CTCS 
    
    t4 = 50
    f4_CTCS = CTCS ( f_0, c , t4 )
    
    # Plot result
    plt.clf()
    plt.ion()
    plt.plot(x, f4_CTCS, label="Profile at time t = %g" %t4 , color = 'orange')
    plt.legend(loc="best")
    plt.title("CTCS scheme for Linear Advection, Courant c = %g" %c)
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()

    

    
    

main()