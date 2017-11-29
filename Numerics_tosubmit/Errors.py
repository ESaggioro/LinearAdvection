# =============================================================================
# l-norm errors (l_2 and l_infinity) of phi in comparison to phiExact
# =============================================================================

import numpy as np

def check_length( phi, phiExact ):
    " Checks if the arrays have same length. \
    "
    if len(phi) != len(phiExact):
        print( " Cannot compute l2 norm for functions with different \
              number of points")
        return(False) 
    else:
        return(True)

            
def l2_norm (phi , phiExact):
    "This function computes the l2 error norm of a numerical approx phi,"
    "given f analytical solution. \
    "
    l2 = check_length( phi, phiExact)
    if l2 :
        num =  np.sum(np.square(phi-phiExact))
        den = np.sum ( np.square(phiExact ) ) 
        l2 = (num / den)**0.5
    else:
        l2 = np.NaN       
    
    return(l2)
        
  
def linfty_norm (phi , phiExact):
    "This function computes the l_infty error norm of a numerical approx phi,"
    "given f analytical solution. \
    "
    linfty = check_length( phi, phiExact)
    if linfty :
        diff_abs = np.absolute( (phi - phiExact) )
        linfty = np.max( diff_abs) / np.max ( np.absolute (phiExact) )
    else:
        linfty = np.NaN          
    
    return(linfty)
    
def ErrorsAgainstResolution( Nx, Lx, C, norm_type, Nt , i_c, *args):
    " This function computes the l-norm errors for all advection schemes and "
    " for different grid meshes, given a fix Courant number C. "
    " The meshes are defined via the number of points in the grid in list of "
    " integers, Nx; grid length is Lx; the Courant number, C; the type of norm"
    " is the string, norm_type; the initial condition type (and extra args) "
    "is string i_c (and *args). To ensure that the physical velocity U is "
    "constant, provide the tsteps Nt such that the ratio with the "
    "correspondant Nx is fix. "
    " Returns a list of arrays of Log10(errors) and a likewise ordered list "
    " of scheme names.\
    "  
    # define the grids
    gridx = [ Grid( n , Lx ) for n in Nx ]
    # Initialize to 0 all phi0, phiExact and phi_Schemes
    # for the various grids
    phi0     = [ np.zeros(n ) for n in Nx] 
    phiExact = [ np.zeros(n ) for n in Nx] 
    phi_FTBS = [ np.zeros(n ) for n in Nx]
    phi_CTCS = [ np.zeros(n ) for n in Nx]
    phi_CNCS = [ np.zeros(n ) for n in Nx]
    phi_LAX  = [ np.zeros(n ) for n in Nx]
    # Error vectors initialized to 0 scalar, for the various x-grids
    er_FTBS = np.zeros(len(Nx)) 
    er_CTCS = np.zeros(len(Nx)) 
    er_CNCS = np.zeros(len(Nx)) 
    er_LAX  = np.zeros(len(Nx)) 
    
    # Error for each Nx: 
    for i,grid in enumerate(gridx): # run over different grid resolution
        phi0[i]     = i_c (grid.x, *args)
        phiExact[i] = Analytical ( i_c , grid , C , Nt[i] ,Lx )
        phi_FTBS[i] = FTBS ( grid, phi0[i] , C , Nt[i] )
        phi_CTCS[i] = CTCS ( grid, phi0[i] , C , Nt[i] )
        phi_CNCS[i] = CNCS ( grid, phi0[i] , C , Nt[i] )
        phi_LAX[i]  = LaxWendroff ( grid, phi0[i] , C , Nt[i] )
        
        er_FTBS[i] = norm_type (phi_FTBS[i] ,phiExact[i])
        er_CTCS[i] = norm_type (phi_CTCS[i] ,phiExact[i])
        er_CNCS[i] = norm_type (phi_CNCS[i] ,phiExact[i])
        er_LAX[i]  = norm_type (phi_LAX[i]  ,phiExact[i])
   
    labels = ['FTBS','CTCS', 'CNCS', 'LAX' ] 
    
    return([np.log10(er_FTBS), np.log10(er_CTCS), np.log10(er_CNCS), \
            np.log10(er_LAX)], labels ) 
    

                
