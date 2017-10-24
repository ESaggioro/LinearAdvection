#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:00:23 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


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
            
            x = np.linspace(0,Lx,nx)
            plt.clf()
            plt.ion()
            plt.plot( x, phi_t , 'b-', label = "Analytical function at time t=%g" %t)
            plt.plot( x, phi_0 , color='black',label = "Initial conditions" )
            plt.legend(loc="best")
            plt.title ("Linear advection with c=%g " %c)
            plt.show()
        
       
        return(phi_t)
        

    