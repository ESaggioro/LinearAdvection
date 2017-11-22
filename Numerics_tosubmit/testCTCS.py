#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:36:02 2017

@author: es3017
"""

# This function is to test if CTCS behaves well.



exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
exec(open("./CTCS.py").read())
exec(open("./Analytical.py").read())
exec(open("./Analytical_Slicing.py").read())


import matplotlib.pyplot as plt
import numpy as np

def main():
    
    # Set the grid
    nx = 40
    L = 1.0 # (meters)
    Gridx = Grid (nx,L)
    
    # Set T , c , Time steps
    
    c = 0.2
    T = np.asarray([10, 30, 50, 100, 150, 250]) # (seconds)
    tsteps = T * 1
    print(tsteps)
    
    dt =np.float64( T / tsteps)
    u = c * Gridx.dx / dt
    
    print( ' u = ', u)
    
    
    
    # test on cos bell function
    
    cos0 = cosBell( Gridx.x ,L )
    for nt in tsteps: 
        cos0H , cosT_hilary = Analytical ( cosBell , Gridx , c, nt, L )
        cosT_SLICE = Analytical_Periodic (cos0, c, nt ,Gridx  )
        cosCTCS = CTCS (Gridx , cos0 , c , nt)
        
        plt.clf()
        plt.ion()
        plt.plot(Gridx.x , cosT_hilary, 'g--', linewidth=0.8, \
                 label='Exact ')
        plt.plot(Gridx.x , cosCTCS, color='orange', linestyle='--',\
                 linewidth=1.5, label='CTCS')
        plt.xlabel('x')
        plt.ylabel('$\phi$')
        plt.title(' tsteps=%g, nx=%g , c=%g' %(nt,nx,c))
        plt.legend(loc=2, ncol=1)
        plt.savefig('CTCS_bell_tsteps%g.pdf' %nt, bbox_inches='tight')
        plt.show()
        plt.close()
    
    
main()