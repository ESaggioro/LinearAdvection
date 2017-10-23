#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:09:03 2017

@author: es3017
"""
# This code is to write function for advenction schemes FTCS, CTBS and CTCS
# for Linear Advection Equation Phi_t + u Phi_x = 0  
# c= u dx / dt  u= velocity of advection


import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


def main():
    
    
    # FTCS scheme with periodic boundaries 
    def FTCS ( phi0, c , nt): 
        
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
            
            
        return(phi)
    
    
    # CTBS scheme with periodic boundaries 
    def CTBS ( phi0, c , nt): 
        
        if np.abs(phi0[0] -phi0[-1])> 10**(-10):
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
    
        # CTCS scheme with periodic boundaries 
    def CTCS ( phi0, c , nt): 
        
        if np.abs(phi0[0] -phi0[-1])> 10**(-10):
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
        
    def Analytical_Periodic ( phi_0 , c, t, Lx , plotting=0 ):
        # Input Lx = Length of x 
        
        if np.abs(phi_0[0] -phi_0[-1])> 10**(-10):
            print('Careful: your c.i. PhiO does not have periodic boundaries')
        
        # Calculate u wave velocity
        nx = len(phi_0)
        dx = Lx / nx
        dt = 1
        u = c * dx / dt
        
        # how many Lx has the wave passed
        alpha = int( u*t/Lx ) 
        
        # where is the first point after t time steps
        x_b = u*t - alpha*Lx
        x_b_index = int(x_b * nx / Lx)
        
        # Update phi by slicing and glueing correctly
        last = phi_0[-x_b_index]
        phi_t_1st = list(phi_0[-x_b_index:])
        phi_t_2nd= list(phi_0[1:nx-x_b_index])
        
        phi_t =  phi_t_1st + phi_t_2nd + [last]
        
        
        if plotting != 0:
            plt.clf()
            plt.ion()
            plt.plot( x, phi_t , 'b-', label = "Analytical function at time t=%g" %t)
            plt.plot( x, phi_0 , color='black',label = "Initial conditions" )
            plt.legend(loc="best")
            plt.title ("Linear advection with c=%g " %c)
            plt.show()
        
       
        return(phi_t)
    
    
    # Set the space grid
    Nx = 100                    # Number of points from x=0 to x=1 inclusive
    Length=1
    x = np.linspace(0,Length,Nx)     # Points in the x direction
    
    # Initial conditions for dependent variable phi 
    f_0 = where(x<0.5, 0.5*(1-cos(4*pi*x)),0 )
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, f_0, color='black', label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()
    
    Nt = 60
    c = 0.3
    
    # Call Analytical solution with periodic boundaries
    
    f_Analytical = Analytical_Periodic ( f_0 , c, Nt, Length , 0 )
    
    # Call FTCS
    
    f_FTCS = FTCS ( f_0, c , Nt)
    # Plot result
    plt.clf()
    plt.ion()
    plt.plot(x, f_FTCS, color='orange',label="Profile at time t = %g" %Nt )
    plt.plot( x , f_Analytical, 'b-',label = "Analytical" )
    plt.legend(loc="best")
    plt.title("FTCS scheme for Linear Advection, Courant c = %g" %c)
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()
    
    # FOR CTBS CONDITIONS HAS TO BE SMOOTH ??
    
    u_0 = sin ( 2 * pi * x)
    
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, u_0, color='black' , label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-1.0,1.0])
    plt.show()
    
    
    u_Analytical = Analytical_Periodic ( u_0 , c, Nt, Length , 0 )
    
    # Call  CTBS 
    
    u_CTBS = CTBS ( u_0, c ,Nt )
    # Plot result
    plt.clf()
    plt.ion()
    plt.plot(x, u_CTBS, color='orange',label="Profile at time t = %g" %Nt )
    plt.plot( x , u_Analytical, 'b-',label = "Analytical" )
    plt.legend(loc="best")
    plt.title("CTBS scheme for Linear Advection, Courant c = %g" %c)
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-1.0,1.0])
    plt.show()
        
        
    # NOW ADD PLOT OF EXACT SOLUTION and 2 schemes together


main()