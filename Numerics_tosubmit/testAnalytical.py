#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:14:44 2017

@author: es3017
"""

# This function is to test if Analytical behaves well.



exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 
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
    T = 100 # (seconds)
    tsteps = 100
    
    dt =np.float64( T / tsteps)
    u = c * Gridx.dx / dt
    
    print( ' u = ', u)
    
    
    
     # test on cosbell function
    cos0 , cosT = Analytical ( cosBell , Gridx , c, tsteps, L )
    
    print('max_cosT = %g and of max_cos0 = %g ' %(np.max(cosT),np.max(cos0)))
    u_num = (1.0/T)*(Gridx.x[np.argmax(cosT)] - Gridx.x[np.argmax(cos0)])
    print('u_num = %g' %u_num)
    print('u_true = %g' %u)
    
    
    plt.plot(Gridx.x , cos0, 'b--', label='CI')
    plt.plot(Gridx.x , cosT, 'm--', label='analy')
    plt.plot(Gridx.x[np.argmax(cos0)],max(cos0), color= 'red' , marker= '+')
    plt.plot(Gridx.x[np.argmax(cosT)], max(cosT), color= 'red' , marker= '+' )
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.title('c=%g , T=%g, tsteps=%g, nx=%g' %(c,T,tsteps,nx))
    #plt.legend(loc=1, ncol=1)
    plt.show()
    
    
    
    # TeST SLICING
    cosT_SLICE = Analytical_Periodic (cos0, c, tsteps ,Gridx  )
    
    print('max_cosTSLICE = %g and of max_cos0 = %g ' %(np.max(cosT_SLICE),np.max(cos0)))
    u_NUM = (1.0/T)*(Gridx.x[np.argmax(cosT_SLICE)] - Gridx.x[np.argmax(cos0)])
    print('u_NUM_SLICE = %g' %u_NUM)
    print('u_true = %g' %u)
    
    
    plt.plot(Gridx.x , cos0, 'b--', label='CI')
    plt.plot(Gridx.x , cosT, 'm--', label='analy hilary')
    plt.plot(Gridx.x , cosT_SLICE, 'g--', label='SLICE')
    plt.plot(Gridx.x[np.argmax(cos0)],max(cos0), color= 'red' , marker= '+')
    plt.plot(Gridx.x[np.argmax(cosT_SLICE)], max(cosT_SLICE), color= 'red' , marker= '+' )
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.title('c=%g , T=%g, tsteps=%g, nx=%g' %(c,T,tsteps,nx))
    plt.legend(loc=2, ncol=1)
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
main()