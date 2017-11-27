## This function is the main that I use to solve and analyse 
## the linear advection problem

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

def main():
    
    # Set up the grid
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
    
    
    for t in [10,30,50,100,200, 500]:
        CC = CTCS ( gridx, phi0_Bell , c , t , t )
        phi0bell ,phibell = Analytical( cosBell , gridx , c , t , t ) 
        plt.plot(x,phibell, color='green', linestyle='--', label = "Analytical")
        plt.plot(x,CC, color='orange', linestyle='-', label = "CTCS")
        plt.legend(loc='best')
        plt.title('time steps ='+str(t), fontsize=12)
        outfile='CTCS_bell_t'+str(t)
        plt.savefig(outfile, bbox_inches='tight')
        plt.show()
    
    
    # FTBS scheme for three initial conditions
    Ftbs_Square = FTBS ( gridx, phi0_Square , c , Nt , T )
    ##plot_Final(gridx, [Ftbs_Square, phiSquare] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_square_advection.png' )
    
    Ftbs_Sine = FTBS ( gridx, phi0_Sine , c , Nt , T )
    ##plot_Final(gridx, [Ftbs_Sine, phiSine] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_sine_advection.png' )
    
    
    Ftbs_Bell = FTBS ( gridx, phi0_Bell , c , Nt , T )
    
    for t in [10,30,50,100,200, 500]:
        FF = FTBS ( gridx, phi0_Bell , c , t , t )
        phi0bell ,phibell = Analytical( cosBell , gridx , c , t , t ) 
        plt.plot(x,phibell, color='green', linestyle='--', label = "Analytical")
        plt.plot(x,FF, color='blue', linestyle='-', label = "FTBS")
        plt.legend(loc='best')
        plt.title('time steps ='+str(t), fontsize=12)
        outfile='FTBS_bell_t'+str(t)
        plt.savefig(outfile, bbox_inches='tight')
        plt.show()
        
    ##plot_Final(gridx, [Ftbs_Bell, phiBell] , \
                ##["FTBS scheme", "Analytical"], 'FTBS_bell_advection.png' )
    
    plot_Final(gridx, [Ftbs_Bell, Ctcs_Bell, phiBell ] , \
                ["FTBS", "CTCS", "Analytical"],'FTBS_CTCS_bell.pdf') 
    
    Error_FTBS_bell=l2_norm ( Ftbs_Bell, phiBell)
    Error_CTCS_bell=l2_norm ( Ctcs_Bell, phiBell)
    
    print("Error FTBS = ", Error_FTBS_bell)
    
    print("Error CTCS = ", Error_CTCS_bell)
    
    
    
    
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
    #plot_Final(gridx, [Upwind_Square, phiSquare] , \
              #["UPWIND scheme", "Analytical"], 'UPWIND_square_advection.png' )
    
    
    
    
main()