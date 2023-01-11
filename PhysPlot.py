# Jonathan Gilchrist
# July 21, 2022,
#
# The idea should be to simplify plotting in Mechanics 2200.
#
#


import matplotlib.pyplot as plt
import math
from mpl_toolkits import mplot3d


# Builds a plot with the given information. Only plots a single line
def plot(xAxis, yAxis, xTitle, yTitle):
    plt.figure(figsize=(7, 5))
    plt.plot(xAxis, yAxis)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.grid()


# Builds a graph with 2 lines of the given information, my goal will be to allow this to generalize to n lines graphed
# on a single plot
def multiplot(xAxis, yAxes, ylbls, xTitle, yTitle):
    plt.figure(figsize=(7, 5))
    for ii in range(len(yAxes)):
        plt.plot(xAxis, yAxes[ii], label=ylbls[ii])
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.grid()
    plt.legend(loc="best")

# 3D plotting
def Plot3D(x, y, z, xlabel, ylabel, zlabel):
    fig = plt.figure()

    ax = plt.axes(projection='3d')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)

    ax.plot3D(x, y, z)

# Plots the trajectory of a planet and adds a dot to signify the starting position of the orbiting object and another dot for the object being orbited
def planetPlot(x, y, xlabel, ylabel):
    plt.plot(x[0], y[0], 'go', marker=".", markersize=10)
    plt.plot(0, 0, 'yo', marker='.', markersize=20)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()

# a function that returns the angle of rotation for a planet in orbit
def angle(x,y):

    if x == 0:
        if y>0:
            return math.pi()/2
        else:
            return 3*(math.pi())/2
    if y ==0:
        if x>0:
            return 0
        else:
            return math.pi
    if x>0:
        if y>0:
            return math.atan(y/x)
        elif y<0:
            return 2*math.pi + math.atan(y/x)
    if x<0:
        return math.pi + math.atan(y/x)
