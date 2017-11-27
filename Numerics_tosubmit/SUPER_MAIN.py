
# Outer code for the study of linear advection on a uniform 1d grid 
# Calls functions for analytical solution and for the advection
# schemes implemented. Plots the results at final time step. Operates 
# analysis on the schemes: Mass and Variance conservation, order of accuracy
# in space.

import numpy as np
import matplotlib as plt

# read in all the linear advection schemes, initial conditions and other
# code associated with this code

exec(open("./grid.py").read()) 
exec(open("./InitialConditions.py").read())

exec(open("./Analytical.py").read())
exec(open("./AdvectionSchemes.py").read()) 

exec(open("./Errors.py").read())
exec(open("./MassVariance.py").read())
exec(open("./Plot.py").read()) 

# a small number to test numerical equality ??
SMALL = 1e-10 

def main():
    
    # Set timestpes,length of grid and number of grid points, Courant number
    
    Nt = [20, 40, 50, 100, 150]# time steps
    Nx = [20, 40, 50, 100, 150]# number of grid points (including end points)
    L = 1.0 # grid length
    C = [0.3, 0.4, 0.5, 0.8 , 1.0 , 1.5 ] # Courant number
   
    # define a grid-object and xaxis for each Nx (using class in grid.py)
    Gridx = [ Grid(nx,L) for nx in Nx]
    Xaxis = [ g.x for g in Gridx]
    
        
    # First test: plot advection for all schemes. 
    # Set up: 
    # coarse dx (Nx=20), short time (Nt=40),small C=0.3, 
    # two initial conditions; cosbell(smooth) and squarewave (non-smooth)
   
    print('Advecting cosBell profile ...')    
    cosB_0     = cosBell(Xaxis[0], L)  # cosBell from InitialConditions.py  
    cosB_Exact = Analytical( cosBell, Gridx[0], C[0], Nt[1], L)
    cosB_FTBS, cosB_CTCS, cosB_CNCS, cosB_LAX = \
                                run_schemes(Gridx[0], cosB_0 , C[0], Nt[1] )
    
    
    # Plot all schemes and analytical solution at final time step
    
    labels = ["FTBS", "CTCS", "Lax", "CNCS", "Exact", "Initial"]
    colors = ['blue' , 'orange', 'magenta', 'red', 'green', 'lightgreen']
    linestyles = ['-','-','-','-','--','-.']
    schemes = [cosB_FTBS, cosB_CTCS,cosB_LAX, cosB_CNCS ,cosB_Exact, cosB_0]
    
    plot_Final(Gridx[0],schemes, labels, colors,linestyles, \
               'Bell_c03_Nt40_Nx20.pdf') 
    
    
    print('Advecting square wave profile ...')
    squareW_0     = squareWave (Xaxis[0], 0.1,0.4 ) # from InitialConditions.py
    squareW_Exact = Analytical(squareWave, Gridx[0], C[0], Nt[1], 0.1 ,0.4 )
    squareW_FTBS, squareW_CTCS, squareW_CNCS, squareW_LAX = \
        run_schemes(Gridx[0], squareW_0 , C[0], Nt[1] )
    
    # Plot all schemes and analytical solution at final time step
    schemes2 = [squareW_FTBS, squareW_CTCS,squareW_LAX, squareW_CNCS ,\
                squareW_Exact, squareW_0]
    plot_Final(Gridx[0], schemes2, labels, colors,linestyles, \
               'Square_c03_Nt40_Nx20.pdf') 
    
  
    # Second test :
    # Mass and Variance conservation for fine mesh (Nx=100), long time (Nt=100)
    
    # M and V for every scheme
    phi0 = cosBell ( Xaxis[1] , L) # initial condition
    print(Gridx[1].dx)
    M0 = Mass (phi0 , Gridx[1].dx) # initial Mass
    V0 = Variance (phi0 , Gridx[1].dx) # initial Variance
    # call schemes
    M_schemes,V_schemes,name_schemes = \
    MassVarianceInTime (Gridx[1], phi0, Nt[3], C[2] )
    print(name_schemes)
    # plot results
    plot_MassVariance(np.arange(1,Nt[3]), M0 , V0, M_schemes , V_schemes,\
                       [ 'blue', 'orange', 'm' , 'red'],\
                        name_schemes,\
                       'Mass_c05_Nx40_Nt100.pdf', 'V_c05_Nx40_Nt100.pdf')
    
   
    
    
    
    
    
    
main()