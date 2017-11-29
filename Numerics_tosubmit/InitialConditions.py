# =============================================================================
# Two initial conditions for linear advection
# =============================================================================

import numpy as np

def cosBell(x , Lx):
    "Function defining a cosine bell as a function of position, x, and Lx is "
    "the total length of the x-domain. \
    " 
    
    x = np.float64(x / Lx ) # rescale x for convenience
    bell = np.where(x<0.5, 0.5*(1-np.cos(4*np.pi*x)),0)
    
    return(bell)

def squareWave(x,alpha,beta):
    "A square wave as a function of position, x, which is 1 between alpha"
    "and beta (included) and zero elsewhere. \
    "
    phi = np.where(x>=alpha, 1, 0) - np.where(x>beta , 1, 0)   
    
    return (phi)


   

 
