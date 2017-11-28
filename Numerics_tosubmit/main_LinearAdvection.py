# =============================================================================
# Outer code for the study of linear advection on a uniform 1d grid: 
# it computes analytical solution and four implemented advection
# schemes; plots the results at final time step; operates 
# analysis on the schemes ( Mass and Variance conservation, 
# space order of accuracy )
# =============================================================================

import numpy as np

# read in all the code associated with the linear advection study
exec(open("./grid.py").read()) 
exec(open("./InitialConditions.py").read()) 
exec(open("./Analytical.py").read()) 
exec(open("./AdvectionSchemes.py").read()) 
exec(open("./Errors.py").read())
exec(open("./MassVariance.py").read()) 
exec(open("./Plot.py").read())

SMALL = 1e-10  # a small number to test boundary conditions

def main():
    
    " Analysis of linear advection equation on a 1-d grid "
    "  via four numerical schemes. \
    "
# =============================================================================
# Set up parameters
# =============================================================================
   
    Nt = [20, 40, 50, 100, 150, 200, 250, 300] # time steps
    Nx = [20, 40, 50, 100, 150, 200, 250, 300] # numbers of grid points
    L = 1.0                                    # grid length
    C =  [0.3, 0.4, 0.5, 0.6, 0.8 ]      # Courant number
   
    Gridx = [ Grid(nx,L) for nx in Nx] # grid class in grid.py
    Xaxis = [ g.x for g in Gridx]      # x-axis 
    Dx    = [ g.dx for g in Gridx]     # resolutions

  
## =============================================================================
## PLOT RESULT FROM ALL SCHEMES ADVECTION     
## =============================================================================
    print( '\n-------ADVECTION OF INITIAL PROFILE-------\n ' )
    # Set up: 
    # Nx=20 coarse, Nt=40 short time , C=0.3 small Courant number. 
    # Two initial conditions: cos-bell (smooth) and square wave (non-smooth) 
    
    i_x = 0
    nt = Nt[1]
    c = C[0]
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c))
    
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
    outfile = 'Bell_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[0])+'.pdf'
    # use Plot.py
    plot_Final(Gridx[i_x], schemes, labels, colors,linestyles, outfile ) 
    
#%%    
    # Set up: 
    # Nx=100 fine, Nt=100 long time , C=0.3 small Courant number. 
    # Two initial conditions: cos-bell (smooth) and square wave (non-smooth) 
    
    i_x = 3
    nt = Nt[4]
    c = C[0]
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c))
    print('Advecting square wave profile ...')
    
    # square wave non-zero for x between 0.1 and 0.4 
    sqW_0     = squareWave (Xaxis[i_x], 0.1, 0.4 ) # from InitialConditions.py
    sqW_Exact = Analytical(squareWave, Gridx[i_x], c, nt, 0.1 ,0.4 )
    sqW_FTBS, sqW_CTCS, sqW_CNCS, sqW_LAX =run_schemes(Gridx[i_x], sqW_0 ,\
                                                       c, nt )
    
    
    # Plot all schemes and analytical solution at final time step
    schemes2 = [sqW_FTBS, sqW_CTCS, sqW_LAX, sqW_CNCS ,sqW_Exact, sqW_0]
    outfile2 = 'Square_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[0])+'.pdf'
    # use Plot.py
    plot_Final(Gridx[i_x], schemes2, labels, colors, linestyles, outfile2 ) 
 
 
#%%     
# =============================================================================
# MASS AND VARIANCE CONSERVATIONS     
# =============================================================================
    print( '\n-------MASS AND VARIANCE IN TIME-------\n ' )
    # Set up: 
    # Nx=100 fine, Nt=100 long time , C=0.6 Courant number. 
    # Initial conditions: cos-bell (smooth)  
    i_x = 2
    nt = Nt[3]
    c = C[1] 
    print( '-------nx=%g , nt=%g, C=%g -------\n' %(Nx[i_x],nt, c))
    print( '-------Initial condition: cosBell function-------' )
    # Initial condition, mass and variance
    cosB_0 = cosBell ( Xaxis[i_x] , L) 
    M0 = Mass (cosB_0 , Gridx[i_x].dx) 
    V0 = Variance (cosB_0 , Gridx[i_x].dx) 
  
    # M and V at each of the nt tsteps , for all schemes 
    M_s,V_s,name_s = MassVarianceInTime (Gridx[i_x], cosB_0 , nt , c )
      
    # plot M and V in time, for all schemes
    times = np.arange(1,Nt[3])
    colors = [ 'blue', 'orange', 'm' , 'red']
    outfile_M = 'Mass_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[0])+\
    '_cosbell.pdf'
    outfile_V = 'Var_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[0])+\
    '_cosbell.pdf'
    # use Plot.py
    plot_MorV (times, M0, M_s , colors, name_s, outfile_M, 'M')
    plot_MorV (times, V0, V_s , colors, name_s, outfile_V, 'V')
    

## =============================================================================
## ERRORS AND ORDER OF ACCURACY     
## =============================================================================
    print( '\n--ERRORS AND ORDER OF ACCURACY--\n ' )
    # Set up: 
    # Nx = Nx, Nt= Nt , C=0.4 Courant number.
    # Initial conditions: cos-bell (smooth) 
    c = C[1]
    
    print( '--Nx='+str(Nx)+' ,\n--Nt='+str(Nx)+' ,\n--C=%g \n' %c)
    print( '-------Initial condition: cosBell function------- \n' )
    
    # log10(error norm) for all schemes, using different number of 
    # grid points, Nx.
    [ler_FTBS, ler_CTCS, ler_CNCS, ler_LAX], lab_er = \
     ErrorsAgainstResolution( Nx, L, c, l2_norm, Nt, cosBell, L)
     
    # Fit the logerrors vs logDx to polynomial y=mx+b. Returns [m,q]:
    logDx   = np.log10(Dx) 
    FTBSfit = np.polyfit(logDx ,ler_FTBS, 1)
    CTCSfit = np.polyfit(logDx ,ler_CTCS, 1)
    CNCSfit = np.polyfit(logDx ,ler_CNCS, 1)
    LAXfit  = np.polyfit(logDx ,ler_LAX , 1)
     
    print('------l2 norm errors vs Dx (log-log scale)------ ')
    print('Linear Fit Parameters:  [ m , q ]')
    print("FTBS parameters      : ", FTBSfit)
    print("CTCS parameters      : ", CTCSfit)
    print("CNCS parameters      : ", CNCSfit)
    print("LAX parameters       : ", LAXfit)
     
    # Lines parallel to dx^1 and dx^2
    logdx1 = 1*logDx + 0.98*FTBSfit[1] 
    logdx2 = 2*logDx + 1.05*CTCSfit[1]
    
    # Plot errors
    outfile = 'Error_schemes_c0'+str(c)[-1]+'_cosbell.pdf'
    labels  = lab_er + [ "$\Delta x$", "${\Delta x}^2$"]
    colors  = ['blue' , 'orange', 'magenta', 'red'] + ['black', 'green']
    styles  = ['-','-','-','-',':','--']
    plot_Errors( logDx,\
                [ler_FTBS, ler_CTCS, ler_CNCS, ler_LAX]+[logdx1, logdx2] ,\
                labels , colors, styles, outfile )
     
     

    
main()

#%% 