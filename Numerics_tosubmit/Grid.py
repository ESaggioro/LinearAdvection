#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:56:53 2017

@author: es3017
"""
# Define a class called Grid to define how to partition the 1-d length

# from hilary code in Bitbucket

import numpy as np

# Set the space grid in 1-d 
    
class Grid(object):
    "Store all grid data and calculates dx and x locations."
    "The grid is assumed periodic."
    def __init__(self, nx, Length , xmin=0.0):
        self.xmin = xmin
        self.length =np.float64(Length)
        self.xmax = xmin + Length 
        self.nx = int(nx)
        # The x locations, including the end point
        self.x = np.linspace(self.xmin, self.length, self.nx)
        
        self.dx =self.x[1]-self.x[0]
        


