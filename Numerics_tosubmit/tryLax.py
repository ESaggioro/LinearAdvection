#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:55:25 2017

@author: es3017
"""

# This function is the first attempt to see my implemetation of Lax Wendroff 

import numpy as np
import matplotlib as plt


exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Plot.py").read()) 
exec(open("./LaxWendroff.py").read()) 
exec(open("./CTCS.py").read()) 



exec(open("./Errors.py").read())

def main():
    
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations. 
    ##Thus grid.dx and grid.x will automatically be defined
    L = 1.0
    Nx =  100
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
    
    
    # Cosbell wave and analytical solutions 
    phi0 = cosBell(x,L)
    phiExact = Analytical(cosBell , gridx, c, Nt, L ) 
    
    # Lax Weendroff scheme for advection
    phi_Lax = LaxWendroff ( gridx, phi0, c , Nt )
    
    
    # Error of Lax    
    error = l2_norm (phi_Lax , phiExact)
    print('log Error lax=', np.log10(error))
    
    # Lax Weendroff scheme for advection
    phi_CTCS = CTCS ( gridx, phi0, c , Nt )
    
    errorCTCS = l2_norm (phi_CTCS , phiExact)
    print('log Error CTCS=', np.log10(errorCTCS))
   
    # The plot:
    plt.plot(x, phi_Lax,'m', label='Lax')
    plt.plot(x, phiExact ,'k--', label = 'Analytic')
    plt.plot(x, phi_CTCS , color='orange', linestyle='-', label = 'CTCS')
    plt.legend()
    plt.show()
    
    
    
    
    #  Sqaure wave and analytical solutions for various dx-resolutions
    phi0_Q = squareWave(x,0.4,0.7)
    phiExact_Q = Analytical(squareWave, gridx, c, Nt ,  0.4,0.7) 
    
    
    # Lax Weendroff scheme for advection
    phi_Lax_Q = LaxWendroff ( gridx, phi0_Q, c , Nt )
    
    
    # Error of Lax    
    error_Q = l2_norm (phi_Lax_Q , phiExact_Q)
    print('log Error lax=', np.log10(error_Q))
    
    # Lax Weendroff scheme for advection
    phi_CTCS_Q = CTCS ( gridx, phi0_Q, c , Nt )
    
    errorCTCS_Q = l2_norm (phi_CTCS_Q , phiExact_Q)
    print('log Error CTCS=', np.log10(errorCTCS_Q))
    
    # The plot:
    plt.plot(x, phi_Lax_Q, 'm', label='Lax')
    plt.plot(x, phiExact_Q , 'k--',label = 'Analytic')
    #plt.plot(x, phi_CTCS_Q ,color='orange', linestyle='-', label = 'CTCS')
    plt.legend()
    plt.show()
    
    
    
    
    
main()