# l-norm errors for the pair (phi, f), where phi is the numerical approximation
# of a function f.   

import numpy as np

def check_length(phi,f):
    " Checks is the array have same length"
    if len(phi) != len(f):
        print( " Cannot compute l2 norm for functions with different \
              number of points")
        return( False ) 
    else:
        return( True)

            
def l2_norm (phi , f):
    "This function computes the l2 error norm of a numerical approx phi,"
    "given f analytical solution"
        
    l2 = check_length(phi,f)
    if l2 :
        num =  np.sum(np.square(phi-f))
        den = np.sum ( np.square(f ) ) 
        l2 = (num / den)**0.5
    else:
        l2 = np.NaN       
    
    return(l2)
        
  
def linfty_norm (phi , f):
    "This function computes the l_infty error norm of a numerical approx phi,\
    given f analytical solution"
    
    linfty = check_length(phi,f)
    if linfty :
        diff_abs = np.absolute( (phi - f) )
        linfty = np.max( diff_abs) / np.max ( np.absolute (f) )
    else:
        linfty = np.NaN          
    
    return(linfty)
    
    

                