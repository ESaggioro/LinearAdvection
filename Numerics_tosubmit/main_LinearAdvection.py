# =============================================================================
# Outer code for the study of linear advection on a uniform 1d grid: 
# it computes analytical solution and four implemented advection
# schemes; plots the results at final time step; operates 
# analysis on the schemes ( Mass and Variance conservation, 
# space order of accuracy, computational cost, dispersion )
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
   
    Nt = [20, 30, 40, 50, 100, 150, 200, 250, 300] # time steps
    Nx = [20, 30, 40, 50, 100, 150, 200, 250, 300] # numbers of grid points
    L = 1.0                                        # grid length
    C =  [0.3, 0.4, 0.5, 0.6, 0.8 , 1.2, 2.0]      # Courant number
   
    Gridx = [ Grid(nx,L) for nx in Nx] # grid class in grid.py
    Xaxis = [ g.x for g in Gridx]      # x-axis 
    Dx    = [ g.dx for g in Gridx]     # resolutions

  
## =============================================================================
## PLOT RESULT FROM ALL SCHEMES ADVECTION     
## =============================================================================
    print( '\n-------ADVECTION OF INITIAL PROFILE-------\n ' )
    # Set up 1: 
    # Nx=30 coarse, Nt=50 short time , C=0.3 small Courant number. 
    
    i_x = 1
    nt = Nt[3]
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
    colors = ['blue' , 'orange', 'magenta', 'red', 'green', 'grey']
    linestyles = ['-','-','-','-','--','--']
    schemes = [cosB_FTBS, cosB_CTCS,cosB_LAX, cosB_CNCS ,cosB_Exact, cosB_0]
    #outfile = 'Bell_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+'.pdf'
    
    # use Plot.py
    plot_Final(Gridx[i_x], schemes, labels, colors,linestyles ) 
    
    
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c))
    print('Advecting square wave profile ...')
    
    # square wave non-zero for x between 0.1 and 0.4 
    sqW_0     = squareWave (Xaxis[i_x], 0.1, 0.4 ) # from InitialConditions.py
    sqW_Exact = Analytical(squareWave, Gridx[i_x], c, nt, 0.1 ,0.4 )
    sqW_FTBS, sqW_CTCS, sqW_CNCS, sqW_LAX =run_schemes(Gridx[i_x], sqW_0 ,\
                                                       c, nt )
    
    
    # Plot all schemes and analytical solution at final time step
    schemes2 = [sqW_FTBS, sqW_CTCS, sqW_LAX, sqW_CNCS ,sqW_Exact, sqW_0]
    #outfile2 = 'Square_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+'.pdf'
    # use Plot.py
    plot_Final(Gridx[i_x], schemes2, labels, colors, linestyles) 
 
     
# =============================================================================
# MASS AND VARIANCE CONSERVATIONS     
# =============================================================================
    print( '\n-------MASS AND VARIANCE IN TIME-------\n ' )
    
    # Set up: 
    # Nx=150 fine, Nt=50 short time , C=0.6 Courant number. 
    # Initial conditions: cos-bell (smooth)  
    i_x = 5
    nt = Nt[3]
    c = C[3] 
    print( '-------nx=%g , nt=%g, C=%g -------\n' %(Nx[i_x],nt, c))
    print( '-------Initial condition: cosBell function-------' )
    # Initial condition, mass and variance
    cosB_0 = cosBell ( Xaxis[i_x] , L) 
    M0 = Mass (cosB_0 , Gridx[i_x].dx) 
    V0 = Variance (cosB_0 , Gridx[i_x].dx) 
  
    # M and V at each of the nt tsteps , for all schemes 
    times, M_s, V_s, name_s = MassVarianceInTime (Gridx[i_x], cosB_0 , nt , c )

    # plot M and V in time, for all schemes
    
    colors = [ 'blue', 'orange', 'm' , 'red']
    #outfile_M = 'Mass_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_cosBell.pdf'
    #outfile_V = 'Var_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_cosBell.pdf'
    
    #Use Plot.py
    delta = (max(M_s[-1])-min(M_s[0])+2e-15)/5
    yaxticM = [min(M_s[0])-0.9e-15+ i*delta for i in range(5) ]
    plot_MorV (times, M0, M_s , colors, name_s,  'M',\
               [min(M_s[0])-1e-15,max(M_s[-1])+1e-15],
               yaxticM)
    
    deltaV = (V0+0.0002-min(V_s[0]))/5
    yaxticV = [min(V_s[0]) + i*deltaV for i in range(5) ]
    plot_MorV(times, V0, V_s , colors, name_s, 'V',\
            [min(V_s[0]), V0+0.0006], yaxticV )
    
    

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
    logdx1 = 1*logDx + 1.7*FTBSfit[1] 
    logdx2 = 2*logDx + 1.05*CTCSfit[1]
    
    # Plot errors
    #outfile = 'Error_schemes_c0'+str(c)[-1]+'_cosbell.pdf'
    labels  = lab_er + [ "$\Delta x$", "${\Delta x}^2$"]
    colors  = ['blue' , 'orange', 'magenta', 'red'] + ['black', 'green']
    styles  = ['-','-','-','-',':',':']
    plot_Errors( logDx,\
                [ler_FTBS, ler_CTCS, ler_CNCS, ler_LAX]+[logdx1, logdx2] ,\
                labels , colors, styles )
     
 
