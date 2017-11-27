## CNCS implicit scheme for linear advection with periodic boundaries 
## Accuracy : 2 - 2
## Stability : c in R 

import scipy as spy
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve


#import matplotlib as plt

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions

def CNCS (gridx, phi0, c ,tsteps ):

    "Linear advection of initial profile phi0 using CNCS, Courant number c"
    "for tsteps time-steps "
    # gridx = the grid object representing x-axis
    # phi0 = initial contition
    # c = courant number
    # tsteps = number of time steps
    
    if np.abs(phi0[0] -phi0[-1])> SMALL :
        print('Careful: your c.i. PhiO does not have periodic boundaries')
        
    # The vector v used in CNCS does not have last element of phi0
    N = gridx.nx - 1     # dimension of vector for CNCS 
    v = phi0[:N]
    
    # Built the matrices Q and M s.t. M*v^{n+1}=Q*v^n  
    diagonals = [ np.ones(N), \
                  0.25*c*np.ones(N-1),\
                 -0.25*c*np.ones(N-1),\
                  0.25*c*np.ones(1),\
                 -0.25*c*np.ones(1)]
    
    Q = diags(diagonals, [0, -1,+1,+(N-1),-(N-1)], format='csr')
    
    M = diags(diagonals, [0, 1,-1,-(N-1),+(N-1)],  format='csr')
    
    # x:=v^{n+1} the unknown. It is calculated solving 
    # M*x = b := Q*v^n
    for t in range(tsteps):
        
        v = spsolve(M, Q * v)
        #plt.plot(gridx.x[:-1] , v  , label='iteration %g' %t)
        
    #plt.legend()
    #plt.show()
        
    # Recover the periodic solution phi   
    phi = np.append(v, v[0]) 
    
    return(phi)
    

