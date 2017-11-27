# This function is the implemetation of the Lax Wendroff finite-volume method
# to solve linear advection in 1-d

import numpy as np


SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def LaxWendroff ( gridx, phi0, c , tsteps ): 
    "Linear advection of initial profile phi0 using CTCS, Courant number c"
    "for tsteps time-steps "
    
    # Check periodic boundaries on phi0
    if np.abs(phi0[0] - phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
    
    nx = gridx.nx # number of grid points
    
    # Create the function phi(t) and initialize to 0
    phi = np.zeros(nx,dtype=float) 
    # Create phiOld and initialize it to phi0
    phiOld = np.copy(phi0)
    
    # Loop over time steps
    for it in range(tsteps):
        # Loop over space (excluding end points, [0] and [nx-1])
        for ix in range(1,nx-1):
            phi[ix] = phiOld[ix]*(1-c**2) + \
                      phiOld[ix+1]*0.5*c*(c-1)+\
                      phiOld[ix-1]*0.5*c*(c+1)
        # Update values at end points    
        phi[0] =  phiOld[0]*(1-c**2) + \
                      phiOld[+1]*0.5*c*(c-1)+\
                      phiOld[-2]*0.5*c*(c+1)
        phi[-1] = phi[0]
        
        # Update new phiOld
        phiOld = np.copy(phi)
        
    
    return(phi)
    
    

        
    