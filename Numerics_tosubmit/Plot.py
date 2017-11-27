
## This function plots many functions in the same figure and saves it to a 
## output file


import matplotlib.pyplot as plt
import numpy as np

def plot_Final (gridx, phis, labels, colors, linestyles, outFile , title = ''):
    "Plot a list of solutions on the same graph, all with different labels,"
    "colors and linestyles, and write the result to outFile. "
    "The list of solutions is in the list of arrays, phis ; "
    "the list of labels (colors\linestyles) is in the list of strings, "
    "labels(colors\linestyles), the plot is saved in the file outFile "
    "All solutions are plotted against gridx.x"
    
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the phis with the corresponding legend,color,linestyle
    for ip in range(len(phis)):
        plt.plot(gridx.x, phis[ip], color=colors[ip], linestyle=linestyles[ip]\
                 ,label=labels[ip])
 
    # further plot decorations
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.xlabel('x' , fontsize = 12)
    plt.ylabel('$\phi$', fontsize = 12, rotation=0)
    plt.axhline(0, color='black', linestyle = ':')
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.title( title , fontsize = 14)
    # save fuigure and show
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()
    # close plot
    plt.close()
    
def plot_error (logdx, logerrors, labels, colors, linestyles,  outFile ,\
                title = '', xlabel='$\Delta x$'):
    "Plot a list of errors for different numerical schemes on same graph"
    "all with different labels, colors, linestyles and write the result to a"
    "file, outFile. The list of errors is in the list of arrays, logerrors "
    "All errors are plotted aginst array logdx"
    
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the errors with the corresponding legend
    for ip in range(len(logerrors)):
        plt.plot(logdx, logerrors[ip], color = colors[ip], \
                 linestyle=linestyles[ip], linewidth=0.8  ,  \
                 fillstyle = 'none', label=labels[ip])

    # further plot decorations
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.yticks(fontsize = 10)
    plt.xticks(logdx, ['' for i in logdx], fontsize = 10)
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='minor',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    direction= 'in', # ticks inward
    labelbottom='off') # labels along the bottom edge are off
    
    plt.xlabel( xlabel , fontsize = 12 )
    plt.ylabel('$error$' , fontsize = 12 ,rotation=90, labelpad=10)
    plt.title( title , fontsize = 14) 
    
    # save plot to the outFile
    plt.savefig(outFile, bbox_inches='tight')
    # shows plot
    plt.show()
    # close plot
    plt.close()
    
def plot_MassVariance (times, M0, V0 , Mass , Variance , colors, labels, \
                       outFileMass, outFileVar, xlabel='$t_{steps} $' ):
    "Plot a list of lists of Masses(and Variances) against time for different "
    "numerical schemes. One graph for Mass and one for Variance."
    "All with different labels and colors and write the result to outFile. "
    "The list of times in times, list( schemes) of list(times) of masses is in "
    "Mass, same for Variance. "
    
    
    # plot options 
    font = {'size'   : 12}
    plt.rc('font', **font)
    
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()  
    
    # MASS :
    minim_y=[]
    maxi_y= []
    
    # plot each of the Mass_Scheme(t) with the corresponding legend
    plt.plot( times , M0*np.ones(len(times)) , color = 'black' , \
             linestyle = '-.', \
             linewidth=0.9, label = 'Exact' )
    for i,M_scheme in enumerate(Mass):
        plt.plot(times, M_scheme ,color = colors[i] ,linewidth=0.7, label=labels[i])
        minim_y.append(min(M_scheme))
        maxi_y.append(max(M_scheme))
        
        
    # further plot decorations
    plt.legend(bbox_to_anchor=(0,1.1,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.yticks(fontsize = 10)
    plt.xticks(fontsize = 10)
    plt.ylim([min(minim_y),max(maxi_y)])
    
    #plt.ylim([min(minim_y) ,max(maxi_y)])
    
    plt.xlabel( xlabel , fontsize = 12 )
    plt.ylabel('$M$' , fontsize = 12 ,rotation=0 ,labelpad=10)
    plt.title( 'Mass conservation' , fontsize = 14)
    
    # save plot to the outFile
    plt.savefig(outFileMass, bbox_inches='tight')
    # shows plot
    plt.show()
    # close plot
    plt.close()
    
    # VARIANCE :
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()  
    
    # plot each of the Mass_Scheme(t) with the corresponding legend
    
    plt.plot( times , V0*np.ones(len(times)) , color = 'black' , \
             linestyle = '-.', \
             linewidth=0.9, label = 'Exact' )
    for i,V_scheme in enumerate(Variance):
        plt.plot(times, V_scheme ,color = colors[i] ,linewidth=0.7, label=labels[i])
    
    
    
    # further plot decorations
    plt.legend(bbox_to_anchor=(0,1.1,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.yticks(fontsize = 10)
    plt.xticks(fontsize = 10)
    
    plt.xlabel( xlabel , fontsize = 12 )
    plt.ylabel('$V$' , fontsize = 12 ,rotation=0)
    plt.title( 'Variance conservation' , fontsize = 14)
    
    # save plot to the outFile
    plt.savefig(outFileVar, bbox_inches='tight')
    # shows plot
    plt.show()
    # close plot
    plt.close()
    
    

    


        
    
    
    
    