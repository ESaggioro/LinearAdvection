# =============================================================================
# l-norm errors (l_2 and l_infinity) of phi in comparison to phiExact
# =============================================================================

import numpy as np

def check_length( phi, phiExact ):
    " Checks is the array have same length"
    if len(phi) != len(phiExact):
        print( " Cannot compute l2 norm for functions with different \
              number of points")
        return( False ) 
    else:
        return( True)

            
def l2_norm (phi , phiExact):
    "This function computes the l2 error norm of a numerical approx phi,"
    "given f analytical solution"
        
    l2 = check_length( phi, phiExact)
    if l2 :
        num =  np.sum(np.square(phi-phiExact))
        den = np.sum ( np.square(phiExact ) ) 
        l2 = (num / den)**0.5
    else:
        l2 = np.NaN       
    
    return(l2)
        
  
def linfty_norm (phi , phiExact):
    "This function computes the l_infty error norm of a numerical approx phi,\
    given f analytical solution"
    
    linfty = check_length( phi, phiExact)
    if linfty :
        diff_abs = np.absolute( (phi - phiExact) )
        linfty = np.max( diff_abs) / np.max ( np.absolute (phiExact) )
    else:
        linfty = np.NaN          
    
    return(linfty)
    
    

                