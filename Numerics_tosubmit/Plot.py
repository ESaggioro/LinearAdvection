# =============================================================================
#  Plot many functions in the same figure and saves it to a 
#  output file. 
# =============================================================================


import matplotlib.pyplot as plt
import numpy as np

def plot_decoration(xlabel, ylabel, yrot, title):
    " Set plot decorations \
    "
    plt.legend(bbox_to_anchor=(0,1.1,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.tick_params(axis='x',which='minor',bottom='off',top='off',\
                    direction= 'in', labelbottom='off')
    plt.tick_params(axis='y',which='minor',bottom='off',top='off',\
                    direction= 'in', labelbottom='off')
    plt.xlabel(xlabel , fontsize = 12)
    plt.ylabel(ylabel , fontsize = 12, rotation = yrot , labelpad=15)
    plt.title( title , fontsize = 12)
    
    
def plot_Final (gridx, phis, labels, colors, linestyles, title = '', outFile=0 ):
    "Plot a list of solutions on the same graph, all with different labels,"
    "colors and linestyles, and write the result to outFile. "
    "The list of solutions is in the list of arrays, phis ; "
    "the list of labels (colors\linestyles) is in the list of strings, "
    "labels(colors\linestyles), the plot is saved in the file outFile "
    "All solutions are plotted against gridx.x\
    "
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the phis with the corresponding legend,color,linestyle
    for ip in range(len(phis)):
        plt.plot(gridx.x, phis[ip], color=colors[ip], linestyle=linestyles[ip]\
                 ,linewidth = 0.7, label=labels[ip])
    plt.axhline(0, color='black', linestyle = ':',linewidth = 0.6 )
    
    # further plot decorations
    plot_decoration('x', '$\phi$', 0, title)
    
    # save fuigure and show
    if outFile == 0: 
        plt.show()
        plt.close()
    
    else:
        plt.savefig(outFile, bbox_inches='tight')
        plt.show()
        plt.close()
    
def plot_Errors (logdx, logerrors, labels, colors, linestyles,  outFile=0 ):
    "Plot a list of errors for different numerical schemes on same graph"
    "all with different labels, colors, linestyles and write the result to a"
    "file, outFile. The list of errors is in the list of arrays, logerrors "
    "All errors are plotted aginst array logdx\
    "
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()

    # plot each of the errors with the corresponding legend
    for ip in range(len(logerrors)):
        plt.plot(logdx, logerrors[ip], color = colors[ip], \
                 linestyle=linestyles[ip], linewidth=0.8  ,  \
                 label=labels[ip])

    # further plot decorations
    plot_decoration( '$\Delta x$', '$error$', 90, '')
    
    # save plot to the outFile , show, close
    if outFile == 0: 
        plt.show()
        plt.close()
    
    else:
        plt.savefig(outFile, bbox_inches='tight')
        plt.show()
        plt.close()
    
def plot_MorV (times, M0, Mass , colors, labels,  ylabel, \
               ylim=[0,0], yticks=[0,0,0,0,0], outFile=0):
    "Plot a list of lists of Masses(or Variances) against time for different "
    "numerical schemes."
    "All with different labels and colors and write the result to outFile. "
    "The list of times in times, M0 is the constant expecated value, "
    " Mass is a list of arrays for each scheme"
    "If ylim amd yticks are not specified, plot is optimized for the yrange\
    "
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()  
    
    # set ylim
    minim_y=[]
    maxi_y= []
    
    # plot each of the Mass_Scheme(t) with the corresponding legend
    
    for i,M in enumerate(Mass):
        plt.plot(times, M ,color = colors[i] ,linewidth=0.7, label=labels[i])
        minim_y.append(min(M))
        maxi_y.append(max(M))
    
    plt.plot( times , M0*np.ones(len(times)) , color = 'black' , \
             linestyle = '-.', \
             linewidth=0.6, label = 'Exact' )
    
    # further plot decorations
    
    #ylimit
    delta = abs(max(maxi_y) - min(minim_y))/20 
    if ylim[0]==0:
        plt.ylim(min(minim_y)-delta,max(maxi_y)+delta)   
    else:
        plt.ylim(ylim)
    
    if yticks[0]!=0:
        plt.yticks( yticks,  fontsize = 10)
        plt.ticklabel_format( style = 'sci', axis = 'y', scilimit = (0,0))
    
    plot_decoration( '$t_{steps} $' , ylabel, 0, '')
    plt.legend(bbox_to_anchor=(0,1.1,1,0.2), loc="lower left",\
                mode="expand", ncol=3) #borderaxespad=0
    plt.tight_layout()
    
    # save plot to the outFile
    if outFile == 0: 
        plt.show()
        plt.close()
    
    else:
        plt.savefig(outFile, bbox_inches='tight')
        plt.show()
        plt.close()