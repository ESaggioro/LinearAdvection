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
        plt.plot(gridx.x, phis[ip], label=labels[ip])
 
    # further plot decorations
    plt.legend(loc='best')
    plt.xlabel('x' , fontsize = 12)
    plt.ylabel('$\phi$', fontsize = 12, rotation=0)
    plt.axhline(0, linestyle=':', color='black')
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.title( title , fontsize = 14)
    
    
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()
    
    
def plot_error (dx, errors, labels, colors,  outFile , show = 0, title = '', xlabel='' ):
    "Plot a list of errors for different numerical schemes on the same graph,"
    "all with different labels, colors and with double log scales"
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
    
    # set a function y = dx^2 and y = dx to contrast the error expected
    
    f2 = [x**2 for x in dx]
    f1 = dx

    # plot each of the phis with the corresponding legend
    for ip in range(len(errors)):
        plt.plot(dx, errors[ip], color = colors[ip], linewidth=0.3  , marker = 's', \
                 fillstyle = 'none', label=labels[ip])
    # plot the 'reference lines'
    ##plt.plot(dx,f1,label='+1')
    ##plt.plot(dx,f2,label='+2')

    
    # further plot decorations
    plt.legend(loc='best')
    
    plt.yticks(fontsize = 10)
    plt.xticks(dx, ['' for i in dx], fontsize = 10)
    
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='minor',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    direction= 'in', # ticks inward
    labelbottom='off') # labels along the bottom edge are off
    
    plt.xlabel( xlabel , fontsize = 12 )
    plt.ylabel('$l_2$' , fontsize = 12 ,rotation=0)
    
    plt.title( title , fontsize = 14)
    
        
    # set log scales
    plt.yscale('log')
    plt.xscale('log')
    
    # save plot to the outFile
    plt.savefig(outFile, bbox_inches='tight')
    
    # shows plot
    plt.show()
    
    # close plot
    plt.close()

        
    
    
    
    