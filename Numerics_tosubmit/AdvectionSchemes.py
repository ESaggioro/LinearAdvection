# =============================================================================
# Advection schemes 
# =============================================================================

import numpy as np
import scipy 
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


def Check_periodic_boundary(f):
    "Check if array f has periodic boundaries\
    "
    if np.abs(f[0] - f[-1])> SMALL :
        print('Careful:your initial condition does not have\
              periodic boundaries')

def FTBS ( gridx, phi0, c , nt): 
    "FTBS scheme for linear advection on initial array profile phi0" 
    "Using Courant number c, for nt time-steps, on a space grid gridx"
    "Returns the final advected profile\
    "
    
    Check_periodic_boundary(phi0) 
    
    # number of grid points       
    nx = gridx.nx
    # Create the functions phi and initialize to 0 
    phi = np.zeros(nx,dtype=float)
    # Create the functions phiOld and initialize to phi0 
    phiOld = phi0.copy()
        
    # Loop over time steps
    for it in range(nt):
        # Loop over space (excluding end points)
        for ix in range(1,nx-1):
            phi[ix] = phiOld[ix] -  c * (phiOld[ix] - phiOld[ix-1])
        # Update values at end points
        phi[0] = phiOld[0] -  c * (phiOld[0] - phiOld[nx-2])
        # Use periodic boundaries
        phi[nx-1] = phi[0]
        # Update old time value
        phiOld = phi.copy() 
        
    return(phi)


def CTCS ( gridx, phi0, c , tsteps, phiOlder=[None]): 
    "CTCS scheme for linear advection on initial array profile phi0" 
    "Using Courant number c, for nt time-steps, on a space grid gridx"
    "Additional argument , *arg, can be phi(-1),  if tsteps=1"
    "Returns the final advected profile\
    "
    
    Check_periodic_boundary(phi0) 
    
    # number of grid points          
    nx = gridx.nx  
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx , dtype=float) 
    
    if tsteps > 1:
        # Create phiOld2 and initialize to phi0
        phiOld2 = phi0.copy()
        # Create phiOld1 and initialize using FTBS 
        phiOld1 = FTBS (gridx, phi0, c , 1)   
    
        # Loop over time steps t = 1,..
        for it in range(1,tsteps):  
            # Loop CTCS over space (excluding end points)
            for ix in range(1,nx-1):
                phi[ix] = phiOld2[ix] - c * ( phiOld1[ix+1] - phiOld1[ix-1] )
            # Update values at end points
            phi[0] = phiOld2[0] -  c * (phiOld1[1] - phiOld1[-2])
            # Use periodic boundaries
            phi[-1] = phi[0]
            # Update old time value 
            phiOld2 = np.copy(phiOld1)
            phiOld1 = np.copy(phi)
                
    else : # tsteps = 1
        phiOld2 = phiOlder.copy()
        phiOld1  = phi0.copy()
        # Loop CTCS over space (excluding end points)
        for ix in range(1,nx-1):
                phi[ix] = phiOld2[ix] - c * ( phiOld1[ix+1] - phiOld1[ix-1] )
        # Update values at end points
        phi[0] = phiOld2[0] -  c * (phiOld1[1] - phiOld1[-2])
        # Use periodic boundaries
        phi[-1] = phi[0] 
            
    return(phi)
    

def CNCS (gridx, phi0, c ,tsteps ):
    "CNCS scheme for linear advection on initial array profile phi0" 
    "Using Courant number c, for nt time-steps, on a space grid gridx"
    "Returns the final advected profile\
    "
    
    Check_periodic_boundary(phi0) 
        
    # The vector used to store phi in CNCS does not include last element 
    N = gridx.nx - 1     # dimension of vector for CNCS 
    v = phi0[:N]         # initial condition 
    
    # Built the matrices Q and M s.t. M*v^{n+1}=Q*v^n  
    diagonals = [ np.ones(N), \
                  0.25*c*np.ones(N-1),\
                 -0.25*c*np.ones(N-1),\
                  0.25*c*np.ones(1),\
                 -0.25*c*np.ones(1)]
    
    Q = diags(diagonals, [0, -1,+1,+(N-1),-(N-1)], format='csr')
    M = diags(diagonals, [0, 1,-1,-(N-1),+(N-1)],  format='csr')
    
    # x := v^{n+1} is calculated solving M*x = b := Q*v^n
    for t in range(tsteps):
        v = spsolve(M, Q * v)
        
    # Recover the periodic solution phi   
    phi = np.append(v, v[0]) 
    
    return(phi)
        
def LaxWendroff ( gridx, phi0, c , tsteps ): 
    "Lax-wendroff scheme for linear advection on initial array profile phi0" 
    "Using Courant number c, for nt time-steps, on a space grid gridx"
    "Returns the final advected profile\
    "
    
    Check_periodic_boundary(phi0) 
    
    # number of grid points
    nx = gridx.nx 
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx,dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld = np.copy(phi0)
    
    # Loop over time steps
    for it in range(tsteps):
        # Loop over space (excluding end points)
        for ix in range(1,nx-1):
            phi[ix] = phiOld[ix]*(1-c**2) + \
                      phiOld[ix+1]*0.5*c*(c-1)+\
                      phiOld[ix-1]*0.5*c*(c+1)
        # Update values at end points    
        phi[0] =  phiOld[0]*(1-c**2) + \
                      phiOld[+1]*0.5*c*(c-1)+\
                      phiOld[-2]*0.5*c*(c+1)
        # Use periodic boundaries 
        phi[-1] = phi[0]
        # Update old time value 
        phiOld = np.copy(phi)
        
    return(phi)
    
    
def run_schemes( gridx, phi0, c , tsteps  ):
    "Runs all the advection schemes on initial array profile phi0, " 
    "using Courant number c, for nt time-steps, on a space grid gridx."
    "Returns the final advected profiles.\
    "
    phiFTBS = FTBS( gridx, phi0, c , tsteps  )
    phiCTCS = CTCS( gridx, phi0, c , tsteps  )
    phiCNCS = CNCS( gridx, phi0, c , tsteps  )
    phiLAX = LaxWendroff( gridx, phi0, c , tsteps  )
    
    return( phiFTBS, phiCTCS, phiCNCS, phiLAX)
    
    