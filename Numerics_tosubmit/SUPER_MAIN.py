# =============================================================================
# Outer code for the study of linear advection on a uniform 1d grid: 
# it computes analytical solution and four implemented advection
# schemes; plots the results at final time step; operates 
# analysis on the schemes ( Mass and Variance conservation, 
# space order of accuracy )
# =============================================================================

#%%
import numpy as np
import matplotlib as plt

# read in all the linear advection schemes, initial conditions and other
# code associated with this code

# SUBTITUTE WITH IMPORT????
exec(open("./grid.py").read()) 
exec(open("./InitialConditions.py").read()) # Initial condition functions
exec(open("./Analytical.py").read())
exec(open("./AdvectionSchemes.py").read()) 
exec(open("./Errors.py").read())
exec(open("./MassVariance.py").read())
exec(open("./Plot.py").read()) 

#import grid as Gr 
#import InitialConditions.py as InCo
#import Analytical.py as Exact
#import AdvectionSchemes.py as Schemes 
#import Errors.py as Err
#import MassVariance.py as Coserv
#import Plot.py as Plot


SMALL = 1e-10  # a small number to test boundary conditions

def main():
    
    " Analysis of linear advection equation on a 1-d grid. \
    "
# =============================================================================
# Set up parameters
# =============================================================================
   
    Nt = [20, 40, 50, 100, 150, 200, 250, 300] # time steps
    Nx = [20, 40, 50, 100, 150, 200, 250, 300] # number of grid points
    L = 1.0                                    # grid length
    C = [0.3, 0.4, 0.5, 0.8 , 1.0 , 1.5 ]      # Courant number
   
    Gridx = [ Grid(nx,L) for nx in Nx] # grid class in grid.py
    Xaxis = [ g.x for g in Gridx]      # x-axis 
#%%   
# =============================================================================
# PLOT ADVECTION FOR ALL SCHEMES
# Set up: 
# Nx=20 coarse, Nt=40 short time , C=0.3 small Courant number. 
# Two initial conditions: cos-bell (smooth) and square wave (non-smooth)      
# =============================================================================
    
    i_x = 0
    nt = Nt[1]
    c = C[0]
    
    print('Advecting cosBell profile ...')    
    
    cosB_0     = cosBell(Xaxis[i_x], L)  # from InitialConditions.py  
    cosB_Exact = Analytical( cosBell, Gridx[i_x], c , nt , L)
    cosB_FTBS, cosB_CTCS, cosB_CNCS, cosB_LAX = \
                                run_schemes(Gridx[i_x], cosB_0 , c , nt )
    
    
    # Plot all schemes and analytical solution at final time-step :
    
    # Define plot parameters
    labels = ["FTBS", "CTCS", "Lax", "CNCS", "Exact", "Initial"]
    colors = ['blue' , 'orange', 'magenta', 'red', 'green', 'lightgreen']
    linestyles = ['-','-','-','-','--','-.']
    schemes = [cosB_FTBS, cosB_CTCS,cosB_LAX, cosB_CNCS ,cosB_Exact, cosB_0]
    outfile = 'Bell_c03_Nt40_Nx20.pdf'
    # use Plot.py
    plot_Final(Gridx[i_x], schemes, labels, colors,linestyles, outfile ) 
    
    
    print('Advecting square wave profile ...')
    # square wave non-zero for x between 0.1 and 0.4 
    sqW_0     = squareWave (Xaxis[i_x], 0.1, 0.4 ) # from InitialConditions.py
    sqW_Exact = Analytical(squareWave, Gridx[i_x], c, nt, 0.1 ,0.4 )
    sqW_FTBS, sqW_CTCS, sqW_CNCS, sqW_LAX =run_schemes(Gridx[i_x], sqW_0 ,\
                                                       c, nt )
    
    
    # Plot all schemes and analytical solution at final time step
    schemes2 = [sqW_FTBS, sqW_CTCS, sqW_LAX, sqW_CNCS ,sqW_Exact, sqW_0]
    # use Plot.py
    plot_Final(Gridx[0], schemes2, labels, colors,linestyles, \
               'Square_c03_Nt40_Nx20.pdf') 
#%%     
# =============================================================================
# MASS AND VARIANCE CONSERVATIONS
# Set up: 
# Nx=100 fine, Nt=100 long time , C=0.8 Courant number. 
# Initial conditions: cos-bell (smooth)     
# =============================================================================
    
    i_x = 1
    nt = Nt[3]
    c = C[2] 
    
    # Initial condition, mass and variance
    phi0 = cosBell ( Xaxis[i_x] , L) 
    M0 = Mass (phi0 , Gridx[i_x].dx) 
    V0 = Variance (phi0 , Gridx[i_x].dx) 
    
    # M and V at each of the nt tsteps , for all schemes 
    M_s,V_s,name_s = MassVarianceInTime (Gridx[i_x], phi0, nt , c )
    
    # plot results
    times = np.arange(1,Nt[3])
    colors = [ 'blue', 'orange', 'm' , 'red']
    outfile_M = 'Mass_c05_Nx40_Nt100.pdf'
    outfile_V = 'V_c05_Nx40_Nt100.pdf' 
    plot_MassVariance( times, M0 , V0, M_s , V_s,\
                       colors, name_s, outfile_M, outfile_V )
    
    
    
# =============================================================================
# ERRORS AND ORDER OF ACCURACY 
# Set up: 
# Nx = Nx, Nt= Nt , C=0.4 Courant number. 
# Initial conditions: cos-bell (smooth)     
# =============================================================================
       
    
    
    
    
    
    
main()

#%% 