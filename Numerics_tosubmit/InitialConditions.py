#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:41:31 2017

@author: es3017
"""

# Various different initial conditions for linear advection

# from hilary code in Bitbucket


import numpy as np

def cosBell(x):
    "Function defining a cosine bell as a function of position, x"
### The lambda keyword lets you define a function in one line       ###
    bell = lambda x: 0.5*(1 - np.cos(4*np.pi*x))
### chooses bell(x) where condition is true, else chooses zeros     ###
    return np.where((x<0.5) | (x>=1.0), bell(x), 0.)

def squareWave(x,alpha,beta):
    "A square wave as a function of position, x, which is 1 between alpha"
    "and beta and zero elsewhere. The initialisation is conservative so"
    "that each phi contains the correct quantity integrated over a region"
    "a distance dx/2 either side of x"
    
    ### WHY you WANT this CONSERVATION??
    
    phi = np.zeros_like(x)
    
    # The grid spacing (assumed uniform)
    dx = x[1] - x[0]
    
    # Set phi away from the end points (assume zero at the end points)
    for j in range(len(x)):
        # edges of the grid box (using west and east notation)
        xw = x[j] - 0.5*dx
        xe = x[j] + 0.5*dx
        
        #integral quantity of phi
        phi[j] = max((min(beta, xe) - max(alpha, xw))/dx, 0)
        
    return (phi)
        
def sine (x, k, A):
    "A sin function with amplitude A and wavenumber k and is 0 in x=0"
    
    # Make sure your amplitude is positive and k is an integer
    A = abs(A)
    k = int(k)
    
    sine = np.sin(k * np.pi * x) 
    return( sine )
    

 
