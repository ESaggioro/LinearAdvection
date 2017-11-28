# =============================================================================
#  Plot many functions in the same figure and saves it to a 
#  output file. 
# =============================================================================


import matplotlib.pyplot as plt
import numpy as np

def plot_decoration(xlabel, ylabel, yrot, title):
    " Set plot decorations \
    "
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    plt.tick_params(axis='x',which='minor',bottom='off',top='off',\
                    direction= 'in', labelbottom='off')
    plt.xlabel(xlabel , fontsize = 12)
    plt.ylabel(ylabel , fontsize = 12, rotation = yrot , labelpad=20)
    plt.title( title , fontsize = 12)
    
    
def plot_Final (gridx, phis, labels, colors, linestyles, outFile , title = ''):
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
                 ,label=labels[ip])
    plt.axhline(0, color='black', linestyle = ':')
    
    
    # further plot decorations
    plot_decoration('x', '$\phi$', 0, title)
    
    # save fuigure and show
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()
    plt.close()
    
def plot_Errors (logdx, logerrors, labels, colors, linestyles,  outFile ):
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
    plt.savefig(outFile, bbox_inches='tight')
    plt.show()
    plt.close()
    
def plot_MorV (times, M0, Mass , colors, labels, outFileMass, ylabel):
    "Plot a list of lists of Masses(or Variances) against time for different "
    "numerical schemes. One graph for Mass and one for Variance."
    "All with different labels and colors and write the result to outFile. "
    "The list of times in times, list( schemes) of list(times) of masses is in "
    "Mass, same for Variance. \
    "
    # Initialise the plot
    plt.figure(2)
    plt.clf()
    plt.ion()  
    
    # set ylim
    minim_y=[]
    maxi_y= []
    
    # plot each of the Mass_Scheme(t) with the corresponding legend
    
    for i,M_scheme in enumerate(Mass):
        plt.plot(times, M_scheme ,color = colors[i] ,linewidth=0.7, label=labels[i])
        minim_y.append(min(M_scheme))
        maxi_y.append(max(M_scheme))
    
    plt.plot( times , M0*np.ones(len(times)) , color = 'black' , \
             linestyle = '-.', \
             linewidth=0.9, label = 'Exact' )
    
        
        
    # further plot decorations
    plot_decoration( '$t_{steps} $' , ylabel, 0, '')
    if ylabel == 'M':
        plt.ylim([min(minim_y),max(maxi_y)])
        plt.legend(bbox_to_anchor=(0,1.1,1,0.2), loc="lower left",\
                mode="expand", borderaxespad=0, ncol=3)
    
    # save plot to the outFile
    plt.savefig(outFileMass, bbox_inches='tight')
    plt.show()
    plt.close()
    