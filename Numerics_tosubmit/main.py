#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:08:12 2017

@author: es3017
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import where, cos, pi , sin

# use exec for grid.py and InitialConditions.py because in 
# this way python re-read the file
exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
import Analytical 
import CTCSAlone
import CTBSAlone
import FTCSAlone

def main():
    
    

    # Set the space grid using Grid class
    gridx = Grid( 100 , 1.0 )
    dx = gridx.dx 
    x = gridx.x   # Points in the x direction
    
    
    # Initial conditions for dependent variable phi 
    
    bell = cosBell(x)
    square = squareWave(x, 0.2 , 0.5 )
    k=5 # wave number of sine function
    sines = sine (x, k , 2.0)
    
    
    # non smooth at x=0.5
    f_0 = where(x<0.5, 0.5*(1-cos(4*pi*x)),0 )
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, f_0, color='black', label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-0.2,1.2])
    plt.show()
    
    # Time step and Courant number
    Nt = 60
    c = 0.3
    
    # Call Analytical solution with periodic boundaries
    f_Analytical = Analytical.Analytical_Periodic ( f_0 , c, Nt, Length , 0 )
    
    # Call CTBS method with periodic boundaries   
    f_CTBS = CTBSAlone.CTBS ( f_0 , c , Nt ,Length , 0  )
    
    # Call CTCS method with periodic boundaries    
    f_CTCS = CTCSAlone.CTCS ( f_0 , c, Nt ,Length , 0  )
    
    # Call CTBS method with periodic boundaries   
    f_FTCS = FTCSAlone.FTCS ( f_0 , c, Nt ,Length , 0  )

    # Plot all together
    plt.clf()
    plt.ion()
    plt.plot( x, f_CTCS , color='orange', label = "CTCS")
    plt.plot( x, f_FTCS , color='pink', label = "FTCS")
    plt.plot(x, f_Analytical, color='blue', label="Analytical")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([ min(f_0)-0.2 , max(f_0)+0.2])
    plt.title("Linear advection schemes with c=%g at time t=%g" %(c,Nt) )
    plt.show()
    
    
    
    # Smooth function for CTBS
    
    u_0 = sin ( 2 * pi * x)
    
    # Plot initial conditions
    plt.clf()
    plt.ion()
    plt.plot(x, u_0, color='black' , label="Initial conditions")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([-1.0,1.0])
    plt.show()
    
    # Call Analytical solution with periodic boundaries
    u_Analytical = Analytical.Analytical_Periodic ( u_0 , c, Nt, Length , 0 )
    
    # Call CTBS method with periodic boundaries   
    u_CTBS = CTBSAlone.CTBS ( u_0 , c , Nt ,Length , 0  )
    
    # Call CTCS method with periodic boundaries    
    u_CTCS = CTCSAlone.CTCS ( u_0 , c, Nt ,Length , 0  )
    
    # Call CTBS method with periodic boundaries   
    u_FTCS = FTCSAlone.FTCS ( u_0 , c, Nt ,Length , 0  )

    # Plot all together
    plt.clf()
    plt.ion()
    plt.plot( x, u_CTBS , color='green', label = "CTBS")
    plt.plot( x, u_CTCS , color='orange', label = "CTCS")
    plt.plot( x, u_FTCS , color='pink', label = "FTCS")
    plt.plot(x, u_Analytical, color='blue', label="Analytical")
    plt.legend(loc="best")
    plt.axhline(0, linestyle=':',color='black')
    plt.ylim([ min(u_0)-0.2 , max(u_0)+0.2])
    plt.title("Linear advection schemes with c=%g at time t=%g" %(c,Nt) )
    plt.show()
    
    
    
main()