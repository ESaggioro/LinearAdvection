# =============================================================================
# This function computes the Mass and Variance of a profile phi
# =============================================================================

import numpy as np

def Mass( phi , dx ):
    "Compute the 'Mass' of a function phi (with periodic-boundary) on a grid"
    "with homogeneous space discretization dx.\
    "
    M = dx * sum(phi[1:])
    
    return( M )
    
def Variance( phi , dx ):
    " Compute the Variance of a function phi (with periodic-boundary) on a grid"
    "with homogeneous space discretization dx.\
    " 
    V = dx * sum(np.square(phi[1:]))
    
    return( V )
    
  
def MassVarianceInTime(  grid, phi0, tsteps, c ):
    " Mass and Variance at every time step , for all advection schemes "
    " Given the space grid, grid, the initial condiotion , phi0 array, and the"
    " number of timesteps, tsteps.\
    "
    
    # Initialize to 0 the array for M and V ,for every scheme
    MFTBS, VFTBS    = np.zeros(tsteps), np.zeros(tsteps)
    MCTCS, VCTCS    = np.zeros(tsteps), np.zeros(tsteps)
    MLAX, VLAX      = np.zeros(tsteps), np.zeros(tsteps)
    MCNCS, VCNCS    = np.zeros(tsteps), np.zeros(tsteps)
    
    # arrays used in the loop
    philoopF = FTBS (grid, phi0, c , 1 )
    philoopCT = CTCS (grid, philoopF, c , 1 , phi0 ) 
    philoopCT_Older = philoopF # CTCS needs to initialize 2 tsteps
    philoopCN = CNCS (grid, phi0, c , 1 )
    philoopLA = LaxWendroff (grid, phi0, c , 1 )
    
    for t in range(2, tsteps+1): # M and V in time
        
        phiFTBS = FTBS (grid, philoopF, c , 1 ) # FTBS scheme
        phiCTCS = CTCS (grid, philoopCT, c , 1 , philoopCT_Older )# CTCS scheme
        phiLAX = LaxWendroff (grid, philoopLA , c , 1 ) # LaxWendroff scheme
        phiCNCS = CNCS (grid, philoopCN, c , 1 )  # CTCS sceheme
         
        # Compute Mass after t
        MFTBS[t-1] = Mass(phiFTBS , grid.dx)
        MCTCS[t-1] = Mass(phiCTCS , grid.dx)
        MLAX[t-1] = Mass (phiLAX , grid.dx)
        MCNCS[t-1] = Mass (phiCNCS , grid.dx)
    
        # Compute Variance after t
        VFTBS[t-1] = Variance(phiFTBS , grid.dx)
        VCTCS[t-1] = Variance(phiCTCS , grid.dx)
        VLAX[t-1] = Variance (phiLAX , grid.dx)
        VCNCS[t-1] = Variance (phiCNCS , grid.dx)
        
        # Update
        philoopF = phiFTBS
        philoopCT_Older = philoopCT
        philoopCT = phiCTCS
        philoopLA = phiLAX 
        philoopCN = phiCNCS 
    
    M_schemes = [ MFTBS[1:], MCTCS[1:], MCNCS[1:], MLAX[1:]] 
    V_schemes = [ VFTBS[1:], VCTCS[1:], VCNCS[1:], VLAX[1:]]
    labels = ['FTBS', 'CTCS', 'CNCS', 'LAX' ]
    
    return( M_schemes, V_schemes, labels )