#!/usr/bin/python
"""
File: Lagrange_poly2.py

Copyright (c) 2016 Michael Seaman

License: MIT

FROM ASSIGNMENT 2
Creates a graph function of the Lagrangian interpolation formula,
graphing both the original function as well as the approximated one
"""


import numpy as np
import matplotlib.pyplot as plt
import math
import Lagrange_poly1


def p_L(x, xp, yp):
    return Lagrange_poly1.p_L(x, xp, yp)
    

def L_k(x, k, xp):
    return Lagrange_poly1.L_k(x, k, xp)


def test_p_l(xp = np.linspace(0,math.pi, 5), yp = np.array([math.sin(y) for y in np.linspace(0,math.pi, 5)]) ):
    Lagrange_poly1.test_p_l(xp, yp)


    
def graph(f, n, xmin, xmax, resolution=101):
    """
    Graphs f(x) as well as the Lagrangian interpolation approximation of
    f(x) with n points on matplotlib
    """
    g = np.vectorize(f)
    xlist = np.linspace(xmin, xmax, resolution)
    ylist = g(xlist)
    interpolatedlist = np.array([p_L(x, xlist, ylist ) for x in np.linspace(xmin, xmax, n)])
    plt.plot(xlist, ylist)
    plt.plot(np.linspace(xmin, xmax, n), interpolatedlist,'g.')
    plt.show()
    
def graph(xp, yp, resolution = 1001):
    """
    Graphs just the linear interpolation of the data points provided
    """
    xList = np.linspace(xp[0], xp[-1], resolution)
    interpolatedList = np.zeros(resolution)
    for i in xrange(resolution):
        interpolatedList[i] = p_L(xList[i], xp, yp)
    plt.plot(xList, interpolatedList)
    plt.show()
