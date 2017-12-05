# =============================================================================
# This function computes the Mass and Variance of a profile phi
# =============================================================================

import numpy as np

def Mass( phi , dx ):
    "Compute the 'Mass' of a function phi (with periodic-boundary) on a grid"
    "with homogeneous space discretization dx.\
    "
    M = dx * np.sum(phi[1:])
    
    return( M )
    
def Variance( phi , dx ):
    " Compute the Variance of a function phi (with periodic-boundary) on a grid"
    "with homogeneous space discretization dx.\
    " 
    V =  dx * np.sum(np.square(phi[1:])) - Mass(phi,dx)**2
    
    return( V )
    
  
def MassVarianceInTime(  grid, phi0, tsteps, c ):
    " Mass and Variance at every time step , for all advection schemes "
    " Given the space grid, grid, the initial condiotion , phi0 array, and the"
    " number of timesteps, tsteps."
    " Returns the time-steps used, times, the list of mass arrays, M_scheme, "
    " th elist of var. arrays, V_scheme, the ordered list of labels , labels."
    
    times = [ 2*n for n in range(1,int(tsteps/2))] #avoid CTCS probles for t=1
    dx = grid.dx
    
    # define lists for  M and V ,for every scheme
    MFTBS  = []
    MCTCS  = []
    MLAX   = []
    MCNCS  = []
    
    VFTBS  = []
    VCTCS  = []
    VLAX   = []
    VCNCS  = []

    # M and V in time
    for i,t in enumerate(times): 
        
        ftbs = FTBS (grid, phi0, c , t ) # FTBS scheme
        ctcs = CTCS (grid, phi0, c , t  )# CTCS scheme
        lax = LaxWendroff (grid, phi0, c , t ) # LaxWendroff scheme
        cncs = CNCS (grid, phi0, c , t )  # CTCS sceheme
         
        # Compute Mass after t
        MFTBS.append(Mass(ftbs , dx))
        MCTCS.append(Mass(ctcs , dx))
        MLAX.append(Mass(lax , dx))
        MCNCS.append(Mass(cncs , dx))
    
        # Compute Variance after t
        VFTBS.append( Variance(ftbs , dx))
        VCTCS.append( Variance(ctcs , dx))
        VLAX.append( Variance(lax , dx))
        VCNCS.append( Variance(cncs , dx))
    
    M_schemes = [ MFTBS, MCTCS, MLAX,  MCNCS] 
    V_schemes = [ VFTBS, VCTCS, VLAX,  VCNCS]
    labels    = ['FTBS', 'CTCS', 'LAX', 'CNCS' ]
    
    return( times, M_schemes, V_schemes, labels )