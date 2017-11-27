# =============================================================================
# A class called Grid to define how to partition the 1-d length
# =============================================================================

import numpy as np

class Grid(object):
    "Store all grid data and calculates dx and x locations."
    "The grid is assumed periodic. "
    "Inputs are nx number of points(including end point) and Length the length" 
    
    def __init__(self, nx, Length , xmin=0.0):
        
        self.xmin = xmin
        self.length =np.float64(Length)
        self.xmax = xmin + Length 
        self.nx = int(nx)
        # The x locations, including the end point
        self.x = np.linspace(self.xmin, self.length, self.nx)
        # The dx length of the partition
        self.dx =self.x[1]-self.x[0]
        


