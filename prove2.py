#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:51:20 2017

@author: es3017
"""

## Plot ANALYTICAL SOLUTION OF LINEAR ADVECTION EQUATION
## f(x,t) = f0 ( x- ut )
## WITH PERIODIC BOUNDARY CONDITION!!!


import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi


def main():
    
    
    
    # Set the space grid
    Nx = 40                    # Number of points from x=0 to x=1 inclusive
    Length=1.0
    x = np.linspace(0,Length,Nx)     # Points in the x direction
       
    # Initial conditions for dependent variable  
    f_0 = where(x<0.5, 0.5*(1-cos(4*pi*x)),0 )
    
    u_0 = where (x<0.25, 1,0 ) - where (x<0.75, 1,0 )
    
    q_0 = np.sin(4*pi*x)
    #q_0[-1]=0
    
    # Function evolved ad time t 
    
    
    # Phi(x,t)=Phi(x-ut,0) with periodic boundaries
    
    def Analytical_Periodic_piecewise0 ( phi_0 , c, t, Lx ):
        # Input Lx = Length of x 
        
        # Calculate u wave velocity
        nx = len(phi_0)
        dx = Lx / nx
        dt = 1
        u = c * dx / dt
        
        # how many Lx has the wave passed
        alpha = int( u*t/Lx ) 
        print("alpha=%g \n" %alpha)
        
        x_b = u*t - alpha*Lx
        print("x_b=ut-alpha*L=%g \n" %x_b)
        
        x_b_index = int(x_b * nx / Lx) 
        print("x_b index=%g" % x_b_index  )
        last = phi_0[-x_b_index]
        phi_t_1st = list(phi_0[-x_b_index:])
        phi_t_2nd= list(phi_0[1:nx-x_b_index])
        
        print(len(phi_t_1st))
        print(len(phi_t_2nd))
        
        phi_t =  phi_t_1st + phi_t_2nd + [last]
        print (len(phi_0), len(phi_t))
        
        plt.clf()
        plt.ion()
        plt.plot( x, phi_t , label = "Evolved function at time t=%g" %t)
        plt.plot( x, phi_0 , label = "Initial conditions" )
        plt.legend(loc="best")
        plt.title ("Linear advection with c=%g " %c)
        
        plt.show()
        
       
        return(phi_t)
        
    
    ##f_10 = Analytical_Periodic_piecewise0 ( f_0 , 0.3 , 10 , Length)
    ##f_50 = Analytical_Periodic_piecewise0 ( f_0 , 0.3 , 50 , Length)
    ##f_100 = Analytical_Periodic_piecewise0 ( f_0 , 0.3 , 100 , Length)
    ##f_200 = Analytical_Periodic_piecewise0 ( f_0 , 0.3 , 200 , Length)
    
    
    ##u_10 = Analytical_Periodic_piecewise0 ( u_0 , 0.3 , 10 , Length)
    ##u_50 = Analytical_Periodic_piecewise0 ( u_0 , 0.3 , 50 , Length)
    ##u_100 = Analytical_Periodic_piecewise0 ( u_0 , 0.3 , 100 , Length)
    ##u_200 = Analytical_Periodic_piecewise0 ( u_0 , 0.3 , 200 , Length)
    
    Analytical_Periodic_piecewise0 ( q_0 , 0.3 , 10 , Length)
    Analytical_Periodic_piecewise0 ( q_0 , 0.3 , 50 , Length)
    Analytical_Periodic_piecewise0 ( q_0 , 0.3 , 100 , Length)
    Analytical_Periodic_piecewise0 ( q_0 , 0.3 , 200 , Length)
    
    
    # See how the first point of the wave goes in time
    # it is trapped between 0 and 1
    ##q = 0.3 / Nx
    ##x_b_t = [q*t - int( q*t/Length )*Length for t in range(500)]  
    
    ##plt.clf()
    ##plt.ion()
    ##plt.plot([t for t in range(500)],x_b_t , marker='.',label=" x_b(t)")     
    
    
    # Plot phi_t vs phi_0    
    #plt.clf()
   #plt.ion()
    #plt.plot(x, f_0, label="Initial conditions")
    #plt.plot(x , f_t , label = "prova evoluzione t")
   # plt.legend(loc="best")
   # plt.axhline(0, linestyle=':',color='black')
    #plt.ylim([-0.2,1.2])
   # plt.show()
        
        
    

main()
    
    