#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:09:46 2017

@author: es3017
"""
## This function is the main that I use to solve and analyse 
# the linear advection problem

import numpy as np

exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical.py").read())
exec(open("./Plot.py").read()) 
exec(open("./CTCS.py").read()) 
exec(open("./FTBS.py").read()) 
exec(open("./FTFS.py").read())
exec(open("./UPWIND.py").read())

def main():
    
    ## Declare an instance of the Grid class, called grid which    ###
    ## defines the grid for these simulations. 
    ##Thus grid.dx and grid.x will automatically be defined
    gridx = Grid( 100 , 1.0 )
    x = gridx.x
    
    # Define the time paramenter and Courant number
    Nt = 110 # NUmber of time steps
    T = 40  # Physical time
    c = 0.3
    
    # Consequent paramenters
    dt = float(T / Nt)
    U = c * dt / gridx.dx
    
    # Some initial conditions and their analytical solutions
    phi0_Square , phiSquare = Analytical( squareWave , gridx , c , Nt , T , 0.3 , 0.7)
    phi0_Sine ,phiSine = Analytical( sine , gridx , c , Nt , T , 4 , 1)
    phi0_Bell ,phiBell = Analytical( cosBell , gridx , c , Nt , T )    
    
    ##plot_Final(gridx, [phiSine, phiSquare, phiBell] , \
                ##["sine", "square", "bell"], 'analytical_advection.png' )
    
    
    # CTCS scheme for three initial conditions
    Ctcs_Square = CTCS ( gridx, phi0_Square , c , Nt , T )
    ##plot_Final(gridx, [Ctcs_Square, phiSquare] , \
                ##["CTCS scheme", "Analytical"], 'CTCS_square_advection.png' )
    
    Ctcs_Sine = CTCS ( gridx, phi0_Sine , c , Nt , T )
    ##plot_Final(gridx, [Ctcs_Sine, phiSine] , \
                ##["CTCS scheme", "Analytical"], 'CTCS_sine_advection.png' )
    
    Ctcs_Bell = CTCS ( gridx, phi0_Bell , c , Nt , T )
    ##plot_Final(gridx, [Ctcs_Bell, phiBell] , \
                ##["CTCS scheme", "Analytical"], 'CTCS_bell_advection.png' )
    
    
    
    # FTBS scheme for three initial conditions
    Ftbs_Square = FTBS ( gridx, phi0_Square , c , Nt , T )
    ##plot_Final(gridx, [Ftbs_Square, phiSquare] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_square_advection.png' )
    
    Ftbs_Sine = FTBS ( gridx, phi0_Sine , c , Nt , T )
    ##plot_Final(gridx, [Ftbs_Sine, phiSine] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_sine_advection.png' )
    
    Ftbs_Bell = FTBS ( gridx, phi0_Bell , c , Nt , T )
    ##plot_Final(gridx, [Ftbs_Bell, phiBell] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_bell_advection.png' )
    
    
    
    # FTFS scheme for three initial conditions
    Ftfs_Square = FTFS ( gridx, phi0_Square , c , Nt , T )
    ##plot_Final(gridx, [Ftfs_Square, phiSquare] , \
                ##["FTFS scheme", "Analytical"], 'FTFS_square_advection.png' )
    
    Ftfs_Sine = FTFS ( gridx, phi0_Sine , c , Nt , T )
    ##plot_Final(gridx, [Ftfs_Sine, phiSine] , \
            ##["FTFS scheme", "Analytical"], 'FTFS_sine_advection.png' )

    Ftfs_Bell = FTFS ( gridx, phi0_Bell , c , Nt , T )
    ##plot_Final(gridx, [Ftfs_Bell, phiBell] , \
                ##["FTFS scheme", "Analytical"], 'FTFS_bell_advection.png' )
                
    
    # UPWIND scheme for three initial conditions
    Upwind_Square = UPWIND ( gridx, phi0_Square , c , Nt , T )
    plot_Final(gridx, [Upwind_Square, phiSquare] , \
              ["UPWIND scheme", "Analytical"], 'UPWIND_square_advection.png' )
    
    
    
    
main()