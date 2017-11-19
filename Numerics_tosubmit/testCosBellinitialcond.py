#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:37:48 2017

@author: es3017
"""

# This function is to test if cosBell initial conditions behaves well.



exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Analytical_Slicing.py").read())


import matplotlib.pyplot as plt
import numpy as np

def main():
    
    # Set the grid
    nx = 50
    L = 1.0 # (meters)
    Gridx = Grid (nx,L)
    
    # Set T , c , Time steps
    
    c = 0.2
    T = 125 # (seconds)
    tsteps = T * 1
    
    dt =np.float64( T / tsteps)
    u = c * Gridx.dx / dt
    
    print( ' u = ', u)
    
    # test 
    
    
    
    cos0 , cosT = Analytical ( cosBell , Gridx , c, tsteps, L )
    plt.plot(Gridx.x , cosT, 'g--', linewidth=0.7,  label=T)
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.plot(Gridx.x , cos0, 'b--', linewidth=0.7 , label='CI')    
    plt.legend()
    plt.title('c=%g and nx=%g' %(c,nx))
    plt.show()
    
    print(Gridx.x)
    print(cos0)
    print(cosT)
    print(u*T/Gridx.dx)
    
    
    
    cosT_SLICE = Analytical_Periodic ( cos0 , c, tsteps , Gridx )
    plt.plot(Gridx.x , cosT_SLICE, 'g--', linewidth=0.7,  label='slice')
    plt.plot(Gridx.x , cosT, 'k--', linewidth=0.7,  label=T)
    plt.plot(Gridx.x , cos0, 'b--', linewidth=0.7 , label='CI') 
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.legend()
    plt.title('c=%g and nx=%g' %(c,nx))
    plt.show()
    
    
main()  