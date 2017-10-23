#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 17:04:51 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


def main():
    
    
   
    
    
    # CTBS scheme with periodic boundaries 
    def CTBS ( phi0, c , nt, output_times): 
        
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
            
            if it in output_times:
                
                phi_An=Analytical_Periodic(phi0,c, it, 1  )
                plt.clf()
                plt.ion()
                plt.plot(x, phi, label="CTBS at time t = %g" %it)
                plt.plot(x, phi_An, label="Analytical at time t = %g" %it)
                plt.title("CTBS scheme for Linear Advection, Courant c = %g" %c)
                plt.legend(loc="best")
                plt.axhline(0, linestyle=':',color='black')
                plt.ylim([-1.0,1.0])
                plt.show()
                
            
            
        return(phi)
        
    def Analytical_Periodic ( phi_0 , c, t, Lx , plotting=0 ):
        # Input Lx = Length of x 
        
        if (phi_0[0] != phi_0[-1]):
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
            plt.plot( x, phi_t , label = "Analytical function at time t=%g" %t)
            plt.plot( x, phi_0 , label = "Initial conditions" )
            plt.legend(loc="best")
            plt.title ("Linear advection with c=%g " %c)
            plt.show()
        
       
        return(phi_t)
    
    
    
    
    # Set the space grid
    Nx = 100                    # Number of points from x=0 to x=1 inclusive
    Length=1
    x = np.linspace(0,Length,Nx)     # Points in the x direction

    # Initial conditions for dependent variable u 
    
    u_0 = sin ( 2 * pi * x)
    
    print ("Are boundaries periodic? : u_0[0]= ",u_0[0]," u_0[-1]= ",u_0[-1])
    if u_0[0] != u_0[-1]:
        print("No!")
    else:
        print("Yes!")
    
    # Set value at x= 2*pi to 0 , to overcome the finite precision of np.pi 
    for i,ui in enumerate(u_0):
        if (-1*10**(-15) < ui < 1*10**(-15)):
            u_0[i]=0
            
    print ("Are boundaries periodic now? : u_0[0]= ",u_0[0]," u_0[-1]= ",u_0[-1])
    if u_0[0] != u_0[-1]:
        print("No!")
    else:
        print("Yes!")
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, u_0, label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-1.0,1.0])
    plt.show()
    
   
    
    # Call  CTBS 
    
    #input('Press return to start simulation')
    
    Nt = 60
    t_output = [50]
    c = 0.3
    
    u_Nt = CTBS ( u_0, c , Nt, t_output ) 
    
    
    
    
    
    
    
    
    
    

    
    

main()