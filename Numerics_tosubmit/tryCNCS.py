#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:54:34 2017

@author: es3017
"""

# This function is the first attempt to see my implemetation of CNCS implicit

import numpy as np
import matplotlib as plt


exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./CNCS.py").read())
exec(open("./Analytical.py").read())
exec(open("./Plot.py").read()) 
exec(open("./Errors.py").read())

def main():
    
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations
    L = 1.0
    Nx =  50
    gridx = Grid( Nx , L ) 
    x = gridx.x 
    dx = gridx.dx 
    
    # Define the time paramenter and Courant number
    tsteps = 150
    c = 0.5 
    print('The Courant number chosen is c = ' , c)
    
    # Cosbell wave and analytical solutions 
    phi0 = cosBell(x,L)
    phi_Exact = Analytical( cosBell ,gridx, c, tsteps , L) 
    
    # CNCS scheme 
    phi_CNCS = CNCS ( gridx, phi0, c , tsteps )
    
    plt.plot(gridx.x , phi_CNCS, 'm', label='CNCS')
    plt.plot(gridx.x , phi_Exact, color='red', label='Exact')
    
    plt.legend()
    plt.show()
    
    
    # Error of CNCS    
    er_CNCS = l2_norm (phi_CNCS , phi_Exact)
    print('log Error CNCS=', np.log10(er_CNCS))
    
    
    


main()