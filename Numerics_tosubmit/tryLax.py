#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:55:25 2017

@author: es3017
"""

## This function is the main that I use to analyse errors
# the linear advection problem

import numpy as np
import matplotlib as plt


exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Plot.py").read()) 
exec(open("./LaxWendroff.py").read()) 
exec(open("./CTCS.py").read()) 



exec(open("./L_norm_errors.py").read())

def main():
    
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations. 
    ##Thus grid.dx and grid.x will automatically be defined
    L = 1.0
    Nx =  320
    gridx = Grid( Nx , L ) 
    x = gridx.x 
    dx = gridx.dx 
    
    # Define the time paramenter and Courant number
    T = 40
    c = 0.3 
    print('The Courant number chosen is c = ' , c)
    
    # Ratio Nx/Nt
    d = 1
    Nt = int(d*Nx)
    
    U =  (c * dx / (T/Nt))
    
    print('The  physical velocity u = ' , U)
    
    
    # Cosbell wave and analytical solutions for various dx-resolutions
    phi0 , phiExact = Analytical ( cosBell , gridx , c, Nt )
    
    
    # Lax Weendroff scheme for advection
    phi_Lax = LaxWendroff ( gridx, phi0, c , Nt )
    
    plt.plot(x, phi_Lax, label='Lax')
    plt.plot(x, phiExact , label = 'Analytic')
    plt.legend()
    plt.show()
    
    # Error of Lax    
    error = l2_norm (phi_Lax , phiExact)
    print('log Error lax=', np.log10(error))
    
    # Lax Weendroff scheme for advection
    phi_CTCS = CTCS ( gridx, phi0, c , Nt )
    
    errorCTCS = l2_norm (phi_CTCS , phiExact)
    print('log Error CTCS=', np.log10(errorCTCS))
    
main()