## =============================================================================
## STABILITY OF CNCS     
## =============================================================================          
    print( '\n-------UNCONDITIONAL STABILITY OF CNCS -------\n ' )
    
    i_x = 4
    nt = Nt[5]
    c = C[6]
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c))
    
    print('Advecting cosBell profile ...')    
    cosB_0 = cosBell ( Xaxis[i_x] , L)  
    cosB_Exact = Analytical( cosBell, Gridx[i_x], c , nt , L)
    cncs = CNCS (Gridx[i_x], cosB_0 , c , nt)
    ctcs = CTCS (Gridx[i_x], cosB_0 , c , nt)
    
    # plot 
    #outfileCNCS = 'Bell_c'+str(c)[0]+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+'_CNCS.pdf'
    plot_Final(Gridx[i_x], [cncs, cosB_Exact], ['CNCS C=%g' %c, 'Exact'],\
               ['red', 'green'],['-','--'] ) 
    
    # plot ctcs unstable!!
    
    i_x = 4
    nt = Nt[0]
    c = C[5]
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c))
    
    print('Advecting cosBell profile ...') 
    cosB_0 = cosBell ( Xaxis[i_x] , L)
    cosB_Exact = Analytical( cosBell, Gridx[i_x], c , nt , L)
    cncs = CNCS (Gridx[i_x], cosB_0 , c , nt)
    ctcs = CTCS (Gridx[i_x], cosB_0 , c , nt)
    #outfileUnstable = 'Bell_c'+str(c)[0]+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_CNCSandCTCS.pdf'
    plot_Final(Gridx[i_x], [cncs,ctcs, cosB_Exact], \
               ['CNCS C=%g' %c,'CTCS ','Exact'],\
               ['red', 'orange', 'green'],['-','-','--'] ) 
    
    
# =============================================================================
# COMPUTATIONAL COST
# =============================================================================
    print( '\n------- COMPUTATIONAL COST (timeit) -------\n ' )
    cos0 = cosBell(Xaxis[4], L) 
    
    
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[4],Nt[5], 0.4 ))
    
    import timeit
   
    def runner(func, *args):
        def runned():
            return (func(*args))
        
        return (runned)
    
    runFTBS = runner ( FTBS, Gridx[4], cos0 , 0.4 , Nt[5]  )
    print('FTBS:', timeit.timeit(runFTBS, number=20))
    
    
    runCTCS = runner ( CTCS, Gridx[4], cos0 , 0.4 , Nt[5]  )
    print('CTCS:', timeit.timeit(runCTCS, number=20))
    
    
    runLAX = runner ( LaxWendroff, Gridx[4], cos0 , 0.4 , Nt[5]  )
    print('LAX:', timeit.timeit(runLAX, number=20) )
    
    
    runCNCS = runner ( CNCS, Gridx[4], cos0 , 0.4 , Nt[5]  )
    print('CNCS:', timeit.timeit(runCNCS, number=20))
    
       
# =============================================================================
# DISPERSION OF LAX WENDROFF                                                      
# =============================================================================
    print( '\n------- DISPERSION ERRORS OF A TOP-HAT PROFILE -------\n ' )
    i_x = 6
    nt = Nt[2]
    c = C[1]
    print( '-------nx=%g , nt=%g, C=%g  ---------\n' %(Nx[i_x],nt, c ))
    
    sq0 = squareWave (Xaxis[i_x], 0.1, 0.4)
    sqt = Analytical(squareWave, Gridx[i_x], c, nt, 0.1 ,0.4 )
    sqW_FTBS, sqW_CTCS, sqW_CNCS, sqW_LAX =run_schemes(Gridx[i_x], sq0 ,\
                                                       c, nt )
    # Plot CTCS 
    schem = [ sqW_CTCS ,sqt]
    colo = ['orange',  'green']
    lab   = ['CTCS', 'Exact']
    linest = ['-','--' ]
    #outfi = 'Square_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_CTCS_DISPERSION.pdf'
   
    plot_Final(Gridx[i_x], schem, lab, colo, linest ) 
    
    # Plot CNCS 
    schem = [ sqW_CNCS ,sqt]
    colo = ['red',  'green']
    lab   = [ 'CNCS', 'Exact']
    linest = ['-','--' ]
    #outfi = 'Square_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_CNCS_DISPERSION.pdf'
    
    plot_Final(Gridx[i_x], schem, lab, colo, linest ) 
    
    
    
    # Plot LAX
    schem = [ sqW_LAX ,sqt]
    colo = ['magenta',  'green']
    lab   = [ 'LAX', 'Exact']
    linest = ['-','--' ]
    #outfi = 'Square_c0'+str(c)[-1]+'_Nt'+str(nt)+'_Nx'+str(Nx[i_x])+\
    #'_LAX_DISPERSION.pdf'
    
    plot_Final(Gridx[i_x], schem, lab, colo, linest ) 
    

main()

