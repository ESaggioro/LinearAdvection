#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:02:06 2017

@author: es3017
"""

import numpy as np
import matplotlib as plt

# This function is a first attempt to see in Mass Variance function works

exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./Analytical_Slicing.py").read())
exec(open("./LaxWendroff.py").read()) 
exec(open("./CTCS.py").read()) 
exec(open("./FTBS.py").read())
exec(open("./MassVariance.py").read())
exec(open("./Plot.py").read())



def main():
    
    # Set the grid
    nx = 40
    L = 1.0 # (meters)
    Gridx = Grid (nx,L)
    
    # Set T , c , Time steps
    c = 0.5
    T = 100 # (seconds)
    tsteps = T * 1
    
    dt =np.float64( T / tsteps)
    u = c * Gridx.dx / dt
    print( ' u = ', u)
    
    # time intervals you want to compute:
    interval = [ int(i*T/10) for i in range(1,11)]
    # M and V for every interval and every scheme
    MExact=[0.0 for i in interval]
    MFTBS=[0.0 for i in interval]
    MCTCS=[0.0 for i in interval]
    MLAX=[0.0 for i in interval]
    
    VExact=[0.0 for i in interval]
    VFTBS=[0.0 for i in interval]
    VCTCS=[0.0 for i in interval]
    VLAX=[0.0 for i in interval]
    
    # Cosbell function evolved with 3 schemes and Exact solution
    phi0 = cosBell ( Gridx.x , L) # initial condition
    M0 = Mass (phi0 , Gridx.dx) # initial Mass
    V0 = Variance (phi0 , Gridx.dx) # initial Variance
    
    for j,ts in enumerate(interval): # M and V at different times
        phiExact = Analytical_Periodic (phi0 , c, ts , Gridx) # Exact solution
    
        phiFTBS = FTBS (Gridx, phi0, c , ts) # FTBS sceheme
        phiCTCS = CTCS (Gridx, phi0, c , ts)  # CTCS sceheme
        phiLAX = LaxWendroff ( Gridx, phi0, c , ts ) # LaxWendroff scheme
    
        # Compute Mass after tsteps
        MExact[j] = Mass(phiExact , Gridx.dx)
        MFTBS[j] = Mass(phiFTBS , Gridx.dx)
        MCTCS[j] = Mass(phiCTCS , Gridx.dx)
        MLAX[j] = Mass (phiLAX , Gridx.dx)
    
        # Compute Variance after tsteps
        VExact[j] = Variance(phiExact , Gridx.dx)
        VFTBS[j] = Variance(phiFTBS , Gridx.dx)
        VCTCS[j] = Variance(phiCTCS , Gridx.dx)
        VLAX[j] = Variance (phiLAX , Gridx.dx)
    
    # plot outuput values
    
    plot_MassVariance (interval, \
                       [MExact, MFTBS, MCTCS,  MLAX] ,\
                       [VExact, VFTBS, VCTCS,  VLAX] , \
                       ['k','blue', 'orange', 'm'],\
                       ['Exact', 'FTBS', 'CTCS', 'LAX'],\
                       'MassConservation.pdf', 'VarianceConservation.pdf')
    
    phiE60 = Analytical_Periodic (phi0 , c, 60 , Gridx)
    phiE80 = Analytical_Periodic (phi0 , c, 80 , Gridx)
    
    phiE100 = Analytical_Periodic (phi0 , c, 100 , Gridx)
    
    plt.plot(Gridx.x, phiE60, label='t=60' )
    plt.plot(Gridx.x, phiE80, label='t=80' )
    plt.plot(Gridx.x, phiE100, label='t=100' )

    
    
    
    
    


main()
    
    