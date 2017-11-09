#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:55:25 2017

@author: es3017
"""

## This function is the main that I use to solve and analyse 
# the linear advection problem

import numpy as np
import matplotlib as plt

exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Plot.py").read()) 
exec(open("./CTCS.py").read()) 
exec(open("./FTBS.py").read()) 
exec(open("./FTFS.py").read())
exec(open("./UPWIND.py").read())
exec(open("./L_norm_errors.py").read())

def main():
    
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations. 
    ##Thus grid.dx and grid.x will automatically be defined
    L = 1.0
    Nx = [ 2, 5 ,10 ,15, 20, 25, 30 , 50 , 100 ,150]
    gridx = [ Grid( n , L ) for n in Nx ] 
    x = [gridx[i].x for i in range(len(Nx)) ]
    
    # Define the time paramenter and Courant number
    Nt = 100 # Number of time steps 
    T = 40
    c = 0.3 
    
    # Consequent paramenters
    dt = float(T / Nt)
    # you haev U [i] = c * gridx[i].dx / dt
    
    # Square wave and analytical solutions for various dx-resolutions
    phi0_Square = [ np.zeros_like(x[0]) for n in Nx]
    phiSquare = [ np.zeros_like(x[0]) for n in Nx]
    alpha = 0.3
    beta = 0.7
    
    # L2 Errors
    
    Error_Square_CTCS = [0.0 for i in range(len(Nx))]
    Error_Square_FTBS = [0.0 for i in range(len(Nx))]
    
    Ctcs_Square = [ np.zeros_like(x[0]) for n in Nx]
    Ftbs_Square = [ np.zeros_like(x[0]) for n in Nx]
    
    for i in range(len(Nx)): # run over different grid resolution
        phi0_Square[i] , phiSquare[i] = \
        Analytical( squareWave , gridx[i] , c , Nt , T , alpha , beta )
        
        Ctcs_Square[i] = CTCS ( gridx[i], phi0_Square[i] , c , Nt , T )
        Ftbs_Square[i] = FTBS ( gridx[i], phi0_Square[i] , c , Nt , T )
        
        Error_Square_CTCS[i]=l2_norm (Ctcs_Square[i] , phiSquare[i])
        Error_Square_FTBS[i]=l2_norm (Ftbs_Square[i] , phiSquare[i])
     
    dx2 = [(gridx[i].dx)*(gridx[i].dx) for i in range(len(Nx)) ]
    dx = [gridx[i].dx for i in range(len(Nx)) ]
    
    
    plot_l2error( dx2, [ Error_Square_CTCS ] , \
                ["CTCS "],'Errors_squarefunction_CTCS.png', \
                title='$l_2$ norm error, $\phi$ square function', \
                xlabel='$(\Delta x)^2$' )
    
    plot_l2error( dx, [ Error_Square_FTBS ] , \
                ["FTBS "],'Errors_squarefunction_FTBS.png', \
                title='$l_2$ norm error, $\phi$ square function' , \
                xlabel='$(\Delta x)$ ')
    
    # Cosbell wave and analytical solutions for various dx-resolutions
    phi0_Bell = [ np.zeros_like(x[0]) for n in Nx]
    phiBell = [ np.zeros_like(x[0]) for n in Nx]
    
    # L2 Errors
    
    Error_Bell_CTCS = [0.0 for i in range(len(Nx))]
    Error_Bell_FTBS = [0.0 for i in range(len(Nx))]
    
    Ctcs_Bell = [ np.zeros_like(x[0]) for n in Nx]
    Ftbs_Bell = [ np.zeros_like(x[0]) for n in Nx]
    
    for i in range(len(Nx)): # run over different grid resolution
        phi0_Bell[i] , phiBell[i] = \
        Analytical( cosBell , gridx[i] , c , Nt , T  )
        
        Ctcs_Bell[i] = CTCS ( gridx[i], phi0_Bell[i] , c , Nt , T )
        Ftbs_Bell[i] = FTBS ( gridx[i], phi0_Bell[i] , c , Nt , T )
        
        Error_Bell_CTCS[i]=l2_norm (Ctcs_Bell[i] , phiBell[i])
        Error_Bell_FTBS[i]=l2_norm (Ftbs_Bell[i] , phiBell[i])
     
    dx2 = [(gridx[i].dx)*(gridx[i].dx) for i in range(len(Nx)) ]
    dx = [gridx[i].dx for i in range(len(Nx)) ]
    
    
    plot_l2error( dx2, [ Error_Bell_CTCS ] , \
                ["CTCS "],'Errors_Bellfunction_CTCS.png', \
                title='$l_2$ norm error, $\phi$ cosBell function', \
                xlabel='$(\Delta x)^2$' )
    
    plot_l2error( dx, [ Error_Bell_FTBS ] , \
                ["FTBS "],'Errors_squarefunction_FTBS.png', \
                title='$l_2$ norm error, $\phi$ cosBell function' , \
                xlabel='$(\Delta x)$ ')
    
    
    
    
        
        
    
main()