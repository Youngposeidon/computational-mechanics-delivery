# test file for project 1
# basically just all the jupyter stuff in standard python so I can look at 
# variables in spyder

import matplotlib.pyplot as plt
import PhysPlot
import numpy as np
import csv

# Define velocity, initial position and final time.
v = 5.0
x0 = 3.0
tf = 6.0

# Compute final position and print result.
x = x0 + v * tf
print(x)

# The following two lines of code use functions from the "numpy" library to create arrays.
# The first runs from 0 to tf, which we defined above as 6, with increment steps of 0.03.
t = np.linspace(0.0, tf, int(tf/0.03))

# The second array is made only of zeroes and has the same number of elements that the
# array "t" has. This number can be obtained for any array with the function len()
x = np.zeros(len(t))

for i in range(len(x)):
    x[i] = x0 + v * t[i]
    
    # Creating the plot from scratch with matplotlib (plt)
plt.figure(figsize=(7, 5))
plt.plot(t, x) # Plots the graph, with t on the x-axis, x(t) on the y-axis
plt.xlabel("Time (s)") # gives the x-axis title
plt.ylabel("Position (m)") # gives the y-axis title
plt.grid() # displays the gridlines

# Does the same thing as the above code but in one line.
PhysPlot.plot(t, x, "Time (s)", "Position (m)") 

# Euler Method integration of Linear Fluid Resistance

dt = .001                      # Size of time steps.
tf = 5                         # Final time (in units of tau). Solution will be calculated up to this point.
u0 = 0                         # Initial condition, velocity at time 0.
t = np.arange(0, tf, dt)       # Values of every time point to compute the solution at. From start to stop in steps of dt
u = np.zeros(len(t))           # Creates an array the same size as t that is all zeroes. Will contain the solutions to the velocity at every time step.
u[0] = u0                      # Assign the value of the first entry of the velocity array with the initial condition. Python arrays are zero-based.

for i in range(0, len(t)-1):   # This is how you create an iterator loop in Python.
    a = 1 - u[i]               # Normalized Linear equation for the acceleration.
    u[i+1] = u[i] + dt * a     # This is Euler's method. Assigning the next value of the velocity.
    
    # print(u)
    # annoying so I turned it off
    
# This is the analytical solution. We will use it to compare to our numerical solution.
def linear_analytic_v(u0, T):
    # u0 is the initial velocity in units of terminal velocity
    # T is an array of times in units of the time constant tau
    return (u0 - 1) * np.exp(-T) + 1

# Plot analytic and numerical solutions
PhysPlot.plot(t, linear_analytic_v(u0,t), r"Time ($t/\tau$)", r"Speed ($v/v_t$)")
PhysPlot.plot(t, u, r"Time ($t/\tau$)", r"Speed ($v/v_t$)")
# This is used to plot two or more curves in a single graph. The first argument is the x-axis array, 
# the second argument is a list with as many y-axis arrays as wanted. The third argument is a list of the same size
# With labels for aech y-axis array. The last two arguments are the axes titles.
PhysPlot.multiplot(t, [linear_analytic_v(u0, t), u], ["Analytic", "Numerical"], r"Time ($t/\tau$)", r"Speed ($v/v_t$)")

# Plot the difference between Numerical and Analytic Solution.
PhysPlot.plot(t, u-linear_analytic_v(u0,t), r"Time ($t/\tau$)", r"Speed ($v/v_t$)")