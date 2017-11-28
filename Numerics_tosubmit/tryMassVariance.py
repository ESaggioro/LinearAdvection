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
exec(open("./Analytical.py").read())
exec(open("./AdvectionSchemes.py").read())
exec(open("./MassVariance.py").read())
exec(open("./Plot.py").read())



def main():
    
    # Set the grid
    nx = 40
    L = 1.0 # (meters)
    Gridx = Grid (nx,L)
    
    # Set T , c , Time steps
    c = 0.3
    T = 100 # (seconds)
    tsteps = T * 1
    
    dt =np.float64( T / tsteps)
    u = c * Gridx.dx / dt
    print( ' u = ', u)
    
    # M and V for every scheme
    MExact = np.zeros(tsteps)
    MFTBS = np.zeros(tsteps)
    MCTCS = np.zeros(tsteps)
    MLAX = np.zeros(tsteps)
    MCNCS = np.zeros(tsteps)
    
    VExact = np.zeros(tsteps)
    VFTBS = np.zeros(tsteps)
    VCTCS = np.zeros(tsteps)
    VLAX = np.zeros(tsteps)
    VCNCS = np.zeros(tsteps)
    
    # Cosbell function 
    phi0 = cosBell ( Gridx.x , L) # initial condition
    M0 = Mass (phi0 , Gridx.dx) # initial Mass
    V0 = Variance (phi0 , Gridx.dx) # initial Variance
    
#    philoopF = np.copy(phi0)
#    philoopCT = np.copy(phi0)
#    philoopCN = np.copy(phi0)
#    philoopLA = np.copy(phi0)
#    
#    for t in range(1, tsteps+1): # M and V in time
#        
#        phiFTBS = FTBS (Gridx, philoopF, c , 1 ) # FTBS sceheme
#        phiCTCS = CTCS (Gridx, philoopCT, c , 2 )  # CTCS sceheme
#        phiLAX = LaxWendroff ( Gridx, philoopLA , c , 1 ) # LaxWendroff scheme
#        phiCNCS = CNCS (Gridx, philoopCN, c , 1 )  # CTCS sceheme
#         
#        # Compute Mass after t
#        MFTBS[t-1] = Mass(phiFTBS , Gridx.dx)
#        MCTCS[t-1] = Mass(phiCTCS , Gridx.dx)
#        MLAX[t-1] = Mass (phiLAX , Gridx.dx)
#        MCNCS[t-1] = Mass (phiCNCS , Gridx.dx)
#    
#        # Compute Variance after t
#        VFTBS[t-1] = Variance(phiFTBS , Gridx.dx)
#        VCTCS[t-1] = Variance(phiCTCS , Gridx.dx)
#        VLAX[t-1] = Variance (phiLAX , Gridx.dx)
#        VCNCS[t-1] = Variance (phiCNCS , Gridx.dx)
#        
#        # Update
#        philoopF = phiFTBS
#        philoopCT = phiCTCS 
#        philoopLA = phiLAX 
#        philoopCN = phiCNCS 
#        

    # plot outuput values
    
#    plot_MassVariance ( np.arange(1,tsteps+1), M0 , V0,  \
#                       [ MFTBS, MCTCS,  MLAX , MCNCS] ,\
#                       [ VFTBS, VCTCS,  VLAX, VCNCS] , \
#                       [ 'blue', 'orange', 'red' , 'm'],\
#                       [ 'FTBS', 'CTCS', 'LAX', 'CNCS' ],\
#                       'MassConservation.pdf', 'VarianceConservation.pdf')
 
# =============================================================================
#  Lax mass and variance strange behaviour   
# =============================================================================
#    C=[0.3, 0.5, 0.6, 0.8]
#    tt = 100
#    
#    
#    MLAX = [np.zeros(tsteps) for cc in C]
#    VLAX = [np.zeros(tsteps) for cc in C]
#    for i,cc in enumerate(C):
#        philoopLA = np.copy(phi0)
#        for t in range(1, tsteps+1):
#            phiLAX = LaxWendroff ( Gridx, philoopLA , cc , 1 ) 
#            MLAX[i][t-1] = Mass (phiLAX , Gridx.dx)
#            VLAX[i][t-1] = Variance (phiLAX , Gridx.dx)
#            
#            philoopLA = phiLAX 
#        
#        
#        
#    plot_MassVariance ( np.arange(1,tsteps+1), M0 , V0,  \
#                        MLAX  ,\
#                        VLAX , \
#                       ['blue',  'orange','red',  'magenta' ],\
#                       [  'c0.3', 'c0.5','c0.6','c0.8'],\
#                       'MassLax.pdf', 'VarianceLax.pdf')

# =============================================================================
#  CNCS mass and variance strange behaviour   
# =============================================================================
    C=[0.3, 0.5, 0.6, 0.8, 1.1]
    tt = 100
    

    MCNCS = [np.zeros(tsteps) for cc in C]
    VCNCS = [np.zeros(tsteps) for cc in C]
    for i,cc in enumerate(C):
        philoopCN = np.copy(phi0)
        for t in range(1, tsteps+1):
            phiCNCS = CNCS ( Gridx, philoopCN , cc , 1 ) 
            MCNCS[i][t-1] = Mass (phiCNCS , Gridx.dx)
            VCNCS[i][t-1] = Variance (phiCNCS , Gridx.dx)
            
            philoopCN = phiCNCS 
        
        
        
    plot_MassVariance ( np.arange(1,tsteps+1), M0 , V0,  \
                        MCNCS  ,\
                        VCNCS , \
                       ['blue',  'orange','red',  'magenta' , 'green'],\
                       [  'CNCS c0.3', 'c0.5','c0.6','c0.8', 'c1.1'],\
                       'MassCNCS.pdf', 'VarianceCNCS.pdf')

# =============================================================================
#  CTCS mass and variance strange behaviour   
# =============================================================================
    C=[0.3 , 0.5, 0.6, 0.8]
    tt = 100
    
    
    MCTCS = [np.zeros(tsteps-1) for cc in C]
    VCTCS = [np.zeros(tsteps-1) for cc in C]
    for i,cc in enumerate(C):
        
        philoopF = FTBS( Gridx, phi0 , cc , 1  )
        philoopCT = CTCS (Gridx, philoopF, cc , 1 , phi0 ) 
        philoopCT_Older = philoopF
        
        for t in range(2, tsteps+1):
            phiCTCS = CTCS ( Gridx, philoopCT , cc , 1 , philoopCT_Older ) 
            MCTCS[i][t-2] = Mass (phiCTCS , Gridx.dx)
            VCTCS[i][t-2] = Variance (phiCTCS , Gridx.dx)
            
            philoopCT_Older = philoopCT
            philoopCT = phiCTCS 
            
        
        
    plot_MassVariance ( np.arange(1,tsteps), M0 , V0,  \
                        MCTCS  ,\
                        VCTCS , \
                       ['blue',  'orange','red',  'magenta' ],\
                       [  'CTCS c0.3', 'c0.5','c0.6','c0.8'],\
                       'MassCTCS.pdf', 'VarianceCTCS.pdf')


main()
    
    