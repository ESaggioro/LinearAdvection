# FinalCode
Final Code for Numerics Corse Work
This folder contains the code for the 29th of November deadline of the Numerics assignment .

main_LinearAdvection.py is the main code for the Linear Advection equation problem. The main calls all the numerical schemes and the numerical tests I have implemented. I have selected a few choices of set-up (i.e grid points, time steps, Courant number C, type of initial condition) to show how my code behaves. In the final report I will include more plots for different choice of the set-up parameters.  
First block: the main calls four numerical methods (FTBS, CTCS, CNCS and Lax Wendroff) for 
for two different set-up and plots the results.
Second block: on a new set-up, the main calls the functions to calculate the Mass and Variance of the numerical solutions at each time step, and plots the result. 
Third block: keeping C fix and change grid point, the main calls a function that compute the l-2 norm error for all schemes and plot results. 

Grid.py sets up the 1-d space grid, provided number of grid points and total lenght.

InitialConditions.py sets up a profile on a grid, aloowing to choose a cosBell or a square wave function.

Analytical.py computes the anlytical solution of the linear advection eq., given an initial condition type, the Courant number and the total number of time steps.

AdvectionSchemes.py contains all the implemented schemes: FTBS, CTCS, CNCS and LaxWendroff. They advect a given initial profile using a provided C and timesteps. It also include a function that runs all the schemes together.

Errors.py contains functions that computes the l_2 norm and the l_infinity norm errors given a numerical solution and the analytical; also contains a function that computes the error for all schemes and different grid resolutions.

MassVariance.py computes mass and variance of a profile defined on a grid of space step dx. Contains also a function that computes the mass and variance as function of time, for all schemes.

Plot.py contains three functions: plot of schemes and analytical solution after tsteps; plot of errors vs grid mesh; plot of Mass or Variance in time .
