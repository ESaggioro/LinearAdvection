#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:48:17 2017

@author: es3017
"""

## This function computes the mass and Variance of a function phi

import numpy as np

SMALL = 1e-10 #is a small number to check periodicity of Initial conditions


def Mass( phi , dx ):
    " Compute the Mass of a function phi (with periodic-boundary on a grid \
    with space discretization dx):\
    M = dx Sum_{j=1 to nx-1} phi_j. \
    First value phi_0 is excluded because, provided periodic boundaries, \
    it coincides with the last phi_{nx-1}"
    
    # Check function is periodic
    if np.abs(phi[0] - phi[-1])> SMALL :
        print('Careful: the function does not have periodic boundaries')
    
    # Compute Mass
    M = dx * sum(phi[1:])
    
    
    return( M )
    
def Variance( phi , dx ):
    " Compute the Variance of a function phi (with periodic-boundary on a grid \
    with space discretization dx): \
    V = dx Sum_{j=1 to nx-1} (phi_j)**2 . \
    First value phi_0 is excluded because, provided periodic boundaries, \
    it coincides with the last phi_{nx-1}"
    
    # Check function is periodic
    if np.abs(phi[0] - phi[-1])> SMALL :
        print('Careful: the function does not have periodic boundaries')
    
    # Compute Variance
    V = dx * sum(np.square(phi[1:]))
    
    
    return( V )
    
    