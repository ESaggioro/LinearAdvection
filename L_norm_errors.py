#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:32:41 2017

@author: es3017
"""

## This code computes l-norm error for 
## the output of a given numerical method : phi
## and the known analytical solution of the original equation : f
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi 


def main():
    
    # This function computes the l1 error norm of an output phi,
    # given f analytical solution
    def l1_norm (phi , f):
        
        if len(phi) != len(f):
            
            print( " Cannot compute l1 norm for functions with different \
                  number of points")
            l1= float('nan') 
            
        else:
        
            diff = phi - f
            l1 = np.sum (np.absolute(diff)) / np.sum(np.absolute(f))
            
        return(l1)
        
    # This function computes the l2 error norm of an output phi,
    # given f analytical solution   
    def l2_norm (phi , f):
        
        if len(phi) != len(f):
            
            print( " Cannot compute l1 norm for functions with different \
                  number of points")
            l2 = float('nan') 
            
        else:
        
            diff_sq = (phi - f)**2
            num = np.sqrt( np.sum (diff_sq))
            den = np.sqrt( np.sum ( f**2 ) ) 
            l2 = num / den
            
        return(l2)
        
    # This function computes the l_infty error norm of an output phi,
    # given f analytical solution    
    def linfty_norm (phi , f):
        
        if len(phi) != len(f):
            
            print( " Cannot compute l1 norm for functions with different \
                  number of points")
            linfty = float('nan') 
            
        else:
        
            diff_abs = np.absolute( (phi - f) )
            linfty = np.max( diff_abs) / np.max ( np.absolute (f) )
            
        return(linfty)
                
 
    # Test the norms with two simple arrays
    
    f1 = np.array([0,1,2,3])
    f2 = np.array([1,2,3,4])

    l1 = l1_norm(f1,f2)
    print(l1)
    
    l2 = l2_norm(f1,f2)
    print(l2)
    
    linfinity = linfty_norm( f1,f2)
    print(linfinity)

    
               

main()