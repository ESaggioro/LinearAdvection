#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:25:42 2017

@author: es3017
"""

## This function plots many functions in the same figure and saves it to a 
## required file


import matplotlib.pyplot as plt


# use exec because in this way python re-reads the file every time
exec(open("./InitialConditions.py").read())
exec(open("./grid.py").read()) 

def plot_Final (gridx, phis, labels, outFile , show = 0, title = '' ):
    "Plot a list of solutions on the same graph, all with different labels"
    "and write the result to outFile. The list of solutions is in the list"
    "of arrays, phis, and the list of labels is in the string list, labels."
    "All solutions are plotted against x"
    # plot options (large fonts)
    font = {'size'   : 14}
    plt.rc('font', **font)
    
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the phis with the corresponding legend
    for ip in range(len(phis)):
        plt.plot(gridx.x, phis[ip], 'b.', label=labels[ip])
 
    # further plot decorations
    plt.legend(loc='best')
    plt.xlabel('x')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle=':', color='black')
    plt.title( title )
    
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()
    
    
def plot_l2error (dx2, errors, labels, outFile , show = 0, title = '', xlabel='' ):
    "Plot a list of l2 errors for different numerical schemes on the same graph,"
    "all with different labels"
    "and write the result to outFile. The list of errors is in the list "
    "of arrays, errors, and the list of labels is in the string list, labels."
    "All solutions are plotted against dx**2"
    # plot options (large fonts)
    font = {'size'   : 14}
    plt.rc('font', **font)
    
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the phis with the corresponding legend
    for ip in range(len(errors)):
        plt.plot(dx2, errors[ip], 'b.', label=labels[ip])
 
    # further plot decorations
    plt.legend(loc='best')
    plt.xlabel( xlabel )
    plt.ylabel('$l_2(\phi)$')
    plt.axhline(0, linestyle=':', color='black')
    plt.title( title )
    
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()

        
    
    
    
    