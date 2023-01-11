# Jonathan Gilchrist
# August 31, 2022,
#
# Reduces down the long complex methods from project 1 and 2 into simplified and callable methods.
#
#
# f2 is the force and must be calculated prior to using, since f2 is calculated at every time
# step, f2 changes every time we recalculate. Unless you want to be editing f2 for each method
# every time you use it, this is the best we can do.
#
#


def eulerMethod(y, f2, dx):
    yout = y + f2 * dx
    return yout


# xp, yp, f2, and f2p need to be calculated prior to being fed into this method
def rungeKuttaMethod(x, y, xp, yp, f2, f2p, dx):
    yout = y + f2p * dx
    xout = x + yp * dx
    return xout, yout


# x1 is the previous step, x2 is the current step, f2 is the force, dx is the discrete step size
def verletMethod(x1, x2, f2, dx):
    x3 = 2 * x2 - x1 + f2 * (dx ** 2)
    yout = (x3 - x1) / (2 * dx)
    return x3, yout
