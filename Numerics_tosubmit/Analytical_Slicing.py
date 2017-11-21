#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:00:23 2017

@author: es3017
"""
## This function computes the analytical solution for the linear advection eq,
## given an initial condition. 

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin


SMALL = 1e-10

def Analytical_Periodic ( phi_0 , c, tsteps , grid , plotting=0 ):
        # phi0 = initial condition
        # c = courant number
        # t = time steps
        # gridx = x grid pbject
    
        
        if np.abs(phi_0[0] - phi_0[-1])> SMALL :
            print('Careful: your c.i. PhiO does not have periodic boundaries')
    
        nx = grid.nx
        dx = grid.dx
        
        # ALTERNATIVE
        x_b_INDEX = int(round(((c*tsteps*grid.dx)%grid.length) / dx))+1
        if x_b_INDEX == 1:
            
            PHI_t_2nd = list(phi_0[:-1])
            PHI_T = [phi_0[-2] ] + PHI_t_2nd
        else:
            
            PHI_t_2nd = list(phi_0 [1:-x_b_INDEX+1])
            PHI_t_1st = list (phi_0 [-x_b_INDEX :]  )
            PHI_T = PHI_t_1st +  PHI_t_2nd 
            
        if plotting != 0:
            
            x = np.linspace(0,grid.length,grid.nx)
            plt.clf()
            plt.ion()
            plt.plot( x, PHI_T  , 'b-', \
                     label = "Analytical function after time steps=%g" %tsteps)
            plt.plot( x, phi_0 , color='black',label = "Initial conditions" )
            plt.legend(loc="best")
            plt.title ("Linear advection with c=%g " %c)
            plt.show()
        
       
        return( PHI_T)
        

    