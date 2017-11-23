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
exec(open("./CNCS.py").read())
exec(open("./LaxWendroff.py").read())

exec(open("./L_norm_errors.py").read())



def main():

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    ## SPACE-TIME GRID AND COURANT NUMBER DEFINITION    

    ## Define the physical total time T and Courant number c
    # YOU WILL WANT TO ASK (L,Nx) AS INPUT TO THE USER ---------- 
    T = 10
    print('The total time chosen is T = ' , T)
    c = 0.3 
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
    d = 1 
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
    Function_CNCS = [ np.zeros(n , dtype=float) for n in Nx]
    Function_LAX = [ np.zeros(n , dtype=float) for n in Nx]
    
    ## Errors vectors initialized to 0 scalar, for the various x-grids
    Error_FTBS = [0.0 for i in range(len(Nx))]
    Error_CTCS = [0.0 for i in range(len(Nx))]
    Error_CNCS = [0.0 for i in range(len(Nx))]
    Error_LAX = [0.0 for i in range(len(Nx))]
    
    
    # Evolve for nt time steps the i.c. (set to bell function)
    # for Analytical, FTCB and CTCS. 
    # And compute error - norm
    for i,grid in enumerate(gridx): # run over different grid resolution
        print('Number of time steps=', Nt[i])
        phi0_s[i] , phiExact_s[i] = \
        Analytical( cosBell , grid , c , Nt[i] ,L )
        
        Function_CTCS[i]  = CTCS ( grid, phi0_s[i] , c , Nt[i] )
        Function_FTBS[i]  = FTBS ( grid, phi0_s[i] , c , Nt[i] )
        Function_CNCS[i]  = CNCS ( grid, phi0_s[i] , c , Nt[i] )
        Function_LAX[i]  = LaxWendroff( grid, phi0_s[i] , c , Nt[i] )
        
        Error_CTCS[i]=l2_norm(Function_CTCS[i] ,phiExact_s[i])
        Error_FTBS[i]=l2_norm(Function_FTBS[i] ,phiExact_s[i])
        Error_CNCS[i]=l2_norm(Function_CNCS[i] ,phiExact_s[i])
        Error_LAX[i]=l2_norm(Function_LAX[i] ,phiExact_s[i])
        
    # Fit the errors:
    # L2
    logdx = np.log10(dx)
    logerrCTCS = np.log10(Error_CTCS)
    logerrFTBS = np.log10(Error_FTBS)
    logerrCNCS = np.log10(Error_CNCS)
    logerrLAX = np.log10(Error_LAX)
    
    # fit x,y data to polynomial y=mx+b. Returns [m,q]
    CTCSfit=np.polyfit(logdx,logerrCTCS, 1)
    FTBSfit=np.polyfit(logdx,logerrFTBS, 1)
    CNCSfit=np.polyfit(logdx,logerrCNCS, 1)
    LAXfit=np.polyfit(logdx,logerrLAX, 1)
    
    print('L2 errors:         [ m   ,   q ]')
    print("FTBS parameters = ", FTBSfit)
    print("CTCS parameters = ", CTCSfit)
    print("CNCS parameters = ", CNCSfit)
    print("LAX parameters = ", LAXfit)
    
    
    # PLOT L2
    myoutfile = 'Error_FTBS-CTCS-CNCS-LAX_c0'+str(c)[-1]+'.pdf'
    
    # Lines parallel to dx^1 and dx^2
    logdx1 = 1*logdx + 0.9*FTBSfit[1]
    logdx2 = 2*logdx + 1.1*CTCSfit[1]
    
    
    plot_error( logdx, [ logerrFTBS , logerrCTCS , logerrCNCS, logerrLAX, \
    logdx1, logdx2  ] , \
    ["FTBS ", "CTCS", "CNCS", "LAX", "$\Delta x$", "${\Delta x}^2$"],\
    ['blue' , 'orange', 'magenta', 'red', 'black', 'green'] ,\
                myoutfile, \
                title='$l_{2}$-norm errors : cosbell and c=%g'%c, \
                xlabel='$\Delta x$', \
                linestyles=['-','-','-','-',':','--'])
    
    
    
    #for i in range(len(Nx)):
       # plt.plot(x[i],Function_FTBS[i], color='blue', label="Ftbs")
       # plt.plot(x[i],Function_CTCS[i], color='orange', label="Ctcs")
       # plt.plot(x[i],phiExact_s[i] , color = 'green', label="Exact")
       # plt.title('Nx='+str(Nx[i]))
       # plt.legend()
       # plt.show()
    
    
        
        
    
main()