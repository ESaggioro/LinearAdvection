#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:44:26 2017

@author: es3017
"""
#-----------------------------------------------------------------------------

## This function is the main that I use to analyse errors for
## the linear advection problem

#-----------------------------------------------------------------------------

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


#exec(open("./Analytical_Slicing.py").read())



def main():

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    ## SPACE-TIME GRID AND COURANT NUMBER DEFINITION    

    ## Define the physical total time T and Courant number c
    # YOU WILL WANT TO ASK (L,Nx) AS INPUT TO THE USER ---------- 
    T = 10
    print('The total time chosen is T = ' , T)
    c = 0.6 
    print('The Courant number chosen is c = ' , c)
    
    
    ## Define the space grid, using grid class, \
    ## giving L length and Nx number of grid points
    
    # YOU WILL WANT TO ASK (L,Nx) AS INPUT TO THE USER ---------- 
    L = 1.0
    Nx = [ 40,80,160,320, 400 ]
    print('The total length chosen is L = ' , L)
    print('The number of grid points are Nx = ' , Nx )
    
    ## Define d = Nt/Nx ratio
    # YOU WILL WANT TO ASK (L,Nx) AS INPUT TO THE USER ---------- 
    d = 3 
    print('The ratio d=Nt/Nx chosen is d = ' , d)
    
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------  
    
    # Consequent time paramenters
    Nt = [ n * int(d) for n in Nx] 
   
    # Consequent space paramenters
    gridx = [ Grid( n , L ) for n in Nx ] 
    x = [grid.x for grid in gridx ]
    dx = [grid.dx for grid in gridx ]
    
    print('The dx chosen are dxs = ' , dx)
   
    # Consequent velocity of the linear advection
    U = c * d* ( L / T)
    print('The physical velocity is u = ' , U)
    
  
    
    ## ERROR COMPUTATION ON THE CTCS AND FTBS NUMERICAL SCHEMES

    
    ## phi_0 and phi_exact initialized to 0-vectors, for the various x-grids
    phi0_s = [ np.zeros(n , dtype=float) for n in Nx]
    phiExact_s = [ np.zeros(n , dtype=float) for n in Nx] 
    
    ## Numerical solutions initialized to 0-vectors, for the various x-grids 
    Function_FTBS = [ np.zeros(n , dtype=float) for n in Nx]
    Function_CTCS = [ np.zeros(n , dtype=float) for n in Nx]
    
    ## Errors vectors initialized to 0 scalar, for the various x-grids
    Error_FTBS = [0.0 for i in range(len(Nx))]
    Error_CTCS = [0.0 for i in range(len(Nx))]
    Errorinfty_FTBS = [0.0 for i in range(len(Nx))]
    Errorinfty_CTCS = [0.0 for i in range(len(Nx))]
    
    
    
    
    
    # Con slice analytical
    #phiExact_Slice = [ np.zeros(n , dtype=float) for n in Nx]
    #Error_FTBS_Slice = [0.0 for i in range(len(Nx))]
    #Error_CTCS_Slice = [0.0 for i in range(len(Nx))]
    #Errorinfty_FTBS_Slice = [0.0 for i in range(len(Nx))]
    #Errorinfty_CTCS_Slice = [0.0 for i in range(len(Nx))]
        
   
    
    
    # Evolve for nt time steps the i.c. (set to bell function)
    # for Analytical, FTCB and CTCS. 
    # And compute error - norm
    for i,grid in enumerate(gridx): # run over different grid resolution
        print('Number of time steps=', Nt[i])
        phi0_s[i] , phiExact_s[i] = \
        Analytical( cosBell , grid , c , Nt[i] ,L )
        
        
        Function_CTCS[i]  = CTCS ( grid, phi0_s[i] , c , Nt[i] )
        Function_FTBS[i]  = FTBS ( grid, phi0_s[i] , c , Nt[i] )
        
        Error_CTCS[i]=l2_norm(Function_CTCS[i] ,phiExact_s[i])
        Error_FTBS[i]=l2_norm(Function_FTBS[i] ,phiExact_s[i])
        
        Errorinfty_CTCS[i]=linfty_norm(Function_CTCS[i] ,phiExact_s[i])
        Errorinfty_FTBS[i]=linfty_norm(Function_FTBS[i] ,phiExact_s[i])
        
        
        #Analytical con slicing
        #phiExact_Slice[i] =  Analytical_Periodic (phi0_s[i], c, Nt[i] ,grid  )
        #Error_CTCS_Slice[i]=l2_norm(Function_CTCS[i] ,phiExact_Slice[i])
        #Error_FTBS_Slice[i]=l2_norm(Function_FTBS[i] ,phiExact_Slice[i])
        
        #Errorinfty_CTCS_Slice[i]=linfty_norm(Function_CTCS[i] ,phiExact_Slice[i])
        #Errorinfty_FTBS_Slice[i]=linfty_norm(Function_FTBS[i] ,phiExact_Slice[i])
        
        
        
        
    # Fit the errors:
    # L2
    logdx = np.log10(dx)
    logerrCTCS = np.log10(Error_CTCS)
    logerrFTBS = np.log10(Error_FTBS)
    
    
    CTCSfit=np.polyfit(logdx,logerrCTCS, 1)
    FTBSfit=np.polyfit(logdx,logerrFTBS, 1)
    
    print('L2 errors:')
    print("Ctcs parameters = ", CTCSfit)
    print("Ftbs parameters = ", FTBSfit)
    
    # L infinity
    logerrCTCS_inf = np.log10(Errorinfty_CTCS)
    logerrFTBS_inf = np.log10(Errorinfty_FTBS)
    
    
    CTCSfit_inf=np.polyfit(logdx,logerrCTCS_inf, 1)
    FTBSfit_inf=np.polyfit(logdx,logerrFTBS_inf, 1)
    
    print('L infinity errors:')
    print("Ctcs parameters = ", CTCSfit_inf)
    print("Ftbs parameters = ", FTBSfit_inf)
    
    
    
    
    
    # PLOT L2
    plot_error( dx, [ Error_FTBS , Error_CTCS  ] , \
                ["FTBS ", "CTCS"],['blue' , 'orange'] ,\
                'L2_LogError_CTCSFTBS_c06.pdf', \
                title='$l_{2}$-norm errors for cosbell function c=%g'%c, \
                xlabel='$\Delta x$' )
    # Fit the errors SLICE analytical:
    #logerrCTCS_Slice = np.log10(Error_CTCS)
    #logerrFTBS_Slice = np.log10(Error_FTBS)
    
    
    #CTCSfit_Slice=np.polyfit(logdx,logerrCTCS, 1)
    #FTBSfit_Slice=np.polyfit(logdx,logerrFTBS_Slice, 1)
    
    #print("Ctcs parameters SLICE = ", CTCSfit_Slice)
    #print("Ftbs parameters SLICE = ", FTBSfit_Slice)
    
    #print("logErr_Ftbs SLICE = ", logerrFTBS_Slice)
    #print("logErr_CTCS SLICE = ", logerrCTCS_Slice)
    
    
    # PLOT ERROR Linfty
    plot_error( dx, [ Errorinfty_FTBS , Errorinfty_CTCS  ] , \
                ["FTBS ", "CTCS"],['blue' , 'orange'] ,\
                'Linfty_LogError_CTCSFTBS_c06.pdf', \
                title='$l_{\infty}$-norm errors for cosbell functionc=%g'%c, \
                xlabel='$\Delta x$' )
    # Fit the errors SLICE analytical:
    #logerrinftyCTCS_Slice = np.log10(Errorinfty_CTCS_Slice)
    #logerrinftyFTBS_Slice = np.log10(Errorinfty_FTBS_Slice)
    
    
    #CTCSfitinfty_Slice=np.polyfit(logdx,logerrinftyCTCS_Slice, 1)
    #FTBSfitinfty_Slice=np.polyfit(logdx,logerrinftyFTBS_Slice, 1)
    
    #print("Ctcs parameters infty = ", CTCSfitinfty_Slice)
    #print("Ftbs parameters infty = ", FTBSfitinfty_Slice)
    
    
    
    #for i in range(len(Nx)):
       # plt.plot(x[i],Function_FTBS[i], color='blue', label="Ftbs")
       # plt.plot(x[i],Function_CTCS[i], color='orange', label="Ctcs")
       # plt.plot(x[i],phiExact_s[i] , color = 'green', label="Exact")
       # plt.title('Nx='+str(Nx[i]))
       # plt.legend()
       # plt.show()
    
    
        
        
    
main()