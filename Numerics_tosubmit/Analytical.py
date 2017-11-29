# =============================================================================
# Function to compute the analytical solution of 1-d linear advection eq,
# given an initial condition, Courant number and time steps. 
# =============================================================================


# read the files defining the initial conditions 
exec(open("./InitialConditions.py").read())

def Analytical ( InCond_type , grid , c, tsteps , *args):

    " Analytical solution of linear advection eqaution in 1d, given "
    " the string telling the initial profile type InCond_type (chosen from "
    " InitialConditions.py), the grid-object grid (defined as in grid.py ), "
    " the Courant number c and the number of time steps tsteps. "
    " Extra args depends on the choice of the initial profile type.\
    "
    
    # Exact solution is the initial condition shifted around the domain
    phiExact = InCond_type((grid.x - c*tsteps*grid.dx)%grid.length, *args)
    
    return( phiExact )
    

